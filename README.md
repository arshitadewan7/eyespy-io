# EyeSpy.io 

**Your eyes can't lie.**  
EyeSpy.io is a gaze tracking tool that reveals where your attention really goes. Whether it's testing loyalty, analyzing focus, or visualizing subconscious attention, your gaze tells the truth.

---

## 🚀 Features
- Real-time gaze tracking via webcam
- Heatmap visualization of gaze points
- Loyalty Test Mode (Left vs. Right attention analysis)
- Emotion detection using FER
- Streamlit interface with interactive heatmaps
- Downloadable visual reports

---

## 🛠️ Tech Stack
- Python 3.11
- OpenCV
- MediaPipe (Face Mesh)
- FER (Facial Emotion Recognition)
- Matplotlib
- Streamlit
- NumPy

---

## 📂 Project Structure
```plaintext
eyespy-io/
├── app/
│   ├── gaze_tracker.py
│   ├── loyalty_test.py
│   ├── streamlit_app.py
├── assets/
│   └── gaze_heatmap.png
├── requirements.txt
├── .gitignore
└── README.md

⚙️ How to Run

1️⃣ Create virtual environment and activate:

python -m venv venv
source venv/bin/activate  # Mac/Linux
# .\venv\Scripts\activate  # Windows

2️⃣ Install dependencies:

pip install -r requirements.txt

3️⃣ Run your files:

# Run Gaze Tracker (ESC to exit)
python app/gaze_tracker.py

# Run Loyalty Test (Emotion Detection)
python app/loyalty_test.py

# Run Streamlit App
streamlit run app/streamlit_app.py

📊 Use Cases

Loyalty tests (Who catches your eye more?)
Gaze heatmap for attention analysis
Fun social challenges
Psychology & UX research demos