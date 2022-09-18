import numpy as np
import cv2


def unsharp_masking(f, k = 1.0):
    g = f.copy()
    nr, nc = f.shape[:2]
    f_avg = cv2.GaussianBlur(f,(15, 15), 0)
    for x in range(nr):
        for y in range(nc):
            g_mask = int(f[x, y]) - int(f_avg[x, y])

    return g

def main():
    img1 = cv2.imread("D:\Desktop\IThome\house_test.jpg", 0)
    img2 = unsharp_masking(img1, 10.0)
    cv2.imshow("Original", img1)
    cv2.imshow("After", img2)
    cv2.waitKey()

main()



