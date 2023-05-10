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


# PERCOBAAN 1
# buat brightness untuk gambar grayscale 
# membuat variable img_brightness untuk menampung
img_brightness = np.zeros(img.shape, dtype = np.uint8)

# fungsi penambahan brightness dengan nilai yang menjadi parameter
def brighter(nilai):
    for y in range(0, img_height):
        for x in range(0, img_width):
            red     = img[y][x][0]
            green   = img[y][x][1]
            blue    = img[y][x][2]
            gray    = (int(red) + int(green) + int(blue))/3
            gray    += nilai
            if gray > 255:
                gray = 255
            if gray < 0:
                gray = 0
            img_brightness[y][x] = (gray, gray, gray)

# menampilkan gambar dengan parameter -100
brighter(-100)
plt.imshow(img_brightness)
plt.title('Brightness -100')
plt.show()

brighter(25)
plt.imshow(img_brightness)
plt.title('Brightness 25')
plt.show()

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


