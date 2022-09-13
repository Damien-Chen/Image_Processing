import numpy as np
import cv2

img1 = cv2.imread("D:\Desktop\IThome\lena.bmp", -1)

def gamma_correction(f, gamma = 2.0):
    g = f.copy()
    nr,nc = f.shape[:2]
    c = 255.0 / (255.0 ** gamma)
    table = np.zeros(256)
    for i in range(256):
        table[i] = round(i ** gamma * c, 0)
    if f.ndim != 3:
        for x in range(nr):
            for y in range(nc):
                g[x, y] = table[x, y]
    else:
        for x in range(nr):
            for y in range(nc):
                for k in range(3):
                    g[x, y, k] = table[f[x, y, k]]


img2 = gamma_correction(img1, 0.1)
cv2.imshow("After", img2)
cv2.waitKey()
