import os
import numpy as np
import librosa
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib
from utils.feature_extraction import extract_features

def train():
    print("📂 Loading dataset...")
    phishing_dir = "dataset/phishing"
    genuine_dir = "dataset/genuine"
    X, y = [], []

    if not os.path.exists(phishing_dir) or not os.path.exists(genuine_dir):
        print("⚠️ Missing dataset folders.")
        return 0.0

    for label, folder in [(1, phishing_dir), (0, genuine_dir)]:
        for file in os.listdir(folder):
            if file.endswith(".wav") or file.endswith(".mp3"):
                path = os.path.join(folder, file)
                try:
                    features = extract_features(path)
                    X.append(features)
                    y.append(label)
                except Exception as e:
                    print(f"❌ Error: {file} — {e}")

    if len(X) == 0:
        print("⚠️ No samples found.")
        return 0.0

    X = np.array(X)
    y = np.array(y)
    print(f"✅ Loaded {len(X)} samples.")

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    preds = model.predict(X_test)
    acc = round(accuracy_score(y_test, preds) * 100, 2)
    print(f"🎯 Model accuracy: {acc}%")

    os.makedirs("model", exist_ok=True)
    joblib.dump(model, "model/model.pkl")
    print("💾 Model saved to model/model.pkl")

    with open("model/accuracy.txt", "w") as f:
        f.write(str(acc))

    return acc

if __name__ == "__main__":
    train()
