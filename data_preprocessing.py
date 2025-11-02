import pandas as pd
import os
import joblib
from sklearn.preprocessing import StandardScaler

DATA_PATH = "dataset/ddos_traffic.csv"
SCALER_PATH = "model/scaler.pkl"

def preprocess_data():
    df = pd.read_csv(DATA_PATH)
    df = df.dropna()

    X = df.drop("Label", axis=1)
    y = df["Label"]

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    os.makedirs("model", exist_ok=True)
    joblib.dump(scaler, SCALER_PATH)
    print(f"✅ Data preprocessed & scaler saved at {SCALER_PATH}")

    return X_scaled, y

if __name__ == "__main__":
    preprocess_data()
