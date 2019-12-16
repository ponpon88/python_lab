import dlib
import cv2
import imutils

# 讀取 people.jpg

img = cv2.imread('E:\\Python_lab2\\20191216\\people.jpg')

# 處理圖檔大小
img = imutils.resize(img, width=1280)

# 設定 dlib 的人臉辨識
detector = dlib.get_frontal_face_detector()

#偵測人臉
faces = detector(img,0)

# 取出所有的結果為方形範圍
for i,d in enumerate(faces):
    x1 = d.left()
    x2 = d.right()
    x3 = d.top()
    x4 = d.bottom()
   
    # 辨識出人臉
    cv2.rectangle(img,(x1,x3),(x2,x4),(0,0,255),3,cv2.LINE_AA)
    cv2.imshow("Face Detection zResilt:",img)
# 關閉所養資源

cv2.waitKey(0)
cv2.detroyAllwindows()
