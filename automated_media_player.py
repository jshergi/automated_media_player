import os
import cv2
import mediapipe as mp
import pyautogui
import time
import webbrowser
import sys
import pygame

def blitlines(surf, text, renderer, color, x, y):
    h = renderer.get_height()
    lines = text.split('\n')
    for i, ll in enumerate(lines):
        txt_surface = renderer.render(ll, True, color)
        surf.blit(txt_surface, (x, y+(i*h)))


background_colour = (0, 0, 0)
textcolor = (255, 255, 255)

multitext = "                  OPTIONS MENU\n\n1 Finger: Forward (5s)\n2 Fingers: Reverse (5s)" \
            "\n3 Fingers: Full Screen / Normal Screen\n4 Fingers: Mute / Unmute\n5 Fingers & Thumb: " \
            "Pause / Resume\n\nFist: Captions / No Captions"

pygame.init()
screen = pygame.display.set_mode((700, 350))
userfont = pygame.font.Font(None, 40)

screen.fill(background_colour)
blitlines(screen, multitext, userfont, textcolor, 100, 100)

pygame.display.flip()



def count_fingers(lst):
    cnt = 0

    thresh = (lst.landmark[0].y*100-lst.landmark[9].y*100)/2

    if(lst.landmark[5].y*100-lst.landmark[8].y*100) > thresh:
        cnt += 1

    if (lst.landmark[9].y * 100 - lst.landmark[12].y * 100) > thresh:
        cnt += 1

    if (lst.landmark[13].y * 100 - lst.landmark[16].y * 100) > thresh:
        cnt += 1

    if (lst.landmark[17].y * 100 - lst.landmark[20].y * 100) > thresh:
        cnt += 1

    if (lst.landmark[5].x * 100 - lst.landmark[4].x * 100) > 5:
        cnt += 1

    return cnt
# sys.path.append('/usr/local/lib/python3/site-packages')
cap = cv2.VideoCapture(0)

drawing = mp.solutions.drawing_utils
hands = mp.solutions.hands
hand_obj = hands.Hands(max_num_hands=1)

start_init = False
prev = -1

webbrowser.open_new('https://www.youtube.com/watch?v=YRhxdVk_sIs')


while True:
    end_time = time.time()
    _, frm = cap.read()
    frm = cv2.flip(frm,1)

    res = hand_obj.process(cv2.cvtColor(frm, cv2.COLOR_BGR2RGB))
    if res.multi_hand_landmarks:

        hand_keyPoints = res.multi_hand_landmarks[0]

        cnt = count_fingers(hand_keyPoints)
        if not (prev==cnt):
            if not (start_init):
                start_time = time.time()
                start_init = True

            elif (end_time-start_time)>0.2:
                if (cnt == 0):
                    pyautogui.press("c")
                if(cnt ==1 ):
                    pyautogui.press("right")
                elif(cnt == 2):
                    pyautogui.press("left")
                elif (cnt == 3):
                    pyautogui.press("f")
                elif (cnt == 4):
                    pyautogui.press("m")
                elif (cnt == 5):
                    pyautogui.press("space")
                prev = cnt
                start_init = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()





        drawing.draw_landmarks(frm, hand_keyPoints, hands.HAND_CONNECTIONS)

    cv2.imshow("window", frm)

    if cv2.waitKey(1) == 27: # escape key
        cv2.destroyAllWindows()
        cap.release()
        os.system("killall -9 'Safari'")
        break

