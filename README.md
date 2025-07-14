# 👁️ EyeSpy.io - Loyalty Test Mode

A fun, lightweight gaze-tracking app built with **Streamlit** and **OpenCV** to test where your attention goes during conversations — are you more loyal to Person A or Person B? 😉

---

## 🚀 Features
- Live webcam gaze tracking (via `mediapipe`)
- Generates a heatmap of your eye movement
- Analyzes left vs. right attention bias
- Downloadable gaze heatmap image
- Fast, lightweight, and runs locally

---

## 🛠️ Tech Stack
- Python 3.11
- Streamlit
- OpenCV
- MediaPipe
- Matplotlib
- NumPy
- FER

---

## ⚙️ Steps to Run

### 1️⃣ Create virtual environment and activate:
\`\`\`bash
python -m venv venv
source venv/bin/activate  # Mac/Linux
# .\venv\Scripts\activate  # Windows
\`\`\`

### 2️⃣ Install dependencies:
\`\`\`bash
pip install -r requirements.txt
\`\`\`

### 3️⃣ Run your files:
\`\`\`bash
# Run Gaze Tracker (ESC to exit)
python app/gaze_tracker.py

# Run Loyalty Test (Emotion Detection)
python app/loyalty_test.py

# Run Streamlit App
streamlit run app/streamlit_app.py
\`\`\`

---

## 📂 Project Structure
\`\`\`bash
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
\`\`\`

---

## 📝 License
MIT License
EOF
