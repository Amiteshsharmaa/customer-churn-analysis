# Customer Churn Analysis
# Python + Pandas + Matplotlib
import pandas as pd
# Load dataset
df = pd.read_csv("customer_churn.csv")
# Basic dataset inspection
print(df.head())
print (df.shape)
print (df.columns)
print(df.dtypes)
print(df.isnull().sum())
print(df.duplicated().sum())
print(df["Churn"].value_counts())
# Churn analysis
churn_rate = df["Churn"].value_counts(normalize=True) * 100

print(churn_rate)
# Churn by contract type
print(pd.crosstab(df["Contract"], df["Churn"]))
print(pd.crosstab(df["Contract"], df["Churn"], normalize="index") * 100)
print(df["tenure"].describe())
# Average tenure by churn
print(df.groupby("Churn")["tenure"].mean())
# Average monthly charges by churn
print(df.groupby("Churn")["MonthlyCharges"].mean())
print(pd.crosstab(df["PaymentMethod"], df["Churn"], normalize="index") * 100)
print(pd.crosstab(df["InternetService"], df["Churn"], normalize="index") * 100)
print(pd.crosstab(df["SeniorCitizen"], df["Churn"], normalize="index") * 100)
print(pd.crosstab(df["Partner"], df["Churn"], normalize="index") * 100)
print(pd.crosstab(df["Dependents"], df["Churn"], normalize="index") * 100)
print(pd.crosstab(df["gender"], df["Churn"], normalize="index") * 100)
print(pd.crosstab(df["OnlineSecurity"], df["Churn"], normalize="index") * 100)
print(pd.crosstab(df["TechSupport"], df["Churn"], normalize="index") * 100)
print(pd.crosstab(df["OnlineBackup"], df["Churn"], normalize="index") * 100)
churn_count = df["Churn"].value_counts()

print(churn_count)
# Data visualization
import matplotlib.pyplot as plt
# Churn rate by contract type
contract_churn = pd.crosstab(
    df["Contract"],
    df["Churn"],
    normalize="index"
) * 100
# Churn rate by contract type
contract_churn["Yes"].plot(kind="bar")

plt.title("Churn Rate by Contract Type")
plt.xlabel("Contract Type")
plt.ylabel("Churn Rate (%)")
plt.xticks(rotation=0)
plt.show()
payment_churn = pd.crosstab(
    df["PaymentMethod"],
    df["Churn"],
    normalize="index"
) * 100
# Churn rate by payment method
payment_churn["Yes"].plot(kind="bar")

plt.title("Churn Rate by Payment Method")
plt.xlabel("Payment Method")
plt.ylabel("Churn Rate (%)")
plt.xticks(rotation=45)
plt.show()
internet_churn = pd.crosstab(
    df["InternetService"],
    df["Churn"],
    normalize="index"
) * 100
# Churn rate by internet service
internet_churn["Yes"].plot(kind="bar")

plt.title("Churn Rate by Internet Service")
plt.xlabel("Internet Service")
plt.ylabel("Churn Rate (%)")
plt.xticks(rotation=0)
plt.show()
# Average monthly charges by churn
monthly_charges = df.groupby("Churn")["MonthlyCharges"].mean()

monthly_charges.plot(kind="bar")

plt.title("Average Monthly Charges by Churn")
plt.xlabel("Churn")
plt.ylabel("Average Monthly Charges")
plt.xticks(rotation=0)
plt.show()
# Average tenure by churn
tenure_churn = df.groupby("Churn")["tenure"].mean()

tenure_churn.plot(kind="bar")

plt.title("Average Tenure by Churn")
plt.xlabel("Churn")
plt.ylabel("Average Tenure (Months)")
plt.xticks(rotation=0)
plt.show()
# Final churn summary

churn_summary = df["Churn"].value_counts()

print("\nFinal Churn Summary:")
print(churn_summary)
# Key Business Insights

print("\nKey Business Insights:")
print("1. Month-to-month customers have the highest churn rate.")
print("2. Churned customers have lower average tenure.")
print("3. Churned customers have higher average monthly charges.")
print("4. Electronic check customers have a higher observed churn rate.")
print("5. Fiber optic customers have a higher observed churn rate.")
# Summary Table

summary = pd.DataFrame({
    "Metric": [
        "Total Customers",
        "Churned Customers",
        "Stayed Customers",
        "Overall Churn Rate"
    ],
    "Value": [
        len(df),
        (df["Churn"] == "Yes").sum(),
        (df["Churn"] == "No").sum(),
        round((df["Churn"] == "Yes").mean() * 100, 2)
    ]
})

print("\nSummary Table:")
print(summary)
# Overall Churn Distribution

df["Churn"].value_counts().plot(kind="bar")

plt.title("Customer Churn Distribution")
plt.xlabel("Churn")
plt.ylabel("Number of Customers")
plt.xticks(rotation=0)
plt.show()