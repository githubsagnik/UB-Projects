import cv2
import numpy as np

template = cv2.imread("template.jpg", cv2.IMREAD_GRAYSCALE)
for i in range (1,11): 
	img = cv2.imread("pos_"+str(i)+".jpg")
	gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	w, h = template.shape[::-1]	 
	result = cv2.matchTemplate(gray_img, template, cv2.TM_CCOEFF_NORMED)
	print(np.max(result))
	loc = np.where(result >= 0.8)
	 
	for pt in zip(*loc[::-1]):
		cv2.rectangle(img, pt, (pt[0] + w, pt[1] + h), (0, 255, 0), 3)	 
	cv2.imshow("img", img)
	cv2.waitKey(0)
	cv2.destroyAllWindows()
	
