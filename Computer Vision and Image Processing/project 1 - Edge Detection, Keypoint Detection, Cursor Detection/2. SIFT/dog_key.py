#########################################################GENERATE Dog IMAGE FROM BLURED IMAGES############################################################################################################################################
import cv2
import numpy as np
img = cv2.imread("octave1.jpg", 0)
										
for i in range (1,5):	
	octave1_1 = cv2.imread("octave"+str(i)+"_1.jpg", 0)
	octave1_2 = cv2.imread("octave"+str(i)+"_2.jpg", 0)
	octave1_3 = cv2.imread("octave"+str(i)+"_3.jpg", 0)
	octave1_4 = cv2.imread("octave"+str(i)+"_4.jpg", 0)
	octave1_5 = cv2.imread("octave"+str(i)+"_5.jpg", 0)

	r,c = octave1_1.shape
	dog1 = dog2 = dog3 = dog4 = np.zeros((r,c),int)

	for x in range(1,r-1):
		for y in range(1,c-1): 
			dog1[x][y] = octave1_1[x][y] - octave1_2[x][y]
			dog2[x][y] = octave1_2[x][y] - octave1_3[x][y]
			dog3[x][y] = octave1_3[x][y] - octave1_4[x][y]
			dog4[x][y] = octave1_4[x][y] - octave1_5[x][y]
			
	key1 = "key"+str(i)+"_1.jpg"
	key2 = "key"+str(i)+"_2.jpg"

	genkey1(dog1,dog2,dog3,dog4,key1,key2)

	cv2.imwrite("dog"+str(i)+"_1.jpg",dog1)
	cv2.imwrite("dog"+str(i)+"_2.jpg",dog2)
	cv2.imwrite("dog"+str(i)+"_3.jpg",dog3)
	cv2.imwrite("dog"+str(i)+"_4.jpg",dog4)
	
