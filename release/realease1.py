import os
import numpy as np
from ALP4 import *
import time
from PIL import Image
'''
展示一组灰度图变化
'''
# 初始化DMD
DMD = ALP4(version = '4.3')
DMD.Initialize()

# 图片数量
image_nums = 10
# 文件夹路径
folder_path = "C:/Users/yangd/Desktop/SequenceTextAndCircle-XGA/"
# 初始化一个空列表，用于存储图像数组
image_arrays = []
# 循环读取每张图片
for i in range(image_nums):
    # 打开图像文件
    image = Image.open(folder_path + str(i+1) + ".png")
    # 将图像转换为数组并添加到列表中
    image_array = np.array(image)
    image_arrays.append(image_array)

# 将图像数组列表转换为NumPy数组
imgSeq = np.array(image_arrays)

DMD.SeqAlloc(nbImg = image_nums, bitDepth = 8)
DMD.SeqPut(imgData = imgSeq)
DMD.SetTiming(pictureTime = 1*10**6)
DMD.Run()
time.sleep(20)
# Stop the sequence display
DMD.Halt()
# Free the sequence from the onboard memory
DMD.FreeSeq()
# De-allocate the device
DMD.Free()