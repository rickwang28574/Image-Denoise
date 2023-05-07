import cv2 as cv
from skimage.metrics import mean_squared_error as mse
import os

# 设定原图像的文件夹（第一个文件夹）
folder1 = 'path/to/folder1'
# 设定目标图像的文件夹（第二个文件夹）
folder2 = 'path/to/folder2'
# 初始化用于MSE的统计量
mse_total = 0

# 获取文件夹中的所有图像文件

# 获取原图像的文件夹（第一个文件夹）中的文件
img_files1 = sorted([os.path.join(folder1, f) for f in os.listdir(folder1)])
# 获取目标图像的文件夹（第二个文件夹）中的文件
img_files2 = sorted([os.path.join(folder2, f) for f in os.listdir(folder2)])

# 遍历每一对图像并计算MSE
for i in range(len(img_files1)):
    # 将原图像转换为灰度图
    img1 = cv.imread(img_files1[i], cv.IMREAD_GRAYSCALE)
    # 将目标图像转换为灰度图
    img2 = cv.imread(img_files2[i], cv.IMREAD_GRAYSCALE)
    # 计算本次MSE的值
    mse_val = mse(img1, img2)
    # 统计MSE总量
    mse_total += mse_val
    # 输出本次的MSE计算量
    print(f"MSE between {img_files1[i]} and {img_files2[i]}: {mse_val}")

# 计算平均MSE

# 计算平均MSE值
mse_avg = mse_total / len(img_files1)
# 输出平均MSE值
print(f"Average MSE: {mse_avg}")