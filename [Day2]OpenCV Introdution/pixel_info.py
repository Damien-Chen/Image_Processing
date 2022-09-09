import numpy as np
import cv2 

global img

def onMouse(event, x, y, flags, param):
    x, y = y, x
    if img.ndim != 3:
        print("(x, y) = (%d, %d)"%(x,y),end = " ")
        print("Gray level = %3d" %img[x,y])
    else:
        print("(x, y) = (%d, %d)"%(x,y),end = " ")
        print("(R, G, B) = (%3d, %3d, %3d)"%(img[x,y,2],img[x,y,1],img[x,y,0]))

img = cv2.imread("D:\Desktop\IThome\lena.bmp", -1)
cv2.namedWindow("lena")
cv2.setMouseCallback("lena", onMouse)
cv2.imshow("lena",img)
cv2.waitKey(0)
