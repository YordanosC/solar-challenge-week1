import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from app.utils import load_data, create_boxplot, create_summary_table

# Streamlit app configuration
st.set_page_config(page_title="Solar Data Dashboard", layout="wide")

# Title and description
st.title("Solar Data Cross-Country Comparison")
st.markdown("Explore solar radiation metrics (GHI, DNI, DHI) across Benin, Sierra Leone, and Togo.")

# Load data
@st.cache_data
def load_cached_data():
    return load_data()

df = load_cached_data()

# Country selection widget
countries = st.multiselect(
    "Select Countries",
    options=['Benin', 'Sierra Leone', 'Togo'],
    default=['Benin', 'Sierra Leone', 'Togo']
)

# Filter data based on selection
filtered_df = df[df['Country'].isin(countries)]

# Boxplot for GHI
if countries:
    st.subheader("GHI Boxplot")
    fig = create_boxplot(filtered_df, 'GHI', countries)
    st.pyplot(fig)
else:
    st.warning("Please select at least one country.")

# Summary Table
st.subheader("Summary Statistics")
summary_df = create_summary_table(filtered_df, countries)
st.table(summary_df)

# Top Regions by GHI
st.subheader("Top Regions by Average GHI")
avg_ghi = filtered_df.groupby('Country')['GHI'].mean().sort_values(ascending=False)
fig, ax = plt.subplots(figsize=(8, 6))
avg_ghi.plot(kind='bar', ax=ax, color=['#1f77b4', '#ff7f0e', '#2ca02c'])
ax.set_title('Average GHI by Country')
ax.set_xlabel('Country')
ax.set_ylabel('Average GHI (W/m²)')
st.pyplot(fig)

# Key Observations
st.subheader("Key Observations")
st.markdown("""
- **GHI Variability**: Check the boxplot to see which country has the highest median GHI and variability.
- **Regional Potential**: The bar chart ranks countries by average GHI, highlighting top solar potential.
- **Data Insights**: Use the summary table to compare mean, median, and standard deviation across countries.
""")