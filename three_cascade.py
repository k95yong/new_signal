import cv2
import numpy as np


# import os.path
def nothing(x):
    pass


cv2.namedWindow('cascade')

tl_cascade = cv2.CascadeClassifier("/Users/gim-yongjun/PycharmProjects/OpenCV_Project/new/signalcascade.xml")


cap = cv2.VideoCapture(1)

cv2.createTrackbar('w', 'cascade', 0, 1000, nothing)
cv2.createTrackbar('h', 'cascade', 0, 1000, nothing)

cv2.setTrackbarPos('w', 'cascade', 4)
cv2.setTrackbarPos('h', 'cascade', 8)


low_blue = np.array([100, 70, 30])
upper_blue = np.array([120, 255, 255])
low_red = np.array([163, 80, 80])
upper_red = np.array([183, 255, 255])
low_green = np.array([58, 80, 80])
upper_green = np.array([78, 255, 255])


while 1:

    w = cv2.getTrackbarPos('w', 'cascade')
    h = cv2.getTrackbarPos('h', 'cascade')

    ret, img = cap.read()
    img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    blue_mask = cv2.inRange(img_hsv, low_blue, upper_blue)
    red_mask = cv2.inRange(img_hsv, low_red, upper_red)
    green_mask = cv2.inRange(img_hsv, low_green, upper_green)

    # numOfLabels, img_label, stats, centroids = cv.connectedComponentsWithStats(img_mask)
    # kernal = np.ones((11, 11), np.uint8)
    # img_mask = cv2.morphologyEx(img_mask, cv2.MORPH_OPEN, kernal)
    # img_mask = cv2.morphologyEx(img_mask, cv2.MORPH_CLOSE, kernal)

    blue_result = cv2.bitwise_and(img, img, mask=blue_mask)
    red_result = cv2.bitwise_and(img, img, mask=red_mask)
    green_result = cv2.bitwise_and(img, img, mask=green_mask)

    numOfLabels, img_label, stats, centroids = cv2.connectedComponentsWithStats(red_mask)
    gray = cv2.cvtColor(blue_result, cv2.COLOR_BGR2GRAY)
    traffic_light = tl_cascade.detectMultiScale(gray, 4, 8)
    for (x, y, w, h) in traffic_light:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 255, 0), 2)
        cv2.rectangle(blue_result, (x, y), (x + w, y + h), (255, 255, 0), 2)
        # for idx, centroid in enumerate(centroids):
        #     if stats[idx][0] == 0 and stats[idx][1] == 0:
        #         continue
        #     if np.any(np.isnan(centroid)):
        #         continue
        #     x, y, width, height, area = stats[idx]
        #     centerX, centerY = int(centroid[0]), int(centroid[1])
        #     if area > 10:
        #         cv2.circle(img, (centerX, centerY), 10, (0, 0, 255), 10)

    cv2.imshow('blue', blue_result)
    cv2.imshow('gray', gray)
    # cv2.imshow('red', red_result)
    # cv2.imshow('green', green_result)
    cv2.imshow('cascade', img)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()