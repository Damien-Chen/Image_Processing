import numpy as np
import cv2

def image_quantization(f, bits):
    g = f.copy()
    nr, nc = f.shape[:2]
    levels = 2**bits
    interval = 256 / levels
    gray_level_interval = 255 / (levels - 1)
    table = np.zeros(256)
    for k in range(256):
        for l in range(levels):
            if k >= l * interval and k < (l+l)*interval:
                table[k] = round(l * gray_level_interval)
    for x in range(nr):
        for y in range(nc):
            g[x,y] = np.uint8(table[f[x,y]])
    return g

def main():
    img1 = cv2.imread("D:\Desktop\IThome\lena.bmp", -1)
    img2 = image_quantization(img1, 5)
    img3 = image_quantization(img1, 4)
    img4 = image_quantization(img1, 3)
    img5 = image_quantization(img1, 2)
    img6 = image_quantization(img1, 1)
    cv2.imshow("Original Image", img1)
    cv2.imshow("Quant5",img2)
    cv2.imshow("Quant4",img3)
    cv2.imshow("Quant3",img4)
    cv2.imshow("Quant2",img5)
    cv2.imshow("Quant1",img6)
    cv2.waitKey()

main()
