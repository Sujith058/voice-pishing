import joblib
from utils.feature_extraction import extract_features

def predict_audio(file_path):
    try:
        model = joblib.load("model/model.pkl")
    except FileNotFoundError:
        return "Model not trained yet"

    features = extract_features(file_path)
    prediction = model.predict([features])[0]
    return "Phishing" if prediction == 1 else "Genuine"
