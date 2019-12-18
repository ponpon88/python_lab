import sys, os, dlib, glob, numpy
from skimage import io 
import cv2
import imutils

if len(sys.argv) !=2:
    print("缺少要辨識的照片")
    exit()

# 68點模型檔
predictor_path ='E:\\Python_lab2\\20191216\\shape_predictor_68_face_landmarks.dat'
# 用來建立人臉的圖檔資料庫
face_rec_model_path = "E:\\Python_lab2\\20191216\\dlib_face_recognition_resnet_model_v1.dat"

#用來建立人臉的圖檔資料課
faces_folder_path = "E:\\Python_lab2\\20191218\\face"

# 需要拿來辨識的圖檔 
img_path = sys.argv[1]

# 載入人臉偵測器 dlib
detector = dlib.get_frontal_face_detector()

# 載入人臉特徵
sp = dlib.shape_predictor(predictor_path)

# 比對人臉辨識

facerec = dlib.face_recognition_model_v1(face_rec_model_path)

# 比對人臉建立串列
descriptors = []

# 比對人臉名稱串列
candidate = []

# 是用來讀取指定路徑的人臉圖檔來建立比對資料庫
for f in glob.glob(os.path.join(faces_folder_path,"*.jpg")):
    base = os.path.basename(f)
    candidate.append(os.path.splitext(base)[0])
    img = io.imread(f)
    
    dets = detector(img,1)

    for k, d in enumerate(dets):
        shape = sp(img, d)
        face_descriptor = facerec.compute_face_descriptor(img, shape)
        v = numpy.array(face_descriptor)
        descriptors.append(v)


img =io.imread(img_path)
dets = detector(img, 1)

dist = []
for k, d in enumerate(dets):
    shape = sp(img, d)
    face_descriptor = facerec.compute_face_descriptor(img, shape)
    d_test = numpy.array(face_descriptor)

    x1 = d.left()
    y1 = d.top()
    x2 = d.right()
    y2 = d.bottom()
    cv2.rectangle(img,(x1,y1),(x2,y2),(0,255,0),4, cv2.LINE_AA)

    # 把框出來的區塊,拿去跟剛剛建立的資料庫做比對,存進串列
    # 計算歐式距離
    for i in descriptors:
        dist_ = numpy.linalg.norm(i - d_test)
        dist.append(dist_)

# 將歐式距離與人名生成一個 dist
c_d = dict(zip(candidate, dist))
# 把取得到的歐式距離,由小到大排序
cd_sorted = sorted(c_d.items(), key =lambda d: d[1])
print(cd_sorted)
# 取得最短距離就辨識出最相近的人名
rec_name = cd_sorted[0][0]

# 將辨識出的人名印到影像上
cv2.putText(img, rec_name,(x1, y1), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)

img = imutils.resize(img, width=600)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
cv2.imshow("Face Recofnition", img)
# 輸入任意見離開程式
cv2.waitKey(0)
cv2.destroyAllWindows()
