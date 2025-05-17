import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("World Population Visualization")

# Load data
@st.cache_data
def load_data():
    df = pd.read_csv("API_SP.POP.TOTL_DS2_en_csv_v2_XXXXXXX.csv", skiprows=4)
    return df

df = load_data()

# Show data
st.subheader("Raw Data")
st.dataframe(df.head())

# Dropdown to select year
years = df.columns[4:-1]  # Skip first 4 metadata columns
selected_year = st.selectbox("Select Year", sorted(years, reverse=True))

# Top N countries slider
top_n = st.slider("Top N Countries", min_value=5, max_value=20, value=10)

# Filter and sort data
top_countries = df[['Country Name', selected_year]].dropna().sort_values(by=selected_year, ascending=False).head(top_n)

# Plot bar chart
st.subheader(f"Top {top_n} Countries by Population in {selected_year}")
fig, ax = plt.subplots()
ax.bar(top_countries['Country Name'], top_countries[selected_year])
ax.set_ylabel("Population")
ax.set_xticklabels(top_countries['Country Name'], rotation=45, ha='right')
st.pyplot(fig)
