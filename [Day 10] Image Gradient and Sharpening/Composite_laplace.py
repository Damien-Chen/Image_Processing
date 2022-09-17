import numpy as np
import cv2

def composite_laplacian(f):
    kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])
    temp = cv2.filter2D(f, cv2.CV_32F, kernel)
    g = np.uint8(np.clip(temp, 0, 255))
    return g

def main():
    img1 = cv2.imread("D:\Desktop\IThome\house.jpg", 0)
    img2 = composite_laplacian(img1)
    cv2.imshow("Orignial", img1)
    cv2.imshow("After", img2)
    cv2.waitKey()

main()
