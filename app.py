from flask import Flask, render_template, request
import joblib
import os

app = Flask(__name__)

MODEL_PATH = "model/churn_model.pkl"
ENCODERS_PATH = "model/encoders.pkl"
METADATA_PATH = "model/metadata.pkl"

model = joblib.load(MODEL_PATH)
encoders = joblib.load(ENCODERS_PATH)
metadata = joblib.load(METADATA_PATH) if os.path.exists(METADATA_PATH) else {"accuracy": None}

FEATURE_ORDER = [
    "gender", "SeniorCitizen", "Partner", "Dependents", "tenure",
    "PhoneService", "MultipleLines", "InternetService", "OnlineSecurity",
    "OnlineBackup", "DeviceProtection", "TechSupport", "StreamingTV",
    "StreamingMovies", "Contract", "PaperlessBilling", "PaymentMethod",
    "MonthlyCharges", "TotalCharges",
]

CATEGORICAL_FIELDS = {
    "gender", "Partner", "Dependents", "PhoneService", "MultipleLines",
    "InternetService", "OnlineSecurity", "OnlineBackup", "DeviceProtection",
    "TechSupport", "StreamingTV", "StreamingMovies", "Contract",
    "PaperlessBilling", "PaymentMethod",
}


def encode_features(form_data):
    features = []
    for field in FEATURE_ORDER:
        value = form_data.get(field, "")
        if field in CATEGORICAL_FIELDS:
            features.append(int(encoders[field].transform([value])[0]))
        else:
            features.append(float(value))
    return features


@app.route("/")
def home():
    field_options = {
        field: list(encoders[field].classes_)
        for field in CATEGORICAL_FIELDS
    }
    return render_template(
        "index.html",
        field_options=field_options,
        model_accuracy=metadata.get("accuracy"),
    )


@app.route("/predict", methods=["POST"])
def predict():
    field_options = {
        field: list(encoders[field].classes_)
        for field in CATEGORICAL_FIELDS
    }

    try:
        features = encode_features(request.form)
        prediction = model.predict([features])[0]
        probabilities = model.predict_proba([features])[0]
        churn_probability = round(float(probabilities[1]) * 100, 1)

        if prediction == 1:
            result = "Customer Will Churn"
            risk_level = "high" if churn_probability >= 70 else "medium"
        else:
            result = "Customer Will Stay"
            risk_level = "low"

        return render_template(
            "index.html",
            prediction=result,
            churn_probability=churn_probability,
            risk_level=risk_level,
            will_churn=prediction == 1,
            field_options=field_options,
            form_data=request.form,
            model_accuracy=metadata.get("accuracy"),
        )
    except (ValueError, KeyError) as error:
        return render_template(
            "index.html",
            error="Please check your inputs and try again.",
            field_options=field_options,
            form_data=request.form,
            model_accuracy=metadata.get("accuracy"),
        )


if __name__ == "__main__":
    app.run(debug=True)

