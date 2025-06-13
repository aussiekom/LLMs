import streamlit as st
import pandas as pd
import re

from prompts import Prompts
from utils import sql_escape, connect_snowflake, read_custom, fetch_documents

st.set_page_config(layout="wide")
st.title("📚 CortexScript: AI-Powered Text Insight Tool")

categories = ["Books", "Movies", "Reviews"]
selected_category = st.selectbox("Select Category:", categories)
selected_title = st.text_input("Enter Title or Keyword:")

if st.button("Analyze Document", type="primary"):
    with st.spinner("Connecting to Snowflake Cortex..."):
        conn = connect_snowflake()

    doc_data = fetch_documents(conn, selected_category, selected_title)

    if not doc_data:
        st.warning("No matching document found.")
    else:
        result = {}
        parsed_text = doc_data["parsed_text"]
        url = doc_data.get("url")

        for prompt in Prompts:
            sql = f"""
            SELECT snowflake.cortex.AI_COMPLETE(
                'mixtral-8x7b',
                '{sql_escape(prompt.start)}' || '{sql_escape(parsed_text)}' || '{sql_escape(prompt.end)}'
            ) AS response;
            """
            response = read_custom(conn, sql)
            result[prompt.name] = response["RESPONSE"].iloc[0]

        st.header(f"Insights for: {doc_data['title']}")
        for prompt in Prompts:
            st.subheader(prompt.name)
            st.markdown(result[prompt.name].replace("\\n", "\n"), unsafe_allow_html=True)

        if url:
            st.markdown(f"**Source URL:** {url}")