############################################################DETECT KEYS FROM THE DoG VALUES############################################################################################################################################
def genkey1(dog1,dog2,dog3,dog4,key1,key2):
	dog1 = dog1
	r,c = dog1.shape
	dog2 = dog2
	dog3 = dog3
	dog4 = dog4
	key1 = key1
	key2 = key2
	for x in range(1,r-1):
			for y in range(1,c-1): 
				if(dog2[x][y] > 1):
					print(dog2[x][y])
					if (dog2[x][y] > dog2[x-1][y-1]  and dog2[x][y] > dog2[x-1][y] and dog2[x][y] > dog2[x-1][y+1] and
					dog2[x][y] > dog2[x][y-1] and dog2[x][y] > dog2[x][y+1] and dog2[x][y] > dog2[x+1][y-1] and 
					dog2[x][y] > dog2[x+1][y] and dog2[x][y] > dog2[x+1][y+1]):
							if (dog2[x][y] > dog1[x-1][y-1]  and dog2[x][y] > dog1[x-1][y] and dog2[x][y] > dog1[x-1][y+1]
							and dog2[x][y] > dog1[x][y-1] and dog2[x][y] > dog1[x][y] and dog2[x][y] > dog1[x][y+1] and 
							dog2[x][y] > dog1[x+1][y-1] and dog2[x][y] > dog1[x+1][y] and dog2[x][y] > dog1[x+1][y+1]):
									if (dog2[x][y] > dog3[x-1][y-1]  and dog2[x][y] > dog3[x-1][y] and dog2[x][y] > dog3[x-1][y+1]
									and dog2[x][y] > dog3[x][y-1] and dog2[x][y] > dog3[x][y] and dog2[x][y] > dog3[x][y+1] and 
									dog2[x][y] > dog3[x+1][y-1] and dog2[x][y] > dog3[x+1][y] and dog2[x][y] > dog3[x+1][y+1]):
												dog2[x][y] = 255											
					if (dog2[x][y] < dog2[x-1][y-1]  and dog2[x][y] < dog2[x-1][y] and dog2[x][y] < dog2[x-1][y+1] and 
					dog2[x][y] < dog2[x][y-1] and dog2[x][y] < dog2[x][y+1] and dog2[x][y] < dog2[x+1][y-1] and 
					dog2[x][y] < dog2[x+1][y] and dog2[x][y] < dog2[x+1][y+1]):
							if (dog2[x][y] < dog1[x-1][y-1]  and dog2[x][y] < dog1[x-1][y] and dog2[x][y] < dog1[x-1][y+1] and
							dog2[x][y] < dog1[x][y-1] and dog2[x][y] < dog1[x][y] and dog2[x][y] < dog1[x][y+1] and 
							dog2[x][y] < dog1[x+1][y-1] and dog2[x][y] < dog1[x+1][y] and dog2[x][y] < dog1[x+1][y+1]):
									if (dog2[x][y] < dog3[x-1][y-1]  and dog2[x][y] < dog3[x-1][y] and dog2[x][y] < dog3[x-1][y+1] 
									and dog2[x][y] < dog3[x][y-1] and dog2[x][y] < dog3[x][y] and dog2[x][y] < dog3[x][y+1] and 
									dog2[x][y] < dog3[x+1][y-1] and dog2[x][y] < dog3[x+1][y] and dog2[x][y] < dog3[x+1][y+1]):
												dog2[x][y] = 255	
	cv2.imwrite(key1,dog2)	
	for x in range(1,r-1):
			for y in range(1,c-1):
				if(dog3[x][y] > 1):
					print(dog3[x][y])
					if (dog3[x][y] > dog3[x-1][y-1]  and dog3[x][y] > dog3[x-1][y] and dog3[x][y] > dog3[x-1][y+1]
					and dog3[x][y] > dog3[x][y-1]and dog3[x][y] > dog3[x][y+1] and dog3[x][y] > dog3[x+1][y-1] and 
					dog3[x][y] > dog3[x+1][y] and dog3[x][y] > dog3[x+1][y+1]):
							if (dog3[x][y] > dog2[x-1][y-1]  and dog3[x][y] > dog2[x-1][y] and dog3[x][y] > dog2[x-1][y+1]
							and dog3[x][y] > dog2[x][y-1] and dog2[x][y] > dog1[x][y] and dog2[x][y] > dog1[x][y+1] and 
							dog3[x][y] > dog2[x+1][y-1] and dog3[x][y] > dog2[x+1][y] and dog3[x][y] > dog2[x+1][y+1]):
									if (dog3[x][y] > dog4[x-1][y-1]  and dog3[x][y] > dog4[x-1][y] and dog3[x][y] > dog4[x-1][y+1]
									and dog3[x][y] > dog4[x][y-1] and dog3[x][y] > dog4[x][y] and dog3[x][y] > dog4[x][y+1] and 
									dog3[x][y] > dog4[x+1][y-1] and dog3[x][y] > dog4[x+1][y] and dog3[x][y] > dog4[x+1][y+1]):
												dog3[x][y] = 255
					if (dog3[x][y] < dog3[x-1][y-1]  and dog3[x][y] < dog3[x-1][y] and dog3[x][y] < dog3[x-1][y+1] and
					dog3[x][y] < dog3[x][y-1] and dog3[x][y] < dog3[x][y+1] and dog3[x][y] < dog3[x+1][y-1] and 
					dog3[x][y] < dog3[x+1][y] and dog3[x][y] < dog3[x+1][y+1]):
							if (dog3[x][y] < dog2[x-1][y-1]  and dog3[x][y] < dog2[x-1][y] and dog3[x][y] < dog2[x-1][y+1] and
							dog3[x][y] < dog2[x][y-1] and dog2[x][y] < dog1[x][y] and dog2[x][y] < dog1[x][y+1] and 
							dog3[x][y] < dog2[x+1][y-1] and dog3[x][y] < dog2[x+1][y] and dog3[x][y] < dog2[x+1][y+1]):
									if (dog3[x][y] < dog4[x-1][y-1]  and dog3[x][y] < dog4[x-1][y] and dog3[x][y] < dog4[x-1][y+1]
									and dog3[x][y] < dog4[x][y-1] and dog3[x][y] < dog4[x][y] and dog3[x][y] < dog4[x][y+1] and 
										dog3[x][y] < dog4[x+1][y-1] and dog3[x][y] < dog4[x+1][y] and dog3[x][y] < dog4[x+1][y+1]):
												dog3[x][y] = 255
	cv2.imwrite(key2,dog3)
################################################PLACE KEYS ON THE ORIGINAL IMAGE##################################################################################################################################################

img = cv2.imread("task2.jpg")

for i in range (1,5):
	key1_1 = cv2.imread("key"+str(i)+"_1.jpg", 0)
	key1_2 = cv2.imread("key"+str(i)+"_2.jpg", 0)
	
	r,c = key1_1.shape
	for x in range(1,r-1):
		for y in range(1,c-1): 
			if(key1_1[x][y] == 255):
				if(i == 1):
					img[x][y] = 255
				elif(i == 2):
					img[x*2][y*2] = 255
				elif(i == 3):
					img[x*4][y*4] = 255
				elif(i == 4):
					img[x*8][y*8] = 255
			if(key1_1[x][y] == 255):
				if(i == 1):
					img[x][y] = 255
				elif(i == 2):
					img[x*2][y*2] = 255
				elif(i == 3):
					img[x*4][y*4] = 255
				elif(i == 4):
					img[x*8][y*8] = 255
		
cv2.imwrite("super.jpg",img)
	