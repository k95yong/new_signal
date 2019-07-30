import cv2
import numpy as np


# import os.path
def nothing(x):
    pass


cv2.namedWindow('cascade')

tl_cascade = cv2.CascadeClassifier("/Users/gim-yongjun/PycharmProjects/OpenCV_Project/new/ori.xml")


cap = cv2.VideoCapture(0)

cv2.createTrackbar('w', 'cascade', 0, 1000, nothing)
cv2.createTrackbar('h', 'cascade', 0, 1000, nothing)

cv2.setTrackbarPos('w', 'cascade', 5)
cv2.setTrackbarPos('h', 'cascade', 8)


low_blue = np.array([100, 80, 30])
upper_blue = np.array([120, 255, 255])
low_red = np.array([163, 80, 80])
upper_red = np.array([183, 255, 255])
low_green = np.array([58, 80, 80])
upper_green = np.array([78, 255, 255])


while 1:

    ww = cv2.getTrackbarPos('w', 'cascade')
    hh = cv2.getTrackbarPos('h', 'cascade')

    ret, img = cap.read()
    img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    blue_mask = cv2.inRange(img_hsv, low_blue, upper_blue)
    red_mask = cv2.inRange(img_hsv, low_red, upper_red)
    green_mask = cv2.inRange(img_hsv, low_green, upper_green)
    blue_result = cv2.bitwise_and(img, img, mask=blue_mask)
    red_result = cv2.bitwise_and(img, img, mask=red_mask)
    # green_result = cv2.bitwise_and(img, img, mask=green_mask)


    gray = cv2.cvtColor(blue_result, cv2.COLOR_BGR2GRAY)
    traffic_light = tl_cascade.detectMultiScale(gray, ww, hh)
    for (x, y, w, h) in traffic_light:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 255, 0), 2)
        cv2.rectangle(blue_result, (x, y), (x + w, y + h), (255, 255, 0), 2)
        numOfLabels, img_label, stats, centroids = cv2.connectedComponentsWithStats(red_mask)
        for idx, centroid in enumerate(centroids):
            if stats[idx][0] == 0 and stats[idx][1] == 0:
                continue
            if np.any(np.isnan(centroid)):
                continue
            x, y, width, height, area = stats[idx]
            centerX, centerY = int(centroid[0]), int(centroid[1])
            if area > 10:
                cv2.circle(img, (centerX, centerY), 10, (0, 0, 255), 10)

    cv2.imshow('cascade', img)
    cv2.imshow('blue', blue_result)
    cv2.imshow('gray', gray)
    # cv2.imshow('red', red_result)
    # cv2.imshow('green', green_result)
    k = cv2.waitKey(1) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()