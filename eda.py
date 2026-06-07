import pandas as pd

df = pd.read_csv("customer_churn.csv")

print("DATA TYPES")
print(df.dtypes)

print("\nCHURN DISTRIBUTION")
print(df["Churn"].value_counts())
