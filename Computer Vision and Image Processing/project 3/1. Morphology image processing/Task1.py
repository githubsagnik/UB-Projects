import cv2 as cv
import numpy as np

def dilation(org_img):
    
    r,c = org_img.shape
    img = np.zeros(org_img.shape)
    for i in range (1,(r-1)):
        for j in range (1,(c-1)):
            if (org_img[i][j] == 255):
                img[i-1][j]   = 255 
                img[i][j]     = 255 
                img[i+1][j]   = 255 
                img[i-1][j+1] = 255 
                img[i][j+1]   = 255 
                img[i+1][j+1] = 255
                img[i-1][j-1] = 255 
                img[i][j-1]   = 255 
                img[i+1][j-1] = 255
            
#     cv.imwrite('dilation.jpg', img) 
    return img
                 
def erosion(org_img):

    r,c = org_img.shape
    img = np.zeros(org_img.shape)
    for i in range (1,(r-1)):
        for j in range (1,(c-1)):
            if (org_img[i-1][j] == 255 and org_img[i][j] == 255 and org_img[i+1][j] == 255 and org_img[i-1][j+1] == 255 and
                org_img[i][j+1] == 255 and org_img[i+1][j+1] == 255 and org_img[i-1][j-1] == 255 and 
                org_img[i][j-1] == 255 and org_img[i+1][j-1] == 255):
                    
                    img[i][j]   = 255
                    
            else:
                img[i-1][j] = 0  
                img[i+1][j] = 0   
                img[i-1][j+1] = 0  
                img[i][j+1] = 0   
                img[i+1][j+1] = 0   
                img[i-1][j-1] = 0   
                img[i][j-1] = 0   
                img[i+1][j-1] = 0
                
#     cv.imwrite('erosion.jpg', img) 
    return img

###<<<<<<-----------------------Noise detection/ removal---------------------->>>>>>######

org_img    = cv.imread('noise.jpg',0)

opening_then_closing = erosion(org_img)
opening_then_closing = dilation(opening_then_closing)
opening_then_closing = dilation(opening_then_closing)
opening_then_closing = erosion(opening_then_closing)


closing_then_opening = dilation(org_img)
closing_then_opening = erosion(closing_then_opening)
closing_then_opening = erosion(closing_then_opening)
closing_then_opening = dilation(closing_then_opening)


cv.imwrite('res_noise1.jpg', opening_then_closing)
cv.imwrite('res_noise2.jpg', closing_then_opening)


###<<<<<<-------------------------Boundary detection------------------------>>>>>>######

img    = cv.imread('res_noise1.jpg',0)
img1 = dilation(img)
img2 = img1 - img
cv.imwrite('res_bound1.jpg', img2)

img    = cv.imread('res_noise2.jpg',0)
img1 = dilation(img)
img2 = img1 - img
cv.imwrite('res_bound2.jpg', img2)