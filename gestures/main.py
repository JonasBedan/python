import mediapipe as mp
import numpy as np
import cv2

cam = cv2.VideoCapture(0)

mp_drawing = mp.solutions.drawing_utils
mp_hand = mp.solutions.hands
hand = mp_hand.Hands()


while True:
    success, frame = cam.read()
    if success:
        RgbFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        result = hand.process(frame)
        if result.multi_hand_landmarks:
            for hand_landmarks in result.multi_hand_landmarks:
                print(hand_landmarks)
                mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hand.HAND_CONNECTIONS)
        cv2.imshow("window",frame)
        if cv2.waitKey(5) == ord ('q'):
            break