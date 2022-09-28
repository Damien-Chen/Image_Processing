
import numpy as np
import cv2

img1 = cv2.imread("D:\Desktop\IThome\lena.bmp", -1)
img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
img2 = cv2.Canny(img1, 50, 100)
cv2.imshow("Original", img1)
cv2.imshow("After", img2)
cv2.waitKey()
cv2.destroyAllWindows()



