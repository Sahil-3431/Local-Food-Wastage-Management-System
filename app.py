import streamlit as st
from db_connection import fetch_data


st.set_page_config(
    page_title="Food Wastage Management",
    page_icon="🍲",
    layout="wide"
)

st.title("🍲 Local Food Wastage Management System")

providers = fetch_data("SELECT COUNT(*) total FROM providers")
receivers = fetch_data("SELECT COUNT(*) total FROM receivers")
foods = fetch_data("SELECT SUM(quantity) total FROM food_listings")
claims = fetch_data("SELECT COUNT(*) total FROM claims")

col1,col2,col3,col4 = st.columns(4)

with col1:
    st.metric("Providers",providers.iloc[0,0])

with col2:
    st.metric("Receivers",receivers.iloc[0,0])

with col3:
    st.metric("Food Listings",foods.iloc[0,0])

with col4:
    st.metric("Claims",claims.iloc[0,0])

st.markdown("---")

st.image("https://images.unsplash.com/photo-1504674900247-0877df9cc836")

st.subheader("Project Overview")

st.write("""
Connect food providers with NGOs and needy people.
Track donations and claims.
Reduce food wastage.
Generate business insights.
""")

# st.sidebar.image("logo.png")
st.sidebar.title("Food Wastage System")

st.sidebar.info(
"""
Reduce Waste
Feed People
Track Donations
"""
)
