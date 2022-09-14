import numpy as np
import cv2
import scipy.special as special

img1 = cv2.imread("D:\Desktop\IThome\lena.bmp", -1)

def beta_correction(f, a = 2.0, b = 2.0):
    g = f.copy()
    nr, nc = f.shape[:2]
    x = np.linspace(0, 1, 256)
    table = np.round(special.betainc(a, b, x) * 255, 0)
    if f.ndim != 3:
        for x in range(nr):
            for y in range(nc):
                g[x, y] = table[f[x, y]]

    else:
        for x in range(nr):
            for y in range(nc):
                for k in range(3):
                    g[x, y, k] = table[f[x,y,k]]
    
    return g
img2 = beta_correction(img1, a = 0.5, b = 0.5)
cv2.imshow("After", img2)
cv2.waitKey()
