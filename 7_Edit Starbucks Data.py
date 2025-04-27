
# pages/4_Edit_Starbucks_Data.py

import streamlit as st
import pandas as pd

st.title("📝 Edit Starbucks Data")

# Load Data
df = pd.read_csv("Starbucks.csv")

# Display editable table
st.write("### You can edit the data below 👇")
edited_df = st.data_editor(
    df,
    num_rows="dynamic",  # Allow adding new rows
    use_container_width=True,
    key="starbucks_editor"
)

# Show edited Data
st.write("### Preview of Edited Data:")
st.dataframe(edited_df)

# Option to Save
if st.button('Save Changes'):
    edited_df.to_csv('Starbucks_Edited.csv', index=False)
    st.success('✅ Changes saved to "Starbucks_Edited.csv"')
