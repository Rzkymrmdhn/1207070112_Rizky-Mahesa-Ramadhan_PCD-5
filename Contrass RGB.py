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

# membuat variable img_brightness untuk menampung
img_rgbcontrass = np.zeros(img.shape, dtype = np.uint8)

#fungsi untuk brightness RGB dengan nilai parameter
def contrass(nilai):
    for y in range(0, img_height):
        for x in range(0, img_width):
            red=img[y][x][0]
            red+=nilai
            if red > 255:
                red = 255
            green = img[y][x][1]
            green += nilai
            if green > 255:
                green = 255
            blue = img[y][x][2]
            blue += nilai
            if blue > 255:
                blue = 255
            img_rgbcontrass[y][x] = (red, green, blue)
        
contrass(2)
plt.imshow(img_rgbcontrass)
plt.title("Contrass 2")
plt.show()

contrass(10)
plt.imshow(img_rgbcontrass)
plt.title("Contrass 10")
plt.show()