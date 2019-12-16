import cv2

# 0 表示微系統的第一台攝影機
cap = cv2.VideoCapture(0)
while (True):
    ret, frame = cap.read()
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    