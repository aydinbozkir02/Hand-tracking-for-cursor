import cv2
import mediapipe as mp
import pyautogui
import math
import time

# Kamera başlat ve çözünürlüğü düşür
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

mp_hands = mp.solutions.hands
hands = mp_hands.Hands()
mp_draw = mp.solutions.drawing_utils

# ekran boyutları
screen_width, screen_height = pyautogui.size()

prev_screen_x = screen_width // 2
prev_screen_y = screen_height // 2

# sürekli tıklamamak için süre takip ediyoruz
last_click_time = 0
click_delay = 0.2  

action_text = ""

while True:
    success, frame = cap.read()
    if not success: 
        break

    frame = cv2.flip(frame, 1)  # aynalama
    h, w, c = frame.shape      # ölçüler

    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)  # BGR -> RGB
    result = hands.process(rgb_frame)

    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:
            # noktalar
            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            # kütüphanenin indeksleri
            isaret_parmak = hand_landmarks.landmark[8]  
            bas_parmak = hand_landmarks.landmark[4]
            orta_parmak = hand_landmarks.landmark[12]
            avuc = hand_landmarks.landmark[0]

            isaret_x = int(isaret_parmak.x * w)  #nokta konumları
            isaret_y = int(isaret_parmak.y * h)
            bas_x = int(bas_parmak.x * w)
            bas_y = int(bas_parmak.y * h)
            orta_x = int(orta_parmak.x * w)
            orta_y = int(orta_parmak.y * h)
            avuc_x = int(avuc.x * w)
            avuc_y = int(avuc.y * h)

            # mesafe hesaplama
            left_click_distance = math.hypot(isaret_x - bas_x, isaret_y - bas_y)
            right_click_distance = math.hypot(isaret_x - orta_x, isaret_y - orta_y)
            in_hand_distance = math.hypot(orta_x - avuc_x, orta_y - avuc_y)

            # ekrana uyarlama ve yumuşatma
            smooth_factor = 0.7
            screen_x = int(isaret_x * screen_width / w)
            screen_y = int(isaret_y * screen_height / h)

            smoothed_x = int(smooth_factor * prev_screen_x + (1 - smooth_factor) * screen_x)
            smoothed_y = int(smooth_factor * prev_screen_y + (1 - smooth_factor) * screen_y)

            prev_screen_x, prev_screen_y = smoothed_x, smoothed_y
            pyautogui.moveTo(smoothed_x, smoothed_y)  # fareyi hareket ettirme

            # sürekli tıklamamak için, sol tık
            current_time = time.time()
            if left_click_distance < 25 and (current_time - last_click_time) > click_delay:
                pyautogui.click()
                last_click_time = current_time
                action_text = "Sol Tik"
            
            # sağ tık 
            current_time = time.time()
            if right_click_distance < 15 and (current_time - last_click_time) > click_delay:
                pyautogui.rightClick()
                last_click_time = current_time
                action_text = "Sag Tik"

            #ekran kapama
            current_time = time.time()
            if in_hand_distance < 90 and (current_time - last_click_time) > click_delay:
                pyautogui.press('q')
                last_click_time = current_time
                action_text = "q"
                


    if action_text:
        cv2.putText(frame, action_text, (50,50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255,0), 2)
    
    cv2.imshow("El Takibi", frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
