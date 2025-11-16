# 🎙️ VishingAI — Voice Phishing Detection Using AI

VishingAI is a machine learning–powered web application that detects **voice phishing (vishing)** and **deepfake scam calls** by analyzing speech stress markers, tone variations, and repeated scam-like phrases using MFCC and Chroma audio features.

This project provides a **secure AI-based detection dashboard**, a **clean dark-themed UI**, and **automated dataset generation** for continuous model improvement.

---

## 🌐 Project Overview

| Functionality | Description |
|---------------|--------------|
| 🎧 **Audio Upload** | Upload or record `.wav` / `.mp3` samples for phishing detection |
| 🧠 **AI Analysis** | Model extracts MFCC + Chroma features and classifies audio |
| 📈 **Dashboard** | View dataset size, accuracy, training history, and predictions |
| 🔁 **Retraining** | Easily retrain the model with new samples |
| ⚙️ **Dataset Tools** | Auto-generate new audio samples or clear existing datasets |

---

## 🧠 Tech Stack

| Layer | Technologies Used |
|-------|--------------------|
| **Frontend** | HTML5, CSS3, JavaScript (Neon Dark UI) |
| **Backend** | Flask 3.0.0 (Python) |
| **AI/ML Engine** | scikit-learn, librosa, numpy, pandas, joblib |
| **Dataset Generator** | gTTS (Google Text-to-Speech) |
| **Environment** | Python 3.12 (VS Code / GitHub Codespaces) |

---

## ⚙️ How to Run

```bash
# 1️⃣ Clone the repository

# 2️⃣ Create and activate virtual environment
python3 -m venv .venv
source .venv/bin/activate   # (Linux/Mac)
# OR
.venv\Scripts\activate      # (Windows)

# 3️⃣ Install dependencies
pip install -r requirements.txt

# 4️⃣ Generate dataset
python generate_dataset.py

# 5️⃣ Train model
python -m model.train_model

# 6️⃣ Launch app
python app.py
Visit → http://127.0.0.1:5000 to access the dashboard.

```

## 🧠 System Architecture

The VishingAI project follows a **layered architecture** connecting the web interface, Flask API, ML model, and audio dataset generation modules.  
This ensures scalability, transparency, and ease of retraining for accurate phishing detection.

---

### 🔹 Architecture Layers

| Layer | Module / Folder | Description |
|-------|------------------|-------------|
| 🎨 **Frontend (Presentation Layer)** | `/templates`, `/static` | HTML, CSS, and JS-based user interface for Dashboard, Upload, and Result pages. |
| ⚙️ **Application Layer (Flask API)** | `app.py` | Handles routes like `/`, `/upload`, and `/retrain`. Connects UI with backend logic. |
| 🧠 **Machine Learning Layer** | `model/train_model.py`, `model/predict_audio.py` | Trains and loads a RandomForestClassifier model. Performs prediction on extracted features. |
| 🎧 **Feature Extraction Layer** | `utils/feature_extraction.py` | Uses `librosa` to extract MFCC, Chroma, and Spectral Contrast features from audio. |
| 💾 **Dataset Layer** | `generate_dataset.py`, `/dataset` | Manages phishing and genuine voice samples auto-generated using `gTTS`. |

---

### 🔹 Data Flow

1️⃣ **User Interaction** — User uploads `.wav` or `.mp3` via the web UI.  
2️⃣ **Flask Processing** — The file is stored in `/uploads` and passed to the feature extraction module.  
3️⃣ **Feature Extraction** — `librosa` converts audio into numerical MFCC & Chroma features.  
4️⃣ **ML Classification** — RandomForest model predicts if the audio is *Phishing* ⚠️ or *Genuine* ✅.  
5️⃣ **Result Visualization** — Flask renders the `result.html` page with the final classification.  
6️⃣ **Model Management** — Dashboard options allow retraining or clearing dataset for new experiments.

---

### 🔹 High-Level System Diagram

      ┌──────────────────────────────┐
      │        User Interface        │
      │  (Upload | Dashboard | UI)   │
      │  HTML, CSS, JS Frontend      │
      └──────────────┬───────────────┘
                     │
                     ▼
      ┌──────────────────────────────┐
      │          Flask App           │
      │ (app.py Routes & Logic)      │
      │  /upload  /result  /retrain  │
      └──────────────┬───────────────┘
                     │
                     ▼
      ┌──────────────────────────────┐
      │     Feature Extraction       │
      │ (librosa + numpy + utils)    │
      │   → MFCC, Chroma, Contrast   │
      └──────────────┬───────────────┘
                     │
                     ▼
      ┌──────────────────────────────┐
      │     ML Model (RandomForest)  │
      │  train_model.py | predict.py │
      │   Model.pkl via Joblib       │
      └──────────────┬───────────────┘
                     │
                     ▼
      ┌──────────────────────────────┐
      │     Dataset (Audio Files)    │
      │ phishing/  genuine/ uploads/ │
      │ Auto-generated via gTTS      │
      └──────────────────────────────┘




## 📊 Dashboard Preview

Page	Description

🖥️ Dashboard	Displays dataset size, model accuracy, and predictions

🎧 Upload Page	Drag-and-drop file upload for real-time detection

🧾 Result Page	Displays “✅ Genuine” or “⚠️ Phishing” result clearly



## 👩‍💻 Contributors
Submitted by:

Siva Prasanth Tippisetti — (000805280)

Natraj Vemula — (000798446)

Sujith Yamsani — (000797860)
