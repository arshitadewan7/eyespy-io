from fer import FER
import matplotlib.pyplot as plt

# Take a snapshot at the end
cap = cv2.VideoCapture(0)
ret, frame = cap.read()
cap.release()

if ret:
    detector = FER(mtcnn=True)
    result = detector.detect_emotions(frame)
    if result:
        emotion_scores = result[0]['emotions']
        dominant_emotion = max(emotion_scores, key=emotion_scores.get)
        print(f"\nYour final emotion during this session: {dominant_emotion.upper()}")
    else:
        print("\nNo face detected for emotion analysis.")
