import numpy as np
import cv2

img1 = cv2.imread("D:\Desktop\IThome\lena.bmp", -1)

def image_negative(f):
    g = 255 - f
    return g

img2 = image_negative(img1)
cv2.imshow("After", img2)
cv2.waitKey()
