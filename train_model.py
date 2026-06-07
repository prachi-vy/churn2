import pandas as pd
import joblib

from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Load dataset
df = pd.read_csv("customer_churn.csv")

# Remove customerID
df.drop("customerID", axis=1, inplace=True)

# Convert TotalCharges
df["TotalCharges"] = pd.to_numeric(
    df["TotalCharges"],
    errors="coerce"
)

# Remove missing values
df.dropna(inplace=True)

# Encode categorical columns
encoders = {}

for col in df.columns:
    if df[col].dtype == "object" or str(df[col].dtype) == "str":
        le = LabelEncoder()

        df[col] = le.fit_transform(df[col])

        encoders[col] = le

# Features and target
X = df.drop("Churn", axis=1)
y = df["Churn"]

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Train model
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(X_train, y_train)

predictions = model.predict(X_test)

accuracy = accuracy_score(
    y_test,
    predictions
)

print("Accuracy:", accuracy)

# Save model
joblib.dump(model, "model/churn_model.pkl")

# Save encoders
joblib.dump(encoders, "model/encoders.pkl")

# Save metadata for the web app
joblib.dump({"accuracy": round(accuracy * 100, 1)}, "model/metadata.pkl")

print("Model Saved Successfully!")
print("Encoders Saved Successfully!")