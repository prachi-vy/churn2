const SAMPLE_CUSTOMER = {
    gender: "Female",
    SeniorCitizen: "0",
    Partner: "Yes",
    Dependents: "No",
    tenure: "12",
    PhoneService: "Yes",
    MultipleLines: "No",
    InternetService: "Fiber optic",
    OnlineSecurity: "No",
    OnlineBackup: "No",
    DeviceProtection: "No",
    TechSupport: "No",
    StreamingTV: "Yes",
    StreamingMovies: "Yes",
    Contract: "Month-to-month",
    PaperlessBilling: "Yes",
    PaymentMethod: "Electronic check",
    MonthlyCharges: "89.10",
    TotalCharges: "1049.65",
};

function fillSampleData() {
    const form = document.getElementById("churn-form");
    if (!form) return;

    Object.entries(SAMPLE_CUSTOMER).forEach(([name, value]) => {
        const field = form.elements[name];
        if (field) field.value = value;
    });
}

function setLoadingState(isLoading) {
    const button = document.getElementById("predict-btn");
    if (!button) return;

    button.disabled = isLoading;
    button.textContent = isLoading ? "Analyzing..." : "Predict Churn Risk";
}

document.addEventListener("DOMContentLoaded", () => {
    const form = document.getElementById("churn-form");
    const sampleButton = document.getElementById("sample-btn");

    if (sampleButton) {
        sampleButton.addEventListener("click", fillSampleData);
    }

    if (form) {
        form.addEventListener("submit", () => setLoadingState(true));
    }
});
