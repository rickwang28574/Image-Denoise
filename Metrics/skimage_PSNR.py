import cv2 as cv
from skimage.metrics import peak_signal_noise_ratio as psnr

path_= 'BM3D_test_images/0.png'
image1 = cv.imread(path_)
image1 = cv.cvtColor(image1,cv.COLOR_BGR2GRAY) #  将图像转换为灰度图

path_= 'Basic3.jpg'
image2 = cv.imread(path_)
image2 = cv.cvtColor(image2,cv.COLOR_BGR2GRAY) #  将图像转换为灰度图

sim = psnr(image1, image2)

print(sim)

