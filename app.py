import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

st.set_page_config(
    page_title="Village of Cuba Financial Dashboard",
    page_icon="📊",
    layout="wide",
)

# -------------------------------------------------------------------
# Data from net.m: Financial Statement Data
# Dashes in the original statement were represented as zero.
# -------------------------------------------------------------------
years = ["2021", "2022", "2023", "2024", "2025", "Total"]

financial_rows = [
    "Gain/Loss on Sale",
    "Interest Expense",
    "Total Non-Operating",
    "Income Before Transfers",
    "Operating Grants",
    "Total Contributions",
    "Change in Net Position",
    "Beginning Net Position",
    "Restatement",
    "Restated Beginning Position",
    "Ending Net Position",
]

financial_values = [
    [0, 0, 410, 0, 0, 410],
    [-8223, -1159, -7268, -7440, -7795, -31885],
    [-8223, -1159, -6858, -7440, -7795, -31475],
    [-434491, -447226, -711194, -801774, -734604, -3129289],
    [201944, 245745, 0, 44433, 326402, 818524],
    [201944, 245745, 0, 44433, 326402, 818524],
    [-232547, -201481, -711194, -757341, -408202, -2310765],
    [4488995, 4314545, 4249816, 3538622, 2781281, 19373259],
    [58097, 136752, 0, 0, -4540, 190309],
    [4547092, 4451297, 4249816, 3538622, 2776741, 19563568],
    [4314545, 4249816, 3538622, 2781281, 2368539, 17252803],
]

financial_df = pd.DataFrame(financial_values, index=financial_rows, columns=years)
financial_df.index.name = "Financial Statement Item"

# -------------------------------------------------------------------
# Data from Graph_Cuba.m: Water & Sewer Financials (values in $K)
# -------------------------------------------------------------------
cuba_df = pd.DataFrame({
    "Year": [2021, 2022, 2023, 2024, 2025],
    "Operating Revenues ($K)": [405.565, 421.905, 412.235, 504.557, 496.658],
    "Total Operating Expenses ($K)": [831.833, 867.972, 1116.571, 1298.891, 1223.467],
    "Operating Loss ($K)": [426.268, 446.067, 704.336, 794.334, 726.809],
})

# -------------------------------------------------------------------
# Header
# -------------------------------------------------------------------
st.title("Village of Cuba Financial Dashboard")
st.caption("Financial statement and water & sewer operating results, 2021–2025")

tab_statement, tab_utility = st.tabs([
    "Financial Statement",
    "Water & Sewer",
])

with tab_statement:
    st.subheader("Financial Statement Data")

    total_col1, total_col2, total_col3 = st.columns(3)
    total_col1.metric("Total Income Before Transfers", f"${financial_df.loc['Income Before Transfers', 'Total']:,.0f}")
    total_col2.metric("Total Operating Grants", f"${financial_df.loc['Operating Grants', 'Total']:,.0f}")
    total_col3.metric("Total Change in Net Position", f"${financial_df.loc['Change in Net Position', 'Total']:,.0f}")

    st.markdown("#### Statement table")
    st.dataframe(
        financial_df.style.format("${:,.0f}"),
        use_container_width=True,
    )

    st.markdown("#### Compare annual financial measures")
    measure_options = [
        "Income Before Transfers",
        "Operating Grants",
        "Change in Net Position",
    ]
    selected_measures = st.multiselect(
        "Choose measures to display",
        options=measure_options,
        default=measure_options,
    )

    if selected_measures:
        chart_df = (
            financial_df.loc[selected_measures, ["2021", "2022", "2023", "2024", "2025"]]
            .T.rename_axis("Year")
            .reset_index()
        )
        chart_long = chart_df.melt(
            id_vars="Year",
            var_name="Measure",
            value_name="Amount ($)",
        )
        fig = px.bar(
            chart_long,
            x="Year",
            y="Amount ($)",
            color="Measure",
            barmode="group",
            title="Financial Performance by Year",
            labels={"Amount ($)": "Amount (USD)"},
        )
        fig.add_hline(y=0, line_color="black", line_width=1)
        fig.update_layout(legend_title_text="", yaxis_tickformat="$,.0f")
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.info("Select at least one measure to display the chart.")

with tab_utility:
    st.subheader("Water & Sewer Operating Results")

    total_loss = cuba_df["Operating Loss ($K)"].sum()
    latest = cuba_df.iloc[-1]

    kpi1, kpi2, kpi3 = st.columns(3)
    kpi1.metric("Cumulative Operating Loss (2021–2025)", f"${total_loss:,.1f}K")
    kpi2.metric("2025 Operating Revenue", f"${latest['Operating Revenues ($K)']:,.1f}K")
    kpi3.metric("2025 Operating Expenses", f"${latest['Total Operating Expenses ($K)']:,.1f}K")

    left, right = st.columns(2)

    with left:
        revenue_expense_fig = go.Figure()
        revenue_expense_fig.add_trace(go.Bar(
            x=cuba_df["Year"],
            y=cuba_df["Operating Revenues ($K)"],
            name="Operating Revenues",
            marker_color="#2E7DB2",
        ))
        revenue_expense_fig.add_trace(go.Bar(
            x=cuba_df["Year"],
            y=cuba_df["Total Operating Expenses ($K)"],
            name="Total Operating Expenses",
            marker_color="#D63E38",
        ))
        revenue_expense_fig.update_layout(
            title="Operating Revenues vs. Expenses",
            barmode="group",
            yaxis_title="USD ($ Thousands)",
            xaxis_title="Year",
            legend_title_text="",
        )
        st.plotly_chart(revenue_expense_fig, use_container_width=True)

    with right:
        loss_fig = px.bar(
            cuba_df,
            x="Year",
            y="Operating Loss ($K)",
            text=cuba_df["Operating Loss ($K)"].map(lambda x: f"${x:,.0f}K"),
            title="Annual Utility Operating Loss",
            labels={"Operating Loss ($K)": "Operating Loss (USD $ Thousands)"},
        )
        loss_fig.update_traces(
            marker_color="#732626",
            textposition="outside",
            cliponaxis=False,
        )
        loss_fig.update_layout(yaxis_range=[0, 950], xaxis_title="Year")
        st.plotly_chart(loss_fig, use_container_width=True)

    st.markdown("#### Water & sewer data table")
    st.dataframe(
        cuba_df.style.format({
            "Operating Revenues ($K)": "${:,.3f}K",
            "Total Operating Expenses ($K)": "${:,.3f}K",
            "Operating Loss ($K)": "${:,.3f}K",
        }),
        hide_index=True,
        use_container_width=True,
    )

st.divider()
st.caption(
    "Source: supplied MATLAB files net.m and Graph_Cuba.m. "
    "The app reproduces the values in those scripts; amounts in the Water & Sewer tab are shown in thousands of dollars."
)
