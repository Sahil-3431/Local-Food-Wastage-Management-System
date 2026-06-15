import streamlit as st
from sqlalchemy import create_engine
from sqlalchemy import text

engine = create_engine(
    "postgresql://postgres:root@localhost:5432/food_wastage_db"
)

st.title("➕ CRUD Operations")

tab1,tab2,tab3 = st.tabs(
["➕ Add Food",
"✏️ Update Food",
"🗑 Delete Food"]
)

with tab1:
    st.subheader("Add New Food")
    col1, col2 = st.columns(2)

    with col1:
        food_id = st.number_input(
            "Food ID",
            min_value=1,
            step=1
        )

        food_name = st.text_input("Food Name")
        quantity = st.number_input(
            "Quantity",
            min_value=1
        )

        expiry_date = st.date_input(
            "Expiry Date"
        )

    with col2:
        provider_id = st.number_input(
            "Provider ID",
            min_value=1
        )

        provider_type = st.text_input(
            "Provider Type"
        )

        location = st.text_input(
            "Location"
        )

        food_type = st.selectbox(
            "Food Type",
            [
                "Vegetarian",
                "Non-Vegetarian",
                "Vegan"
            ]
        )

        meal_type = st.selectbox(
            "Meal Type",
            [
                "Breakfast",
                "Lunch",
                "Dinner",
                "Snacks"
            ]
        )

    if st.button("Add Food"):
        try:
            with engine.begin() as conn:
                conn.execute(
                    text("""
                        INSERT INTO food_listings
                        (
                            food_id,
                            food_name,
                            quantity,
                            expiry_date,
                            provider_id,
                            provider_type,
                            location,
                            food_type,
                            meal_type
                        )
                        VALUES
                        (
                            :food_id,
                            :food_name,
                            :quantity,
                            :expiry_date,
                            :provider_id,
                            :provider_type,
                            :location,
                            :food_type,
                            :meal_type
                        )
                    """),
                    {
                        "food_id": int(food_id),
                        "food_name": food_name,
                        "quantity": int(quantity),
                        "expiry_date": expiry_date,
                        "provider_id": int(provider_id),
                        "provider_type": provider_type,
                        "location": location,
                        "food_type": food_type,
                        "meal_type": meal_type
                    }
                )
            st.success("Food Added Successfully")
        except Exception as e:
            st.error(e)

with tab2:

    st.subheader("Update Food Quantity")

    update_food_id = st.number_input(
        "Food ID",
        min_value=1,
        key="update_food"
    )

    new_quantity = st.number_input(
        "New Quantity",
        min_value=1,
        key="new_qty"
    )

    if st.button("Update Food"):
        try:
            with engine.begin() as conn:
                result = conn.execute(
                    text("""
                        UPDATE food_listings
                        SET quantity=:qty
                        WHERE food_id=:id
                    """),
                    {
                        "qty": int(new_quantity),
                        "id": int(update_food_id)
                    }
                )

            if result.rowcount > 0:
                st.success(
                    "Food Updated Successfully"
                )
            else:
                st.warning(
                    "Food ID Not Found"
                )
        except Exception as e:
            st.error(e)


with tab3:

    st.subheader("Delete Food")

    delete_food_id = st.number_input(
        "Food ID To Delete",
        min_value=1,
        key="delete_food"
    )

    if st.button("Delete Food"):

        try:
            with engine.begin() as conn:
                result = conn.execute(
                    text("""
                        DELETE FROM food_listings
                        WHERE food_id=:id
                    """),
                    {
                        "id": int(delete_food_id)
                    }
                )

            if result.rowcount > 0:
                st.success(
                    "Food Deleted Successfully"
                )
            else:
                st.warning(
                    "Food ID Not Found"
                )
        except Exception as e:
            st.error(e)
