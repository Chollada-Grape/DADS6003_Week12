import streamlit as st
import duckdb as db
import pandas as pd

st.title("🗺️ Starbucks Store Map :coffee:")

df = pd.read_csv("Starbucks.csv")
db.register('df', df)

# Filter by country
country = st.sidebar.selectbox('Select a Country to view stores:', df['Country'].unique())

filtered_df = db.sql(f"SELECT * FROM df WHERE Country='{country}'").df()

# Fix column names to lowercase
filtered_df = filtered_df.rename(columns={'Latitude': 'latitude', 'Longitude': 'longitude'})

# Map
if 'latitude' in filtered_df.columns and 'longitude' in filtered_df.columns:
    st.map(filtered_df[['latitude', 'longitude']])
else:
    st.write("No geolocation data available.")

st.dataframe(filtered_df)

