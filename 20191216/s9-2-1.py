import dlib
import cv2
import imutils


cap = cv2.VideoCapture(0)

# 設定 dlib 的人臉辨識
detector = dlib.get_frontal_face_detector()


while (True):
    ret, frame = cap.read()
#偵測人臉    
    face, score, idx = detector.run(frame,0)

    # 取出所有的結果為方形範圍
    for i, d in enumerate(face):
        x1 = d.left()
        x2 = d.right()
        x3 = d.top()
        x4 = d.bottom()
        text = "%2.2f(%d)" % (score[i],idx[i])
        # 辨識出人臉
        cv2.rectangle(frame,(x1,x3),(x2,x4),(0,0,255),3,cv2.LINE_AA)

        # 擺放辨識分數
        cv2.putText(frame, text, (x1,x3), cv2.FONT_HERSHEY_DUPLEX,0.7,(255,255,255),1, cv2.LINE_AA)

    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


# 關閉所養資源
cap.release()
cv2.detroyAllwindows()
