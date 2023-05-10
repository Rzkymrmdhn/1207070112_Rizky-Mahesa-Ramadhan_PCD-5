#import library
import matplotlib.pyplot as plt

from skimage import data
from skimage.io import imread
from skimage.color import rgb2gray
from skimage.util import invert
import numpy as np

imageLocal1 = imread("E:/mahe.jpg")
# crop bagian tengah gambar
crop_width = 192
crop_height = 192
imageLocal1Cropped = imageLocal1.copy()
imageLocal1Cropped = imageLocal1Cropped[128:128+crop_height, 256:256+crop_width]

print('imageLocal1 Ori Shape : ',imageLocal1.shape)
print('imageLocal1 Crop Shape : ',imageLocal1Cropped.shape)

inv = invert(imageLocal1Cropped)
print('Shape Input : ', imageLocal1Cropped.shape)
print('Shape Output : ',inv.shape)

fig, axes = plt.subplots(2, 2, figsize=(12, 12))
ax = axes.ravel()

ax[0].imshow(imageLocal1Cropped)
ax[0].set_title("Citra Input")

ax[1].hist(imageLocal1Cropped.ravel(), bins=256)
ax[1].set_title('Histogram Input')

ax[2].imshow(inv)
ax[2].set_title('Citra Output (Inverted Image)')

ax[3].hist(inv.ravel(), bins=256)
ax[3].set_title('Histogram Output')
plt.show()