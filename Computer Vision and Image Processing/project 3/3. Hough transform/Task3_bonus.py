import cv2
import numpy as np

# Read image
org_img = cv2.imread("hough.jpg")
img = cv2.imread("hough.jpg", 0)

###<<<<<<-----------------------------Edge detection---------------------------->>>>>>######

largest = 255
smallest = 0
r,c = img.shape
print(img.shape)

count = 0

img1 = np.zeros(img.shape)
kernel = [[-1,-2,-1],[0,0,0],[1,2,1]] 

for x in range(1,r-1):
    for y in range(1,c-1): 
        img1[x][y]= img[x-1][y-1] * kernel[0][0] + \
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

for x in range(0,r):
    for y in range(0,c):
        img1[x][y] = (np.abs(img1[x][y]) / np.abs(largest))*255
        if (img1[x][y] > 180):
            img1[x][y] = 255
            count += 1
        else:
            img1[x][y] = 0

        
cv2.imwrite('edge.jpg', img1)

###<<<<<<-----------------------------create accumulator---------------------------->>>>>>######
 
# d = np.sqrt((r**2)+(c**2))
# d = int(d)

radi = 22

accumulator = np.zeros(img.shape)
print(accumulator.shape)


for a in range(0,r):
    for b in range(0,c):
        if (img1[a][b] == 255):
            for deg in range (0,360):
                row = int(a - radi*np.sin(np.deg2rad(deg)))
                col = int(b - radi*np.cos(np.deg2rad(deg)))
                accumulator[row][col] = accumulator[row][col]+1 
                    
cv2.imwrite("accumulator.jpg",accumulator)

###<<<<<<-----------------------------Circle detection---------------------------->>>>>>######

a = []
b = []

img2 = cv2.imread("hough.jpg", 0)
img3 = cv2.imread("hough.jpg")
r,c = img2.shape

for i in range (len(idx[0])):
    x = idx[0][i]
    y = idx[1][i]
    img3 =  cv2.circle(img3,(y,x), 20, (0,255,0), thickness=1, lineType=8, shift=0)

cv2.imwrite("circle.jpg", img3)