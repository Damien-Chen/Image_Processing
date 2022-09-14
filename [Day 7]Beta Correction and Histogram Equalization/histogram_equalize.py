import numpy as np
import cv2


img1 = cv2.imread("D:\Desktop\IThome\lena_gray.jpg", -1)

# For Color
R, G, B = cv2.split(img1)

output1_R = cv2.equalizeHist(R)
output1_G = cv2.equalizeHist(G)
output1_B = cv2.equalizeHist(B)

img2 = cv2.merge((output1_R, output1_G, output1_B))
# For Gray
img2 = cv2.equalizeHist(img1)
cv2.imshow("Orignial", img1)
cv2.imshow("After", img2)
cv2.waitKey()
