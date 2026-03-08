import pandas as pd
from utils import clean_data, detect_large_transactions

def categorize(description):
    description = str(description).lower()

    if "uber" in description or "ola" in description:
        return "Transport"
    elif "zomato" in description or "swiggy" in description:
        return "Food"
    elif "netflix" in description or "spotify" in description:
        return "Subscriptions"
    elif "amazon" in description:
        return "Shopping"
    else:
        return "Other"


def analyze_transactions(df):

    df = clean_data(df)

    df["Category"] = df["Description"].apply(categorize)

    category_spending = df.groupby("Category")["Amount"].sum()

    insights = []

    top_category = category_spending.idxmax()
    insights.append(f"Highest spending category: {top_category}")

    insights += detect_large_transactions(df)

    ai_advice = ai_financial_advice(category_spending)

    return {
    "category_spending": category_spending,
    "insights": insights,
    "ai_advice": ai_advice
    }

def ai_financial_advice(category_spending):

    advice = []

    if category_spending.get("Food", 0) > 5000:
        advice.append("Reduce food delivery spending.")

    if category_spending.get("Shopping", 0) > 4000:
        advice.append("Consider limiting discretionary shopping.")

    if category_spending.get("Subscriptions", 0) > 1500:
        advice.append("Review unused subscriptions.")

    advice.append("Try saving at least 20% of your monthly income.")

    return advice