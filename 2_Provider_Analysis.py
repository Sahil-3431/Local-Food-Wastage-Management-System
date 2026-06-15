import streamlit as st
import plotly.express as px
from db_connection import fetch_data

st.title("🏢 Provider Analysis")

query = """
SELECT
provider_type,
SUM(quantity) total_food
FROM food_listings
GROUP BY provider_type
"""

df = fetch_data(query)

fig = px.bar(
    df,
    x='provider_type',
    y='total_food',
    title='Food Contribution by Provider Type'
)

st.plotly_chart(fig,use_container_width=True)

st.plotly_chart(px.pie(df,values='total_food',names='provider_type',title='Provider Type Distribution',hole=.4),use_container_width=True)

st.plotly_chart(px.bar(df.sort_values('total_food', ascending=False).head(10),x='provider_type',y='total_food',title='Top 10 Providers by Donation'),use_container_width=True)

st.plotly_chart(px.histogram(df,x='total_food',title='Food Quantity Distribution by Provider'),use_container_width=True)

st.plotly_chart(px.box(df,x='provider_type',y='total_food',title='Food Quantity Distribution by Provider Type'),use_container_width=True)


