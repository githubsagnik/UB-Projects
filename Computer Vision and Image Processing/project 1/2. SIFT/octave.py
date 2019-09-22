import cv2
import numpy as np

img1 = cv2.imread("task2.jpg", 0)
cv2.imwrite("octave1.jpg",img1)
img = cv2.imread("octave1.jpg", 0)

cv2.imwrite("octave2.jpg",img1)


img = cv2.imread("octave2.jpg", 0)
i = 0
r,c = img.shape
r1 = int(r/2)
c1 = int(c/2)
img1 = np.zeros((r1,c1),float)
for x in range(0,r):
	if x%2 != 0:
		j = 0
		for y in range(0,c): 
			if y%2 != 0:
				img1[i][j] = img[x][y]
				j += 1
		i +=1
		
a,b = img1.shape
print(a,b)
cv2.imwrite("octave3.jpg",img1)

img = cv2.imread("octave3.jpg", 0)
i = 0
r,c = img.shape
r1 = int(r/2)
c1 = int(c/2)
img1 = np.zeros((r1,c1),float)
for x in range(0,r):
	if x%2 != 0:
		j = 0
		for y in range(0,c): 
			if y%2 != 0:
				img1[i][j] = img[x][y]
				j += 1
		i +=1
		
a,b = img1.shape
print(a,b)
cv2.imwrite("octave4.jpg",img1)