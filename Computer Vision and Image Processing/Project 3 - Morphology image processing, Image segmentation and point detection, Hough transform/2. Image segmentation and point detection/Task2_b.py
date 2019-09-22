import cv2
import numpy as np;
import matplotlib.pyplot as plt

im = cv2.imread('segment.jpg',0)
r,c = im.shape

x = []

index = np.zeros(255, dtype=int)

for i in range (r):
    for j in range (c):
        v = im[i][j]
        if (v != 0):
            index[v] += 1

x = np.asarray(list(range(255)))

plt.bar(x, index) 
plt.show()

img = cv2.imread('segment.jpg',0)
img1 = np.zeros(img.shape)

r,c = img.shape

for i in range (0, r):
    for j in range (0, c):
        if (img[i][j] > 204):
            img1[i][j] = 255
            
cv2.imwrite('seg-thres.jpg', img1)