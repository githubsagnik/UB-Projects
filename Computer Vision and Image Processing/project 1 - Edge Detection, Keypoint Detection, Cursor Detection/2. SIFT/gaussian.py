import cv2
import numpy as np
from math import exp

def gaussian(x, mu, sigma):       #Gaussian Kernel
  return exp( -(((x-mu)/(sigma))**2)/2.0 )

kernel_radius = 2				  #5*5 Gaussian Kernel
sigma = 0.70 					  #we have to manually enter the value of sigma

hkernel = [gaussian(x, kernel_radius, sigma) for x in range(2*kernel_radius+1)]
vkernel = [x for x in hkernel]
kernel = [[xh*xv for xh in hkernel] for xv in vkernel]

kernelsum = sum([sum(row) for row in kernel])
kernel = [[x/kernelsum for x in row] for row in kernel]

img = cv2.imread("octave1.jpg", 0)
cv2.namedWindow('image', cv2.WINDOW_NORMAL)
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

r,c = img.shape
img1 = np.zeros((r,c),np.float32)

for x in range(2,r-2):
	for y in range(2,c-2): 
		img1[x][y] = img[x-2][y-2] * kernel[0][0] + \
					 img[x-2][y-1] * kernel[0][1] + \
					 img[x-2][y] * kernel[0][2] + \
					 img[x-2][y+1] * kernel[0][3] + \
					 img[x-2][y+2] * kernel[0][4] + \
					 img[x-1][y-2] * kernel[1][0] + \
					 img[x-1][y-1] * kernel[1][1] + \
					 img[x-1][y] * kernel[1][2] + \
					 img[x-1][y+1] * kernel[1][3] + \
					 img[x-1][y+2] * kernel[1][4] + \
					 img[x][y-2] * kernel[2][0] + \
					 img[x][y-1] * kernel[2][1] + \
					 img[x][y] * kernel[2][2] + \
					 img[x][y+1] * kernel[2][3] + \
					 img[x][y+2] * kernel[2][4] + \
					 img[x+1][y-2] * kernel[3][0] + \
					 img[x+1][y-1] * kernel[3][1] + \
					 img[x+1][y] * kernel[3][2] + \
					 img[x+1][y+1] * kernel[3][3] + \
					 img[x+1][y+2] * kernel[3][4] + \
					 img[x+2][y-2] * kernel[4][0] + \
					 img[x+2][y-1] * kernel[4][1] + \
					 img[x+2][y] * kernel[4][2] + \
					 img[x+2][y+1] * kernel[4][3] + \
					 img[x+2][y+2] * kernel[4][4]
cv2.imwrite("octave1_1.jpg",img1)
exit()


  
  