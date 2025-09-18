import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("metadata.csv")
df['publish_time'] = pd.to_datetime(df['publish_time'], errors='coerce')
df['year'] = df['publish_time'].dt.year

st.title("CORD-19 Data Explorer")
st.write("Explore COVID-19 research metadata")

# Interactive year filter
year_range = st.slider("Select Year Range", 2015, 2025, (2020, 2021))
filtered = df[df['year'].between(year_range[0], year_range[1])]

# Plot publications by year
year_counts = filtered['year'].value_counts().sort_index()
st.bar_chart(year_counts)

# Show sample data
st.write(filtered.head(10))
