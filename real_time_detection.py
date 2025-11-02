import joblib
import pandas as pd

SCALER_PATH = "model/scaler.pkl"
MODEL_PATH = "model/ddos_model.pkl"

def detect_ddos(features):
    scaler = joblib.load(SCALER_PATH)
    model = joblib.load(MODEL_PATH)

    columns = ["packets_per_second", "bytes_per_second", "avg_packet_size",
               "flow_duration", "unique_src_ips", "unique_dst_ports"]

    df = pd.DataFrame([features], columns=columns)
    df_scaled = scaler.transform(df)
    pred = model.predict(df_scaled)[0]

    if pred == 1:
        return "⚠️ DDoS Attack Detected"
    else:
        return "✅ Normal Traffic"

if __name__ == "__main__":
    test_sample = [1500, 1200000, 450, 2.5, 120, 5]
    print(detect_ddos(test_sample))
