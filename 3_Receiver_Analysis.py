import streamlit as st
import plotly.express as px
from db_connection import fetch_data

st.title("👨‍👩‍👧 Receiver Analysis")

query = """
SELECT
r.name,
COUNT(*) claims
FROM claims c
JOIN receivers r
ON c.receiver_id=r.receiver_id
GROUP BY r.name
ORDER BY claims DESC
LIMIT 10
"""

df = fetch_data(query)

fig = px.bar(
    df,
    x='name',
    y='claims',
    title='Top Receivers'
)

st.plotly_chart(fig,use_container_width=True)

st.plotly_chart(px.pie(df,values='claims',names='name',title='Receiver Distribution',hole=.4),use_container_width=True)

st.plotly_chart(px.line(df,x='name',y='claims',title='Claims by Receiver'),use_container_width=True)

st.plotly_chart(px.histogram(df,x='claims',title='Claims Distribution by Receiver'),use_container_width=True)
