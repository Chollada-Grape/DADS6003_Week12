
# pages/2_Top_Cities.py

import streamlit as st
import duckdb as db
import pandas as pd

st.title("🏙️ Top Cities with Most Starbucks Stores")

df = pd.read_csv("Starbucks.csv")
db.register('df', df)

# Query top cities
top_cities = db.sql("""
    SELECT City, Country, COUNT(*) AS Num_Stores
    FROM df
    GROUP BY City, Country
    ORDER BY Num_Stores DESC
    LIMIT 10
""").df()

st.dataframe(top_cities)

# Bar chart
st.bar_chart(top_cities.set_index('City')['Num_Stores'])
