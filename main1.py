import numpy as np
from ALP4 import *
import time
from PIL import Image

# Load the Vialux .dll
DMD = ALP4(version = '4.3')
# Initialize the device
DMD.Initialize()

img1 = Image.open("C:/Users/yangd/Desktop/rgb/1.jpg")
gray_image = img1.convert("L")
imgSeq = np.array(gray_image).ravel()

# Allocate the onboard memory for the image sequence
DMD.SeqAlloc(nbImg = 1, bitDepth = 8)
# Send the image sequence as a 1D list/array/numpy array
DMD.SeqPut(imgData = imgSeq)
# Set image rate to 1 Hz
DMD.SetTiming(pictureTime = 1*10**6)
# Run the sequence in an infinite loop
DMD.Run()

time.sleep(10)

# Stop the sequence display
DMD.Halt()
# Free the sequence from the onboard memory
DMD.FreeSeq()
# De-allocate the device
DMD.Free()