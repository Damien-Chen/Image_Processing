import numpy as np
import cv2

def RGB_model(f, channel):
    if channel == 1:
        return f[:, :, 2]
    elif channel == 2:
        return f[:, :, 1]
    else:
        return f[:, :, 0]

def main():
    img = cv2.imread("D:\Desktop\IThome\rose.bmp", -1)
    R = RGB_model(img, 1)
    G = RGB_model(img, 2)
    B = RGB_model(img, 3)
    cv2.imshow("R", R)
    cv2.imshow("G", G)
    cv2.imshow("B", B)
    cv2.waitKey()
    cv2.destroyAllWindows()

main() 
