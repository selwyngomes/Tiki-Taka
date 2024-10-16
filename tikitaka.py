import cv2
import cvzone
from cvzone.HandTrackingModule import HandDetector
import numpy as np

cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)

imgGameStart = cv2.imread("Resources/gameStart.png")
imgGameStart1 = cv2.imread("Resources/gameStart1.png")
imgBackground = cv2.imread("Resources/Background.png")
imgGameOver = cv2.imread("Resources/gameOver.png")
imgBall = cv2.imread("Resources/Ball.png", cv2.IMREAD_UNCHANGED)
imgBat1 = cv2.imread("Resources/bat1.png", cv2.IMREAD_UNCHANGED)
imgBat2 = cv2.imread("Resources/bat2.png", cv2.IMREAD_UNCHANGED)


detector = HandDetector(detectionCon=0.8, maxHands=2)

ballPos = [640, 300]
speed = 15

speedX = speed
speedY = speed
gameOver = False
score = [0, 0]
started = True
while True:
    _, img = cap.read()
    img = cv2.flip(img, 1)
    imgRaw = img.copy()
    hands, img = detector.findHands(img, flipType=False)
    strings = str(speed)
    if started:
        print("in start loop")
        img = cv2.addWeighted(img, 0.1,imgGameStart , 0.9, 0)
    else:
        if hands == 0:
            img = cv2.addWeighted(img, 0.1,imgGameStart1, 0.4, 0)
            print("caution")
        else:
            img = cv2.addWeighted(img, 0.1, imgBackground, 0.4, 0)
            print("background")

    if hands:
        print("in loop")
        started = False
        #img = cv2.addWeighted(img, 0.1, imgBackground, 0.4, 0)
        for hand in hands:
            x, y, w, h = hand['bbox']
            h1, w1, _ = imgBat1.shape
            y1 = y - h1 // 2
            y1 = np.clip(y1, 20, 415)

            if hand['type'] == "Left":
                img = cvzone.overlayPNG(img, imgBat1, (59, y1))
                if 59 < ballPos[0] < 59 + w1 and y1 < ballPos[1] < y1 + h1:
                    speedX = -speedX
                    ballPos[0] += 30
                    speed = speed + 1
                    score[0] += 1

        if hand['type'] == "Right":
            img = cvzone.overlayPNG(img, imgBat2, (1195, y1))
            if 1195 - 50 < ballPos[0] < 1195 and y1 < ballPos[1] < y1 + h1:
                speedX = -speedX
                ballPos[0] -= 30
                speed = speed + 1
                score[1] += 1

    if ballPos[0] < 40 or ballPos[0] > 1200:
        gameOver = True

    if gameOver:
        img = imgGameOver
        cv2.putText(img, str(score[0]).zfill(2), (400, 360), cv2.FONT_HERSHEY_COMPLEX,
                    2.5, (200, 0, 200), 5)
        cv2.putText(img, str(score[1]).zfill(2), (800, 360), cv2.FONT_HERSHEY_COMPLEX,
                    2.5, (200, 0, 200), 5)


    else:

        if started == False:
            if ballPos[1] >= 500 or ballPos[1] <= 10:
                speedY = -speedY

            ballPos[0] += speedX

            ballPos[1] += speedY




        img = cvzone.overlayPNG(img, imgBall, ballPos)

        cv2.putText(img, str(score[0]), (300, 650), cv2.FONT_HERSHEY_COMPLEX, 3, (255, 255, 255), 5)
        cv2.putText(img, str(score[1]), (900, 650), cv2.FONT_HERSHEY_COMPLEX, 3, (255, 255, 255), 5)
        cv2.putText(img, str(strings), (600, 650), cv2.FONT_HERSHEY_COMPLEX, 3, (255, 255, 255), 5)

    img[580:700, 20:233] = cv2.resize(imgRaw, (213, 120))



    cv2.imshow("Tiki-Taka - The Game", img)
    key = cv2.waitKey(1)
    if key == ord('r'):
        ballPos = [100, 100]
        speedX = 15
        speedY = 15
        gameOver = False
        score = [0, 0]
        started = True
        hands = False
        strings = 15
        speed = 15
        imgGameOver = cv2.imread("Resources/gameOver.png")