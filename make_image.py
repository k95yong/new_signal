import urllib.request
import cv2
import numpy as np
import os

def create_pos_n_neg():
    for file_type in ['neg150']:

        for img in os.listdir(file_type):

            if file_type == 'pos':
                line = file_type + '/' + img + ' 1 0 0 40 115\n'
                with open('info_img.dat', 'a') as f:
                    f.write(line)
            elif file_type == 'neg150':
                line = file_type + '/' + img + '\n'
                with open('bg_img.txt', 'a') as f:
                    f.write(line)

create_pos_n_neg()
