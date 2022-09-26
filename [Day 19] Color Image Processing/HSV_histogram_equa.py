import numpy as np
import cv2

def HSV_histogram_equalization(f):
    hsv = cv2.cvtColor(f, cv2.COLOR_BGR2HSV)
    hsv[:, :, 2] = cv2.equalizeHist(hsv[:, :, 2])
    g = cv2.cvtColor(f, cv2.COLOR_HSV2BGR)
    return g

def main():
    img1 = cv2.imread("D:\Desktop\IThome\test.bmp", -1)
    img2 = HSV_histogram_equalization(img1)
    cv2.imshow("Original", img1)
    cv2.imshow("After", img2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

main()





