from flask import Flask, render_template, request
import os
from datetime import datetime
from model.predict_audio import predict_audio

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

# ===== Helper Functions =====
def count_dataset_files():
    phishing_dir = "dataset/phishing"
    genuine_dir = "dataset/genuine"
    phishing_count = len(os.listdir(phishing_dir)) if os.path.exists(phishing_dir) else 0
    genuine_count = len(os.listdir(genuine_dir)) if os.path.exists(genuine_dir) else 0
    return phishing_count + genuine_count

def get_model_status():
    model_path = "model/model.pkl"
    return "✅ Trained" if os.path.exists(model_path) else "❌ Not Trained"

def get_model_accuracy():
    acc_path = "model/accuracy.txt"
    if os.path.exists(acc_path):
        with open(acc_path, "r") as f:
            try:
                return float(f.read().strip())
            except ValueError:
                return None
    return None

def get_last_trained_time():
    model_path = "model/model.pkl"
    if os.path.exists(model_path):
        ts = os.path.getmtime(model_path)
        return datetime.fromtimestamp(ts).strftime("%Y-%m-%d %H:%M:%S")
    return "—"

recent_predictions = []

# ===== Routes =====
@app.route('/')
def index():
    num_samples = count_dataset_files()
    model_status = get_model_status()
    model_accuracy = get_model_accuracy()
    trained_time = get_last_trained_time()

    return render_template(
        "index.html",
        num_samples=num_samples,
        model_status=model_status,
        model_accuracy=model_accuracy,
        model_trained_time=trained_time,
        recent_predictions=recent_predictions
    )

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        if 'file' not in request.files:
            return render_template('upload.html', error="No file selected")

        file = request.files['file']
        if file.filename == '':
            return render_template('upload.html', error="Empty filename")

        filename = file.filename
        save_path = os.path.join(app.config["UPLOAD_FOLDER"], filename)
        file.save(save_path)

        result = predict_audio(save_path)
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        recent_predictions.insert(0, {"file": filename, "result": result, "time": now})

        if len(recent_predictions) > 10:
            recent_predictions.pop()

        return render_template('result.html', result=result, filename=filename)

    return render_template('upload.html')

@app.route('/retrain', methods=['POST'])
def retrain():
    from model.train_model import train
    acc = train()
    with open("model/accuracy.txt", "w") as f:
        f.write(str(acc))
    return ("", 204)

@app.route('/clear_dataset', methods=['POST'])
def clear_dataset():
    import shutil
    if os.path.exists("dataset/phishing"):
        shutil.rmtree("dataset/phishing")
    if os.path.exists("dataset/genuine"):
        shutil.rmtree("dataset/genuine")
    os.makedirs("dataset/phishing", exist_ok=True)
    os.makedirs("dataset/genuine", exist_ok=True)
    return ("", 204)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
