import snowflake.connector
import pandas as pd

def connect_snowflake():
    return snowflake.connector.connect(
        user="USERNAME",
        password="PASSWORD",
        account="ACCOUNT",
        warehouse="WAREHOUSE",
        database="DATABASE",
        schema="PUBLIC"
    )

def sql_escape(text):
    if text is None:
        return ""
    return text.replace("'", "''")

def read_custom(conn, query):
    with conn.cursor() as cur:
        cur.execute(query)
        columns = [col[0] for col in cur.description]
        rows = cur.fetchall()
        return pd.DataFrame(rows, columns=columns)

def fetch_documents(conn, category, title_keyword):
    table_map = {
        "Books": "books_table",
        "Movies": "scripts_table",
        "Reviews": "reviews_table"
    }

    table = table_map.get(category)
    if not table:
        return {}

    query = f"""
    SELECT doc_id, title, url, parsed_text
    FROM {table}
    WHERE LOWER(title) LIKE '%{title_keyword.lower()}%'
    LIMIT 1;
    """

    df = read_custom(conn, query)
    if df.empty:
        return {}
    
    return df.iloc[0].to_dict()
