import pandas as pd
from sklearn.ensemble import IsolationForest
import joblib

# -----------------------------
# 1️⃣ Load Dataset
# -----------------------------
df = pd.read_csv("server_metrics.csv")

print("Dataset Loaded Successfully\n")

# Check dataset structure
print("Columns in dataset:", df.columns)
print("\nFirst 5 rows:\n", df.head())


# -----------------------------
# 2️⃣ Feature Selection
# -----------------------------
# Change this if your dataset has different column names
feature_columns = ["cpu", "ram", "network", "process_count"]

X = df[feature_columns]


# -----------------------------
# 3️⃣ Train Isolation Forest
# -----------------------------
model = IsolationForest(
    n_estimators=100,
    contamination=0.05,
    random_state=42
)

model.fit(X)

print("\nModel Training Completed")


# -----------------------------
# 4️⃣ Save Model + Feature List
# -----------------------------
joblib.dump(model, "anomaly_model.pkl")
joblib.dump(feature_columns, "feature_columns.pkl")

print("Model Saved Successfully")


# -----------------------------
# 5️⃣ Predict Anomalies
# -----------------------------
predictions = model.predict(X)

df["anomaly"] = predictions

print("\nAnomaly Distribution:")
print(df["anomaly"].value_counts())


# -----------------------------
# 6️⃣ Risk Score Calculation
# -----------------------------
scores = model.decision_function(X)

df["risk_score"] = scores


# -----------------------------
# 7️⃣ Risk Label Logic
# -----------------------------
def risk_label(score):
    if score < -0.1:
        return "High"
    elif score < 0:
        return "Medium"
    else:
        return "Low"


df["risk_label"] = df["risk_score"].apply(risk_label)


# -----------------------------
# 8️⃣ Save Results
# -----------------------------
df.to_csv("anomaly_results.csv", index=False)

print("\nRisk Analysis Completed")
print("\nSample Output:\n")

print(df.head())


print("\nResults saved to: anomaly_results.csv")