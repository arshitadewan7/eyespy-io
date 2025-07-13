import cv2
import mediapipe as mp
import matplotlib.pyplot as plt

gaze_points = []

mp_face_mesh = mp.solutions.face_mesh.FaceMesh(refine_landmarks=True)
cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = mp_face_mesh.process(frame_rgb)

    ih, iw, _ = frame.shape

    if results.multi_face_landmarks:
        for face_landmarks in results.multi_face_landmarks:
            # Right eye approximate center: landmarks 33-133
            xs = []
            ys = []
            for id, lm in enumerate(face_landmarks.landmark):
                x, y = int(lm.x * iw), int(lm.y * ih)
                if 33 <= id <= 133:
                    xs.append(x)
                    ys.append(y)

            if xs and ys:
                center_x = int(sum(xs) / len(xs))
                center_y = int(sum(ys) / len(ys))
                gaze_points.append((center_x, center_y))
                cv2.circle(frame, (center_x, center_y), 4, (0, 0, 255), -1)  # Red dot for eye center

    cv2.imshow('EyeSpy - Gaze Tracker', frame)
    if cv2.waitKey(1) & 0xFF == 27:  # ESC to exit
        break

cap.release()
cv2.destroyAllWindows()

# Plotting Heatmap of gaze points
if gaze_points:
    xs, ys = zip(*gaze_points)
    plt.figure(figsize=(10, 6))
    plt.hist2d(xs, ys, bins=50, cmap='hot')
    plt.colorbar()
    plt.title('EyeSpy.io - Gaze Heatmap')
    plt.gca().invert_yaxis()
    plt.show()
