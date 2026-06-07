# ChurnGuard — Customer Churn Prediction

A beginner-friendly machine learning web app that predicts whether a telecom customer is likely to leave (churn). Built with Python, Flask, and scikit-learn.

![Python](https://img.shields.io/badge/Python-3.10+-blue)
![Flask](https://img.shields.io/badge/Flask-3.x-green)
![scikit-learn](https://img.shields.io/badge/scikit--learn-1.3+-orange)

## What this project does

- Trains a **Random Forest** model on the Telco Customer Churn dataset
- Serves predictions through a simple **Flask web app**
- Shows a **churn probability score** and plain-English result
- Includes a polished frontend for demos and portfolios

## Project structure

```
churn prediction/
├── app.py              # Flask web server
├── train_model.py      # Train and save the ML model
├── eda.py              # Quick data exploration script
├── customer_churn.csv  # Dataset
├── model/              # Saved model files (generated)
├── templates/          # HTML templates
├── static/             # CSS and JavaScript
└── requirements.txt    # Python dependencies
```

## Quick start

### 1. Create a virtual environment

```bash
python3 -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Train the model

```bash
python train_model.py
```

This creates:
- `model/churn_model.pkl`
- `model/encoders.pkl`
- `model/metadata.pkl`

### 4. Run the web app

```bash
python app.py
```

Open [http://127.0.0.1:5000](http://127.0.0.1:5000) in your browser.

Click **Load Sample Customer** to try a pre-filled example, then hit **Predict Churn Risk**.

## How it works

1. **Training** (`train_model.py`): Reads the CSV, encodes categorical columns, trains a Random Forest classifier, and saves the model.
2. **Prediction** (`app.py`): Takes form input, encodes it the same way as training, and returns churn vs. stay with a probability score.
3. **Frontend** (`templates/`, `static/`): A dashboard-style UI with grouped form sections and a result panel.

## Skills you'll learn

- Loading and cleaning tabular data with pandas
- Training a classification model with scikit-learn
- Saving and loading models with joblib
- Building a simple ML API with Flask
- Connecting a Python backend to an HTML frontend

## Dataset

Uses the [Telco Customer Churn](https://www.kaggle.com/datasets/blastchar/telco-customer-churn) dataset (included as `customer_churn.csv`).

## Next steps (optional)

- Add a batch upload page (CSV → predictions)
- Deploy to [Render](https://render.com) or [Railway](https://railway.app)
- Swap Random Forest for Logistic Regression and compare accuracy
- Add SHAP or feature importance to explain predictions

## License

Educational / portfolio use. Dataset belongs to its original source.
