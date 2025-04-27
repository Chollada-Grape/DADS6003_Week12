# pages/1_Stores_by_Country.py

import streamlit as st
import duckdb as db
import pandas as pd

st.title("🌎 Starbucks Stores by Country")

df = pd.read_csv("Starbucks.csv")
db.register('df', df)

# Sidebar - select country
country = st.sidebar.selectbox('Choose your country:', df['Country'].unique())

# Query
results = db.sql(f"SELECT * FROM df WHERE Country='{country}'").df()
count = results.shape[0]

st.metric(label=f"Total Starbucks in {country}", value=count)
st.dataframe(results)

# Bar chart: stores per city in selected country
store_by_city = db.sql(f"""
    SELECT City, COUNT(*) AS Num_Stores
    FROM df
    WHERE Country='{country}'
    GROUP BY City
    ORDER BY Num_Stores DESC
""").df()

st.bar_chart(store_by_city.set_index('City'))
