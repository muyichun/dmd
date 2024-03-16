import os
import numpy as np
from ALP4 import *
import time
from PIL import Image

# 初始化DMD
DMD = ALP4(version = '4.3')
DMD.Initialize()

img1 = Image.open("C:/Users/yangd/Desktop/rgb/2.jpg")
gray_image = img1.convert("L")
image_array = np.array(gray_image).ravel()


DMD.SeqAlloc(nbImg = 1, bitDepth = 1)
DMD.SeqPut(imgData = image_array)
DMD.SetTiming(pictureTime = 1*10**6)
DMD.Run()
time.sleep(50)
# Stop the sequence display
DMD.Halt()
# Free the sequence from the onboard memory
DMD.FreeSeq()
# De-allocate the device
DMD.Free()