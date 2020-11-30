from PIL import Image
import numpy as np

image = Image.open('oxygen.png')
img = np.array([[image.getpixel((i, j)) for j in range(image.height)] for i in range(image.width)])

for i in range(image.width):
    for j in range(image.height):
        if img[i,j,0] == img[i,j,1] and img[i,j,1] == img[i,j,2]:
            print((i,j), end=' ')
    print()

img = img[:608, 43:52, 0]
for i in range(0, img.shape[0], 7):
    print(chr(img[i,0]), end='')
print()

num = [105, 110, 116, 101, 103, 114, 105, 116, 121]
for n in num:
    print(chr(n), end='')
print()
