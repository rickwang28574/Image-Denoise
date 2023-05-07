import cv2 as cv

# PSNR
from skimage.metrics import peak_signal_noise_ratio as psnr
# SSIM
from skimage.metrics import structural_similarity as ssim
# MSE
from skimage.metrics import mean_squared_error as mse

path_= './0.png'
image1 = cv.imread(path_)
image1 = cv.cvtColor(image1,cv.COLOR_BGR2GRAY) #  将图像转换为灰度图

path_= './Basic3.jpg'
image2 = cv.imread(path_)
image2 = cv.cvtColor(image2,cv.COLOR_BGR2GRAY) #  将图像转换为灰度图


PSNR_value = psnr(image1, image2)

SSIM_value = ssim(image1, image2)

MSE_value = mse(image1, image2)

print('The PSNR of the original image and the denoised image is: %f' % PSNR_value)
print('The SSIM of the original image and the denoised image is: %f' % SSIM_value)
print('The MSE of the original image and the denoised image is: %f' % MSE_value)