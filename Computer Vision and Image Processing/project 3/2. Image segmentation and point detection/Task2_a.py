import cv2
import numpy as np;
import matplotlib.pyplot as plt

# Read image
img = cv2.imread("point.jpg", 0)
        
largest = 255
smallest = 0
r,c = img.shape

img1 = np.zeros(img.shape)
kernel = [[-1,-1,-1],[-1,8,-1],[-1,-1,-1]] 

for x in range(1,r-1):
    for y in range(1,c-1): 
        img1[x][y] = img[x-1][y-1] * kernel[0][0] + \
                     img[x-1][y] * kernel[0][1] + \
                     img[x-1][y+1] * kernel[0][2] + \
                     img[x][y-1] * kernel[1][0] + \
                     img[x][y] * kernel[1][1] + \
                     img[x][y+1] * kernel[1][2] + \
                     img[x+1][y-1] * kernel[2][0] + \
                     img[x+1][y] * kernel[2][1] + \
                     img[x+1][y+1] * kernel[2][2]
        
        if (img1[x][y] > largest):
            largest = img1[x][y]

for x in range(1,r-1):
    for y in range(1,c-1):
        img1[x][y] = (np.abs(img1[x][y]) / np.abs(largest))*255
        
x = []

index = np.zeros(256, dtype=int)

for i in range (r):
    for j in range (c):
        v = img[i][j]
        v = int(v)
        index[v] += 1

x = np.asarray(list(range(256)))

plt.bar(x, index) 
plt.show()
        
img2 = np.zeros(img1.shape)

for i in range (r):
    for j in range (c):
        if(img1[i][j] > 128):
            img2[i][j] = 255
            
cv2.imwrite('porosity.jpg', img2)