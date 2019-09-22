import cv2
import numpy as np
img = cv2.imread("task1.png", 0)
cv2.namedWindow('image', cv2.WINDOW_NORMAL)
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

largest = 255
smallest = 0
r,c = img.shape

img1 = [[0]*c for i in range(r)]
kernel = [[-1,-2,-1],[0,0,0],[1,2,1]] 

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
		img1[x][y] = np.abs(img1[x][y]) / np.abs(largest)


cv2.namedWindow('h_edge', cv2.WINDOW_NORMAL)
cv2.imshow('h_edge', np.asarray(img1))
cv2.waitKey(0)
cv2.destroyAllWindows()

kernel = [[-1,0,1],[-2,0,2],[-1,0,1]] 

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
		img1[x][y] = np.abs(img1[x][y]) / np.abs(largest)

cv2.namedWindow('v_edge', cv2.WINDOW_NORMAL)
cv2.imshow('v_edge', np.asarray(img1))
cv2.imwrite("v_edge.jpg",np.asarray(img1))
cv2.waitKey(0)
cv2.destroyAllWindows()

	
	
