import numpy as np
import cv2


img1 = cv2.imread("D:\Desktop\IThome\lena.bmp", 0)
img2 = cv2.bilateralFilter(img1, 5, 50, 50)
cv2.imshow("Original", img1)
cv2.imshow("After", img2)
cv2.waitKey()


