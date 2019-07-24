import cv2
import numpy as np


# import os.path
def nothing(x):
    pass


# new_path = 'C:/Users/borah/Anaconda3/'
cv2.namedWindow('cascade')

tl_cascade = cv2.CascadeClassifier("/Users/gim-yongjun/PycharmProjects/OpenCV_Project/face_cascade/signalcascade.xml")
tl_cascade_r = cv2.CascadeClassifier("/Users/gim-yongjun/PycharmProjects/OpenCV_Project/face_cascade/signal_red.xml")
tl_cascade_g = cv2.CascadeClassifier("/Users/gim-yongjun/PycharmProjects/OpenCV_Project/face_cascade/signal_green.xml")

# #파일 있는지 확인
# if os.path.isfile(face_cascade):
#   print("Yes. it is a file")
# esif os.path.isdir(face_cascade):
#   print("Yes. it is a directory")
# esif os.path.exists(face_cascade):
#   print("Something exist")
# else :
#   print("Nothing")

cap = cv2.VideoCapture(0)

cv2.createTrackbar('w', 'cascade', 0, 1000, nothing)
cv2.createTrackbar('h', 'cascade', 0, 1000, nothing)

cv2.setTrackbarPos('w', 'cascade', 4)
cv2.setTrackbarPos('h', 'cascade', 8)

while 1:

    w = cv2.getTrackbarPos('w', 'cascade')
    h = cv2.getTrackbarPos('h', 'cascade')

    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    tmph, tmpw = gray.shape
    for i in range(0, tmph):
        for j in range(0, tmpw):
            if gray[i][j] < 50:
                gray[i][j] += 50
            elif gray[i][j] > 150:
                gray[i][j] -= 50

    # add this
    # image, reject levels level weights.
    traffic_light = tl_cascade.detectMultiScale(gray, w, h)
    tl_g = tl_cascade_g.detectMultiScale(gray, w, h)
    tl_r = tl_cascade_r.detectMultiScale(gray, w, h)
    # add this
    for (x, y, w, h) in traffic_light:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 255, 0), 2)
        # font = cv2.FONT_HERSHEY_SIMPLEX
        # cv2.putText(img, 'TL',(x-w,y-h),font,0.5,(0,255,255),2,cv2.LINE_AA)
    for (x, y, w, h) in tl_g:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
    for (x, y, w, h) in tl_r:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)


    cv2.imshow('cascade', img)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()