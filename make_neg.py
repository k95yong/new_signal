import glob
import cv2 as cv

images = glob.glob('/home/ubuntu/opencv_workspace/project/project_new/new_signal/pic/*.jpg')

def make_neg_images():
    pic_num = 1044
    for i in images:
        print(pic_num)
        print(i)
        img = cv.imread(i ,cv.IMREAD_GRAYSCALE)
        resized_image = cv.resize(img, (150, 150))
        cv.imwrite("neg150/" + str(pic_num) + ".jpg" ,resized_image)
        pic_num+=1

make_neg_images()
