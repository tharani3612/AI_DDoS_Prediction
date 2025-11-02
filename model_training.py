import os
import joblib
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
from data_preprocessing import preprocess_data

MODEL_PATH = "model/ddos_model.pkl"

def train_model():
    X, y = preprocess_data()

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = RandomForestClassifier(n_estimators=150, random_state=42)
    model.fit(X_train, y_train)

    os.makedirs("model", exist_ok=True)
    joblib.dump(model, MODEL_PATH)
    print(f"✅ Model trained & saved at {MODEL_PATH}")

    y_pred = model.predict(X_test)
    print(f"🎯 Accuracy: {accuracy_score(y_test, y_pred):.2f}")
    print("📊 Classification Report:\n", classification_report(y_test, y_pred))

if __name__ == "__main__":
    train_model()
