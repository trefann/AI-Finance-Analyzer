import plotly.express as px
import streamlit as st
import pandas as pd
from analyzer import analyze_transactions

st.title("AI Personal Finance Analyzer")

uploaded_file = st.file_uploader("Upload Bank Statement CSV")

if uploaded_file:
    df = pd.read_csv(uploaded_file)

    st.subheader("Raw Transactions")
    st.write(df)

    results = analyze_transactions(df)

    st.subheader("Spending Summary")
    st.write(results["category_spending"])

    st.subheader("Top Insights")
    for tip in results["insights"]:
        st.write("- " + tip)

    st.subheader("AI Financial Advisor")
    st.write(results["ai_advice"])

    # Spending breakdown chart
    st.subheader("Spending Breakdown")

    category_df = results["category_spending"].reset_index()
    category_df.columns = ["Category", "Amount"]

    fig = px.pie(
        category_df,
        values="Amount",
        names="Category",
        title="Expense Distribution"
    )

    st.plotly_chart(fig)

    # Bar chart
    st.subheader("Category Spending")

    bar_fig = px.bar(
        category_df,
        x="Category",
        y="Amount",
        title="Spending by Category"
    )

    st.plotly_chart(bar_fig)
