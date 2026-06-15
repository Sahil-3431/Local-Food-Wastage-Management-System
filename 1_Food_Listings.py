import streamlit as st
import pandas as pd
from db_connection import fetch_data
import plotly.express as px

st.title("🍱 Food Listings")

df = fetch_data(
    "SELECT * FROM food_listings"
)

city = st.selectbox(
    "Select City",
    ["All"] + sorted(df['location'].unique())
)

food_type = st.selectbox(
    "Select Food Type",
    ["All"] + sorted(df['food_type'].unique())
)

meal_type = st.selectbox(
    "Select Meal Type",
    ["All"] + sorted(df['meal_type'].unique())
)

if city != "All":
    df = df[df['location']==city]

if food_type != "All":
    df = df[df['food_type']==food_type]

if meal_type != "All":
    df = df[df['meal_type']==meal_type]

st.dataframe(df,use_container_width=True)

st.plotly_chart(px.bar(df,x='location',y='quantity',title='Food Quantity by Location'),use_container_width=True)

st.plotly_chart(px.pie(df,values='quantity',names='meal_type',title='Meal Type Distribution',hole=.4),use_container_width=True)

st.plotly_chart(px.bar(df,x='food_type',y='quantity',title='Food Quantity by Type'),use_container_width=True)

st.plotly_chart(px.histogram(df,x='expiry_date',title='Expiry Date Distribution'),use_container_width=True)
