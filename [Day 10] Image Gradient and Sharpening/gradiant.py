import numpy as np
import cv2


def Sobel_gradiant(f, direction = 1):
    soble_x = np.array([[1, -2, -1], [0, 0, 0], [1, 2, 1]])
    soble_y = np.array([[-1, 0, 1,], [-2, 0, 2], [-1, 0, 1]])
    if direction == 1:
        grad_x = cv2.filter2D(f, cv2.CV_32F, soble_x)
        gx = abs(grad_x)
        g = np.uint8(np.clip(gx, 0, 255))
    elif direction == 2:
        grad_y = cv2.filter2D(f, cv2.CV_32F, soble_y)
        gy = abs(grad_y)
        g = np.uint8(np.clip(gy, 0, 255))
    else:
        grad_x = cv2.filter2D(f, cv2.CV_32F, soble_x)
        grad_y = cv2.filter2D(f, cv2.CV_32F, soble_y)
        magnitude = abs(grad_x) + abs(grad_y)
        g = np.uint8(np.clip(magnitude, 0, 255))
    return g

def main():
    img = cv2.imread("D:\Desktop\IThome\house.jpg", 0)
    gx = Sobel_gradiant(img, 1)
    gy = Sobel_gradiant(img, 2)
    g = Sobel_gradiant(img, 3)
    cv2.imshow("Original", img)
    cv2.imshow("Gradient in x", gx)
    cv2.imshow("Gradient in y", gy)
    cv2.imshow("Gradient", g)
    cv2.waitKey()

main()
