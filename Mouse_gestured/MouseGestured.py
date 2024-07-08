import cv2
import numpy as np
import HandTrackingModule as htm
import time
import pyautogui

# Webcam resolution
vCam, hCam = 640, 480
cap = cv2.VideoCapture(0)
cap.set(3, vCam)
cap.set(4, hCam)
smoothening = 3
preX, preY = 0, 0
curX, curY = 0, 0
frameR = 120
# Screen resolution
wScr, hScr = 1366, 768

pTime = 0
detector = htm.handDetector(maxHands=1)

while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)
    img = detector.findHands(img)
    lmList, bbox = detector.findPosition(img)
    if len(lmList) != 0:
        x1, y1 = lmList[8][1:]
        x2, y2 = lmList[12][1:]
        # print(x1, y1, x2, y2)
        fingers = detector.fingersUp()
        cv2.rectangle(img, (frameR, frameR), (vCam - frameR, hCam - frameR), (0, 0, 0), 2)
        # print(fingers)
        if fingers[1] == 1 and fingers[2] == 0:
            # Map hand coordinates to screen coordinates

            x3 = np.interp(x1, (frameR, vCam - frameR), (0, wScr))
            y3 = np.interp(y1, (frameR, hCam - frameR), (0, hScr))

            curX = preX + (x3 - preX) / smoothening
            curY = preY + (y3 - preY) / smoothening

            # Move the mouse
            pyautogui.moveTo(curX, curY)
            cv2.circle(img, (x1, y1), 15, (255, 0, 255), cv2.FILLED)
            preY, preX = curY, curX

        if fingers[1] == 1 and fingers[2] == 1:
            length, img, lineInfo = detector.findDistance(8, 12, img)
            if length < 39:
                cv2.circle(img, (lineInfo[4], lineInfo[5]), 15, (0, 230, 255), cv2.FILLED)
                pyautogui.click()

        if fingers[1] == 1 and fingers[0] == 1:
            # Calculate the length between the thumb tip (4) and the center of the hand (9)
            length, img, lineInfo = detector.findDistance(4, 8, img)

            # print(length)
            if length > 100:
                pyautogui.vscroll(+10)  # Scroll up
                cv2.circle(img, (lineInfo[4], lineInfo[5]), 15, (0, 230, 255), cv2.FILLED)

            if length < 100:
                pyautogui.vscroll(-10)  # Scroll down
                cv2.circle(img, (lineInfo[4], lineInfo[5]), 15, (0, 230, 255), cv2.FILLED)

            

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    cv2.putText(img, str(int(fps)), (20, 50), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)
    cv2.imshow("Image", img)
    cv2.waitKey(1)

cap.release()
cv2.destroyAllWindows()
