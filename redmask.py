import cv2
import numpy as n

kamera = cv2.VideoCapture(0)

while (1):
    ret, frame = kamera.read()

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    alt_kırmızı = n.array([160, 100, 100])
    ust_kırmızı = n.array([179, 225, 225])
    mask = cv2.inRange(hsv, alt_kırmızı, ust_kırmızı)
    son_resim = cv2.bitwise_and(frame, frame, mask=mask)

    cv2.imshow('orjinal', frame)
    cv2.imshow('mask', mask)
    cv2.imshow('son_resim', son_resim)

    if cv2.waitKey(25) & 0xFF == ord('q'):
        break
kamera.release()
cv2.destroyAllWindows()
