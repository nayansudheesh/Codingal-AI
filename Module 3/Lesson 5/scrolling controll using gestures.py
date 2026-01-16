import cv2 , time , pyautogui

import mediapipe as mp

mp_hands = mp.solutions.hands

hands = mp_hands.Hands(max_num_hands = 1, min_detection_confidence = 0.7)

hands_drawing = mp.solutions.drawing_utils

SCROLL_SPEED = 300

SCROLL_DELAY = 1

CAM_WIDTH , CAM_HEIGHT = 640 , 480


def detect_gesture(landmarks , handedness):

    fingers = []

    tips = [mp_hands.HandLandmark.INDEX_FINGER_TIP , mp_hands.HandLandmark.MIDDLE_FINGER_TIP ,mp_hands.HandLandmark.RING_FINGER_TIP , mp_hands.HandLandmark.PINKY_TIP ]

    for tip in tips:
        if landmarks.landmark[tip].y < landmarks.landmark[tip-2].y:
            fingers.append(1)
        
        thumb_tip = landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]
        thumb_ip = landmarks.landmark[mp_hands.HandLandmark.THUMB_IP]

        if (handedness == "Right" and thumb_tip.x > thumb_ip.x) or (handedness == "Left" and thumb_tip.x < thumb_ip.x):

            fingers.append(1)

            return "Scroll up" if sum(fingers) == 5 else "scroll down" if len(fingers) == 0 else "None"
        
cap = cv2.VideoCapture(0)

cap.set(3 , CAM_WIDTH)

cap.set(4, CAM_HEIGHT)

last_scroll = p_time = 0

print("Gesture controll active \n open palm : scroll up \n fist: scroll down \n press q to exit")

while cap.isOpened():
    sucess , img = cap.read()

    if not sucess: break


    img = cv2.flip(cv2.cvtColor(img , cv2.COLOR_BGR2RGB))   

    results = hands.process(img)     

    gesture , handedness = "None" , "Unknown"

    if results.multi_hand_landmarks:
        for hands , jandedness_info in zip(results.multi_hand_landmarks , results.multi_handedness):

            gesture = detect_gesture(hands , handedness)

            mp.drawing.draw_landmarks(img , hands, mp_hands.HAND_CONNECTIONS)

            if (time.time() - last_scroll) > SCROLL_DELAY:

                if gesture == "Scroll up": pyautogui.scroll(SCROLL_SPEED)
                if gesture == "scroll down": pyautogui.scroll(-SCROLL_SPEED)


    fps = 1/(time.time()-p_time) if (time.time()-p_time) > 0 else 0

    p_time = time.time()

    cv2.putText(img , f"FPS: {int(fps)} | Hand: {handedness} | gesture: {gesture}" , (10 , 30), cv2.FONT_HERSHEY_SIMPLEX , 0.7 , (255 , 0 , 0 ) , 2)

    cv2.imshow("Gesture controll " , cv2.cvtColor(img , cv2.COLOR_BGR2RGB))
    if cv2.waitKey(1) == ord("q"): break

cap.release()
cv2.destroyAllWindows()

