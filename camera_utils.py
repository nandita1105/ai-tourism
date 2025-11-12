"""
camera_utils.py

Simple helper to capture a single frame from the Jetson camera.
"""

import cv2
import time


def capture_frame(device_index: int = 0, out_path: str = "frame.jpg") -> str:
    cap = cv2.VideoCapture(device_index)
    if not cap.isOpened():
        raise RuntimeError(f"Could not open camera at index {device_index}")

    # Give the camera a moment to adjust exposure/focus
    time.sleep(0.5)

    ret, frame = cap.read()
    cap.release()

    if not ret:
        raise RuntimeError("Failed to capture frame from camera")

    cv2.imwrite(out_path, frame)
    return out_path
