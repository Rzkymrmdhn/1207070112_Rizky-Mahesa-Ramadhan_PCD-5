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
img_rgbbright = np.zeros(img.shape, dtype = np.uint8)

#fungsi untuk brightness RGB dengan nilai parameter
def rgbbrighter(nilai):
    for y in range(0, img_height):
        for x in range(0, img_width):
            red=img[y][x][0]
            red+=nilai
            if red > 255:
                red = 255
            if red < 0:
                red = 0
            green = img[y][x][1]
            green += nilai
            if green > 255:
                green = 255
            if green < 0:
                green = 0
            blue = img[y][x][2]
            blue += nilai
            if blue > 255:
                blue = 255
            if blue < 0 :
                blue = 0
            img_rgbbright[y][x] = (red, green, blue)
        
rgbbrighter(-100)
plt.imshow(img_rgbbright)
plt.title("Brightness -100")
plt.show()

rgbbrighter(100)
plt.imshow(img_rgbbright)
plt.title("Brightness 100")
plt.show()