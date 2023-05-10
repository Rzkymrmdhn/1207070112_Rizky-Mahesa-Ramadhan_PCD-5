#import library
import matplotlib.pyplot as plt

from skimage import data
from skimage.io import imread
from skimage.color import rgb2gray
from skimage.util import invert
import numpy as np

#percobaan 1 : Crop Image
astronautImage = data.astronaut()
cameraImage = data.camera()
astroCropped = astronautImage.copy()
astroCropped = astroCropped[0:256,64:320]
cameraCropped = cameraImage.copy()
cameraCropped = cameraCropped[64:256,128:320]

fig, axes = plt.subplots(2, 2, figsize=(12, 12))
ax = axes.ravel()
ax[0].imshow(astronautImage)
ax[0].set_title("Citra Input 1")

ax[1].imshow(cameraImage, cmap='gray')
ax[1].set_title('Citra Input 2')

ax[2].imshow(astroCropped)
ax[2].set_title("Citra Output 1")

ax[3].imshow(cameraCropped, cmap='gray')
ax[3].set_title('Citra Output 2')
plt.show()