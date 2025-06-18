import pandas as pd
import streamlit as st

# Load and clean data
file_path = "McDonalds_Financial_Statements.csv"
df = pd.read_csv(file_path)

# Clean column names
df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_').str.replace('(', '').str.replace(')', '')

# Convert financial columns to numeric (remove $ and commas)
for col in df.columns[1:]:  # Skip 'year'
    df[col] = df[col].replace(r'[\$,]', '', regex=True).astype(float)

# Streamlit UI
st.title("📊 McDonald's Financial Explorer")

st.markdown("Explore trends in McDonald's key financial metrics over time.")

# Dropdown to select a metric
metric = st.selectbox("Select a metric to plot:", df.columns[1:])

# Line chart of the selected metric
st.line_chart(df.set_index('year')[metric])