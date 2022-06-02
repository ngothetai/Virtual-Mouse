import mediapipe as mp
import cv2

tracking_hand = mp.solutions.hands.Hands(mode=False, max_hands=2, detection_confidence=0.5)
cam = cv2.VideoCapture(0)

while True:
    _, frame = cam.read()
    tracking_hand.process_image(frame)
    if tracking_hand.multi_hand_landmarks:
        