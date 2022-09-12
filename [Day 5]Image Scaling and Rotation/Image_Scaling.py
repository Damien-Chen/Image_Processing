import numpy as np
import cv2

img1 = cv2.imread("D:\Desktop\IThome\lena.bmp", -1)

nr,nc = img1.shape[:2]
scale = eval(input("Please enter scale:"))
nr2 = int(nr * scale)
nc2 = int(nc * scale)

img2 = cv2.resize(img1, (nr2,nc2), interpolation = cv2.INTER_NEAREST)
img3 = cv2.resize(img1, (nr2,nc2), interpolation = cv2.INTER_LINEAR)
cv2.imshow("Original", img1)
cv2.imshow("After", img2)
cv2.imshow("Second", img3)

cv2.waitKey()
cv2.destroyAllWindows()



