import cv2
import numpy as np

# Read image
org_img = cv2.imread("hough.jpg")
img = cv2.imread("hough.jpg", 0)

###<<<<<<-----------------------------Edge detection---------------------------->>>>>>######

largest = 255
smallest = 0
r,c = img.shape

count = 0

img1 = np.zeros(img.shape)
kernel = [[-1,0,1],[-2,0,2],[-1,0,1]] 

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
        if (img1[x][y] > 80):
            img1[x][y] = 255
            count += 1
        else:
            img1[x][y] = 0

        
cv2.imwrite('edge.jpg', img1)

###<<<<<<-----------------------------create accumulator---------------------------->>>>>>######
 
d = np.sqrt((r**2)+(c**2))
d = int(d)

accumulator = np.zeros((d,360))

for x in range(0,r):
    for y in range(0,c):
        if (img1[x][y] == 255):
            for deg in range (-180,180):
                r = x*np.cos(np.deg2rad(deg)) + y*np.sin(np.deg2rad(deg))
                r = int(r)
                if (r > 0 and r < d):
                    accumulator[r][deg] = accumulator[r][deg]+1 
                    
cv2.imwrite("accumulator.jpg",accumulator)

###<<<<<<---------------------selecting highest voted points------------------------->>>>>>######

idx = np.unravel_index(np.argsort(accumulator.ravel())[-1000:], accumulator.shape)

###<<<<<<-----------------------------red lines detection---------------------------->>>>>>######

rho = []
theta = []

for i in range (len(idx[0])):
    x = idx[0][i]
    y = idx[1][i]
    if (y == 306):
        rho.append(x)
        theta.append(y)
    if (y == 126):
        rho.append(x)
        theta.append(y)
        
img2 = cv2.imread("hough.jpg", 0)
img3 = cv2.imread("hough.jpg")
r,c = img2.shape

x = []
y = []

for i in range (len(theta)):
    p = rho[i]
    q = theta[i]
    for i in range (r):
        k = (p-(i*np.cos(np.deg2rad(q))))/(np.sin(np.deg2rad(q)))
        if (k > 0 and k <= 666):
            x.append(i)
            y.append(int(k)) 
                
for i in range (len(x)):
    a = x[i]
    b = y[i]
    img3[a][b] = [0,255,0]

cv2.imwrite("blue_line.jpg", img3)

###<<<<<<-----------------------------red lines detection---------------------------->>>>>>######

rho = []
theta = []

idx = np.unravel_index(np.argsort(accumulator.ravel())[-1000:], accumulator.shape)

for i in range (len(idx[0])):
    x = idx[0][i]
    y = idx[1][i]
    if (y == 92):
        rho.append(x)
        theta.append(y)
        
img2 = cv2.imread("hough.jpg", 0)
img3 = cv2.imread("hough.jpg")
r,c = img2.shape

x = []
y = []

for i in range (len(theta)):
    p = rho[i]
    q = theta[i]
    for i in range (r):
        k = (p-(i*np.cos(np.deg2rad(q))))/(np.sin(np.deg2rad(q)))
        if (k > 0 and k <= 666):
            x.append(i)
            y.append(int(k)) 
                
for i in range (len(x)):
    a = x[i]
    b = y[i]
    img3[a][b] = [0,255,0]
    
cv2.imwrite("red_line.jpg", img3)