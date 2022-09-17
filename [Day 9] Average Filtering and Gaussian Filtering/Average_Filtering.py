import numpy as np
import cv2

img1 = cv2.imread("D:\Desktop\IThome\lena.bmp", -1)
img2 = cv2.blur(img1, (5, 5))
img3 = cv2.blur(img1, (11, 11))
img4 = cv2.blur(img1, (20, 20))

cv2.imshow("Orignial", img1)
cv2.imshow("5x5", img2)
cv2.imshow("11x11", img3)
cv2.imshow("20x20", img4)
cv2.waitKey()