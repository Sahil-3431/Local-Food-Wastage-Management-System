import streamlit as st
from db_connection import fetch_data
from queries import queries

st.title("📝 SQL Queries")

selected = st.selectbox(
    "Choose Query",
    list(queries.keys())
)

df = fetch_data(
    queries[selected]
)

st.dataframe(
    df,
    use_container_width=True
)
