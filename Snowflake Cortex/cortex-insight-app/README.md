# Cortex Insight App

An interactive Streamlit application that uses **Snowflake Cortex** to analyze documents like books, movie scripts, and customer reviews — extracting themes, emotions, and sentiment insights using LLMs.

---

## Features

- Analyze narrative content using Snowflake Cortex LLM (`mixtral-8x7b`)
- Supports categories like Books, Movie Scripts, and Customer Reviews
- Extract:
  - Character emotion and tone
  - Themes and motifs
  - Memorable quotes
  - Sentiment progression over time
- Live AI analysis with markdown output
- Snowflake-native backend (no file uploads required)

---

## Technologies

- **[Streamlit](https://streamlit.io/)** – for building the UI
- **[Snowflake Cortex](https://docs.snowflake.com/en/user-guide/cortex-overview)** – for prompt-based AI completions
- **Python 3.9+**

