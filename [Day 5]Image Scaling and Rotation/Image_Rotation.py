import numpy as np
import cv2

img1 = cv2.imread("D:\Desktop\IThome\lena.bmp", -1)

nr2,nc2 = img1.shape[:2]

rotation_matrix = cv2.getRotationMatrix2D((nc2 / 2, nr2 / 2), 30, 1)
img2 = cv2.warpAffine(img1, rotation_matrix,(nc2, nr2))

cv2.imshow("Original", img1)
cv2.imshow("After", img2)

cv2.waitKey()
cv2.destroyAllWindows()

