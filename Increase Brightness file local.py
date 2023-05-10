#import library
import matplotlib.pyplot as plt
import cv2

from skimage import data
from skimage.io import imread
from skimage.color import rgb2gray
from skimage.util import invert
import numpy as np

imageLocal1 = imread("E:/PicsArt_08-31-11.13.46.jpg")
imageLocal1Cropped = imageLocal1.copy()
imageLocal1Cropped = imageLocal1Cropped[64:256,128:320]

copyimageLocal1 = imageLocal1Cropped.copy().astype(float)

# m1, n1 = copyKucing.shape[:2]  # hanya memuat satu nilai tuple

# Menambahkan variabel brightness
brightness = 100
imageLocal1_bright = np.clip(copyimageLocal1 + brightness, 0, 255).astype(dtype=np.uint8)

# for baris in range(0, m1 - 1):
#     for kolom in range(0, n1 - 1):
#         a1 = baris
#         b1 = kolom
#         imageLocal1_bright[a1, b1] = copyimageLocal1[baris, kolom] + 100

fig, axes = plt.subplots(2, 2, figsize=(8, 8))
ax = axes.ravel()

# Plot Gambar Input dengan cv2.imshow
ax[0].imshow(cv2.cvtColor(imageLocal1, cv2.COLOR_BGR2RGB))
ax[0].set_title("Citra Input 2")

ax[1].hist(imageLocal1Cropped.ravel(), bins=256)
ax[1].set_title("Histogram Input")

ax[2].imshow(cv2.cvtColor(imageLocal1_bright, cv2.COLOR_BGR2RGB))
ax[2].set_title("Citra Output (Brightness +100)")

ax[3].hist(imageLocal1_bright.ravel(), bins=256)
ax[3].set_title("Histogram Output")

fig.tight_layout()
plt.show()
