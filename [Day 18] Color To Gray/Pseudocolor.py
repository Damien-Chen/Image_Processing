import numpy as np
import cv2

img1 = cv2.imread("D:\Desktop\IThome\lena.bmp", -1)
img2 = cv2.applyColorMap(img1, cv2.COLORMAP_HSV)


cv2.imshow("Original", img1)
cv2.imshow("After", img2)
cv2.waitKey()
cv2.destroyAllWindows()



