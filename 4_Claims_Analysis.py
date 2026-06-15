import streamlit as st
import plotly.express as px
from db_connection import fetch_data

st.title("📦 Claims Analysis")

query = """
SELECT
status,
COUNT(*) total
FROM claims
GROUP BY status
"""

df = fetch_data(query)

fig = px.pie(
    df,
    names='status',
    values='total',
    hole=.4,
    title='Claims Distribution by Status'
)

st.plotly_chart(fig,use_container_width=True)

st.plotly_chart(px.bar(df,x='status',y='total',title='Claims by Status'),use_container_width=True)

st.plotly_chart(px.histogram(df,x='total',title='Claims Distribution by Status'),use_container_width=True)

st.plotly_chart(px.line(df,x='status',y='total',title='Claims Trend by Status'),use_container_width=True)

st.plotly_chart(px.box(df,x='status',y='total',title='Claims Distribution by Status'),use_container_width=True)

st.plotly_chart(px.histogram(df,x='status',y='total',title='Claims Distribution by Status'),use_container_width=True)

st.plotly_chart(px.treemap(df,path=['status'],values='total',title='Claims Treemap by Status'),use_container_width=True)


