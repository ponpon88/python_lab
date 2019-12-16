import dlib
import cv2
import imutils


cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH,650)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT,500)
# 設定 dlib 的人臉辨識
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor('E:\\Python_lab2\\20191216\\shape_predictor_68_face_landmarks.dat')

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

        # 設定68個點的格式
        landmark_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # 找出特徵點
        shape = predictor(landmark_frame,d)

        for i in range(68):
            cv2.circle(frame, (shape.part(i).x,shape.part(i).y),3 ,(0,0,255),2)
            cv2.putText(frame,str(i), (shape.part(i).x,shape.part(i).y),cv2.FONT_HERSHEY_DUPLEX,0.5,(255,0,0),1) 
        

    cv2.imshow('Face Detection Result:',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


# 關閉所養資源
cap.release()
cv2.detroyAllwindows()
