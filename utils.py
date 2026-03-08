import pandas as pd

def clean_data(df):
    # Remove empty rows
    df = df.dropna()

    # Ensure Amount is numeric
    df["Amount"] = pd.to_numeric(df["Amount"], errors="coerce")

    # Drop invalid values
    df = df.dropna(subset=["Amount"])

    return df


def detect_large_transactions(df):
    insights = []

    avg = df["Amount"].mean()

    for amount in df["Amount"]:
        if amount > avg * 2.5:
            insights.append(f"⚠️ Possible unusual transaction detected: ₹{amount}")

    return insights