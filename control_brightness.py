import cv2 as cv

cap = cv.VideoCapture(0)


while 1:
    ret, img = cap.read()
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    gray2 = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    h, w = gray2.shape
    for i in range(0, h):
        for j in range(0, w):
            if gray2[i][j] < 50:
                gray2[i][j]+=50
            elif gray2[i][j] > 150:
                gray2[i][j] -= 50

    cv.imshow('t1', gray)
    cv.imshow('t2', gray2)

    k = cv.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv.destroyAllWindows()