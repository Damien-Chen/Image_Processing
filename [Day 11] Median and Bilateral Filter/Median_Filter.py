import numpy as np
import cv2


img1 = cv2.imread("D:\Desktop\IThome\lena_falt and pepper.jpg", 0)
img2 = cv2.medianBlur(img1, 3)
cv2.imshow("Original", img1)
cv2.imshow("After", img2)
cv2.waitKey()


