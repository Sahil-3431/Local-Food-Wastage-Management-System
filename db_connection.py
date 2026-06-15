from sqlalchemy import create_engine
import pandas as pd

engine = create_engine(
    "postgresql://postgres:root@localhost:5432/food_wastage_db"
)

def fetch_data(query):
    return pd.read_sql(query, engine)

