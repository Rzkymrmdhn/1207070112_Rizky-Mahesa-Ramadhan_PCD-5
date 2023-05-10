#import library
import matplotlib.pyplot as plt

from skimage import data
from skimage.io import imread
from skimage.color import rgb2gray
from skimage.util import invert
import numpy as np

astronautImage = data.astronaut()
astroCropped = astronautImage.copy()
astroCropped = astroCropped[0:256,64:320]

print('Astro Ori Shape : ',astronautImage.shape)
print('Astro Crop Shape : ',astroCropped.shape)

inv = invert(astroCropped)
print('Shape Input : ', astroCropped.shape)
print('Shape Output : ',inv.shape)

fig, axes = plt.subplots(2, 2, figsize=(12, 12))
ax = axes.ravel()

ax[0].imshow(astroCropped)
ax[0].set_title("Citra Input")

ax[1].hist(astroCropped.ravel(), bins=256)
ax[1].set_title('Histogram Input')

ax[2].imshow(inv)
ax[2].set_title('Citra Output (Inverted Image)')

ax[3].hist(inv.ravel(), bins=256)
ax[3].set_title('Histogram Output')
plt.show()