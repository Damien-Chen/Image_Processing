
import numpy as np
import cv2

def Sobel_edge_detection(f):
    grad_x = cv2.Sobel(f, cv2.CV_32F, 1, 0, ksize = 3)
    grad_y = cv2.Sobel(f, cv2.CV_32F, 0, 1, ksize = 3)
    magnitude = abs(grad_x) + abs(grad_y)
    g = np.uint8(np.clip(magnitude, 0, 255))
    ret, g = cv2.threshold(g, 127, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    return g

def main():
    img1 = cv2.imread("D:\Desktop\IThome\lena.bmp", -1)
    img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    img2 = Sobel_edge_detection(img1)
    cv2.imshow("Original", img1)
    cv2.imshow("After", img2)
    cv2.waitKey()
    cv2.destroyAllWindows()

main()


