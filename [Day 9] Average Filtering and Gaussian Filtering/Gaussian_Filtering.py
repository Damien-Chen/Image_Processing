import numpy as np
import cv2

img1 = cv2.imread("D:\Desktop\IThome\lena.bmp", -1)
img2 = cv2.GaussianBlur(img1, (5, 5), 0)


cv2.imshow("Orignial", img1)
cv2.imshow("5x5", img2)

cv2.waitKey()