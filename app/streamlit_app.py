import streamlit as st
import cv2
import mediapipe as mp
import numpy as np
import matplotlib.pyplot as plt
import os

# Streamlit UI
st.title("EyeSpy.io - Loyalty Test Mode 👀")
st.markdown("Move your eyes left ↔️ right. We'll show where your gaze stayed most.")
run = st.button("Start Loyalty Test")

if run:
    mp_face_mesh = mp.solutions.face_mesh.FaceMesh(refine_landmarks=True)
    cap = cv2.VideoCapture(0)
    gaze_points = []

    stframe = st.empty()

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        ih, iw, _ = frame.shape
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = mp_face_mesh.process(frame_rgb)

        if results.multi_face_landmarks:
            for face_landmarks in results.multi_face_landmarks:
                xs = []
                ys = []
                for id, lm in enumerate(face_landmarks.landmark):
                    x, y = int(lm.x * iw), int(lm.y * ih)
                    if 33 <= id <= 133:
                        xs.append(x)
                        ys.append(y)

                if xs:
                    center_x = int(sum(xs) / len(xs))
                    center_y = int(sum(ys) / len(ys))
                    gaze_points.append((center_x, center_y))
                    cv2.circle(frame, (center_x, center_y), 5, (0, 0, 255), -1)

        frame_bgr = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
        stframe.image(frame_bgr, channels="BGR")

        if len(gaze_points) > 300:  # Run approx 10 seconds
            break

    cap.release()
    st.success("Loyalty test complete! Generating heatmap...")

    xs, ys = zip(*gaze_points)
    os.makedirs("assets", exist_ok=True)
    heatmap_path = os.path.join("assets", "gaze_heatmap.png")

    plt.figure(figsize=(10, 5))
    plt.hist2d(xs, ys, bins=50, cmap='hot')
    plt.colorbar()
    plt.gca().invert_yaxis()
    plt.title("EyeSpy.io - Gaze Heatmap")
    plt.savefig(heatmap_path)
    st.image(heatmap_path, caption="Your Gaze Heatmap", use_container_width=True)

    left_side = [x for x, _ in gaze_points if x < iw / 2]
    right_side = [x for x, _ in gaze_points if x >= iw / 2]
    left_pct = len(left_side) / len(gaze_points) * 100
    right_pct = len(right_side) / len(gaze_points) * 100

    if left_pct > right_pct:
        result = f"You looked LEFT {left_pct:.1f}% of the time! Loyalty to Person A confirmed. 😉"
    else:
        result = f"You looked RIGHT {right_pct:.1f}% of the time! Loyalty to Person B confirmed. 😄"

    st.markdown(f"### {result}")

    with open(heatmap_path, "rb") as file:
        btn = st.download_button(
            label="Download Heatmap Image",
            data=file,
            file_name="gaze_heatmap.png",
            mime="image/png"
        )
