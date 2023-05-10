#import library
import matplotlib.pyplot as plt

from skimage import data
from skimage.io import imread
from skimage.color import rgb2gray
from skimage.util import invert
import numpy as np

# membaca gambar dari file lokal
imageLocal1 = imread("E:/UIN SGD/SMT 6/PENGOLAHAN CITRA DIGITAL/PRAKTIKUM 5/PicsArt_09-12-09.03.11.jpg")
imageLocal2 = imread("E:/mahe.jpg")

# crop bagian tengah gambar
crop_width = 192
crop_height = 192
imageLocal1Cropped = imageLocal1.copy()
imageLocal1Cropped = imageLocal1Cropped[128:128+crop_height, 256:256+crop_width]
imageLocal2Cropped = imageLocal2.copy()
imageLocal2Cropped = imageLocal2[128:128+crop_height, 256:256+crop_width]

fig, axes = plt.subplots(2, 2, figsize=(12, 12))
ax = axes.ravel()
ax[0].imshow(imageLocal1)
ax[0].set_title("Citra Input 1")

ax[1].imshow(imageLocal2, cmap='gray')
ax[1].set_title('Citra Input 2')

ax[2].imshow(imageLocal1Cropped)
ax[2].set_title("Citra Output 1")

ax[3].imshow(imageLocal2Cropped, cmap='gray')
ax[3].set_title('Citra Output 2')
plt.show()