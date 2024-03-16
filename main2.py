from PIL import Image
import numpy as np
from ALP4 import *

# imgBlack = np.zeros([768,1024])
# imgWhite = np.ones([1024,768])*(2**8-1)
# imgSeq = np.concatenate([imgBlack.ravel(),imgWhite.ravel()])
# print(imgSeq)
# print(type(imgSeq))
DMD = ALP4(version = '4.3')
# img1 = Image.open("C:/Users/yangd/Desktop/SequenceTextAndCircle-XGA/ProjectionSequence_Count1024x768_01.png")
img1 = Image.open("C:/Users/yangd/Desktop/OIP-C.jpg")
img_array1 = np.array(img1)

a = DMD.ImgToBitPlane(img_array1, 1)

bitplane_image = Image.fromarray((a * 255).astype(np.uint8))
bitplane_image.show()