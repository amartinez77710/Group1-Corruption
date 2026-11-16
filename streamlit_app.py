import pandas as pd
import streamlit as st

st.set_page_config(
    page_title="Village of Cuba Water & Sewer Financials", layout="wide"
)

st.title(
    "📉 Village of Cuba Water & Sewer Financial Deficit ($3.10M Total Loss)"
)
st.write(
    "Interactive financial trends and operating deficit analysis (2021–2025)"
    " exported from MATLAB."
)


# Load data with caching
@st.cache_data
def load_data():
  return pd.read_csv("cuba_water_sewer_financials.csv")


try:
  df = load_data()

  # Set Year as string index for cleaner chart plotting
  chart_df = df.set_index("Year")

  # Display Data Table
  st.subheader("Financial Summary Table ($ Thousands)")
  st.dataframe(df, use_container_width=True)

  # Layout into two columns mimicking MATLAB subplots
  col1, col2 = st.columns(2)

  with col1:
    st.subheader("Operating Revenues vs. Expenses")
    rev_exp_df = chart_df[[
        "Operating_Revenues_Thousands",
        "Total_Expenses_Thousands",
    ]].rename(
        columns={
            "Operating_Revenues_Thousands": "Operating Revenues ($K)",
            "Total_Expenses_Thousands": "Total Operating Expenses ($K)",
        }
    )
    st.bar_chart(rev_exp_df)

  with col2:
    st.subheader("Annual Utility Operating Loss")
    loss_df = chart_df[["Operating_Loss_Thousands"]].rename(
        columns={"Operating_Loss_Thousands": "Operating Loss ($K)"}
    )
    st.bar_chart(loss_df, color="#732626")

except FileNotFoundError:
  st.error(
      "⚠️ `cuba_water_sewer_financials.csv` not found. Please run your MATLAB"
      " script to generate and push the CSV file to your repository."
  )
