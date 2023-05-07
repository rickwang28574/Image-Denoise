import cv2 as cv
from skimage.metrics import peak_signal_noise_ratio as psnr
import os

# 设定原图像的文件夹（第一个文件夹）
folder1 = 'path/to/folder1'
# 设定目标图像的文件夹（第二个文件夹）
folder2 = 'path/to/folder2'
# 初始化用于PSNR的统计量
psnr_total = 0

# 获取文件夹中的所有图像文件

# 获取原图像的文件夹（第一个文件夹）中的文件
img_files1 = sorted([os.path.join(folder1, f) for f in os.listdir(folder1)])
# 获取目标图像的文件夹（第二个文件夹）中的文件
img_files2 = sorted([os.path.join(folder2, f) for f in os.listdir(folder2)])

# 遍历每一对图像并计算PSNR
for i in range(len(img_files1)):
    # 将原图像转换为灰度图
    img1 = cv.imread(img_files1[i], cv.IMREAD_GRAYSCALE)
    # 将目标图像转换为灰度图
    img2 = cv.imread(img_files2[i], cv.IMREAD_GRAYSCALE)
    # 计算本次PSNR的值
    psnr_val = psnr(img1, img2)
    # 统计PSNR总量
    psnr_total += psnr_val
    # 输出本次的PSNR计算量
    print(f"PSNR between {img_files1[i]} and {img_files2[i]}: {psnr_val}")

# 计算平均PSNR

# 计算平均PSNR值
psnr_avg = psnr_total / len(img_files1)
# 输出平均PSNR值
print(f"Average PSNR: {psnr_avg}")