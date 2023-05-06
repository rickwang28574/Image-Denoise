import cv2
import numpy as np
import math

def psnr(img1, img2):
    # Normalizes image pixel values to floats in the range [0, 1]
    img1 = img1.astype(np.float32) / 255.0
    img2 = img2.astype(np.float32) / 255.0

    # Calculate MSE
    mse = np.mean((img1 - img2) ** 2)

    # If MSE is 0, PSNR is positive infinity
    if mse == 0:
        return float('inf')

    # Calculate the PSNR value
    PIXEL_MAX = 1.0
    psnr = 20 * math.log10(PIXEL_MAX / math.sqrt(mse))
    return psnr

img1 = cv2.imread('BM3D_test_images/0.png', cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread('Basic3.jpg', cv2.IMREAD_GRAYSCALE)

psnr_value = psnr(img1, img2)
print('PSNR: {:.2f}'.format(psnr_value))
