#import library
import numpy as np
import matplotlib.pyplot as plt
import cv2

#load gambar
img = cv2.imread('PicsArt_09-12-09.03.11.jpg')

#mendapatkan/define resolusi dan tipe gambar
img_height  = img.shape[0]
img_width   = img.shape[1]
img_channel = img.shape[2]
img_type    = img.dtype

# contrass autolevel
img_autocontrass = np.zeros(img.shape, dtype = np.uint8)

# melakukan penambahan contrass secara otomatis
def autocontrass():
    xmax=255
    xmin=0
    d = 0

    for y in range(0, img_height):
        for x in range(0, img_width):
            red=img[y][x][0]
            green=img[y][x][1]
            blue=img[y][x][2]
            gray=(int(red)+int(green)+int(red))/3
            if gray < xmax:
                xmax = gray
            if gray > xmin:
                xmin = gray
    d = xmin - xmax
    for y in range(0, img_height):
        for x in range(0, img_width):
            red=img[y][x][0]
            green=img[y][x][1]
            blue=img[y][x][2]
            gray=(int(red)+int(green)+int(red))/3
            gray=int(float(255/d)*(gray-xmax))
            img_autocontrass[y][x]=(gray,gray,gray)

#menampilkan hasil autolevel contrass
autocontrass()
plt.imshow(img_autocontrass)
plt.title("Contrass Autolevel")
plt.show()