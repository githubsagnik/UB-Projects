UBIT = 'sagnikgh';
import numpy as np;
np.random.seed(sum([ord(c) for c in UBIT]))
import cv2
import numpy as np
from matplotlib import pyplot as plt
from random import choices
##########################################PROBLEM 2.1####################################################
img1 = cv2.imread('tsucuba_left.png',0)
img2 = cv2.imread('tsucuba_right.png',0)
sift = cv2.xfeatures2d.SIFT_create()
kp1, des1 = sift.detectAndCompute(img1,None)
kp2, des2 = sift.detectAndCompute(img2,None)
img1 =

cv2.drawKeypoints(img1,kp1,None,flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
img2 =
cv2.drawKeypoints(img2,kp2,None,flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
bf = cv2.BFMatcher()
matches = bf.knnMatch(des1,des2, k=2)
good_match = []
for m,n in matches:
if m.distance < 0.75*n.distance:
good_match.append([m])
img3 =
cv2.drawMatchesKnn(img1,kp1,img2,kp2,good_match,None,flags=2)
cv2.imwrite('task2_sift1.jpg',img1)
cv2.imwrite('task2_sift2.jpg',img2)
cv2.imwrite('task2_matches_knn.jpg',img3)
##########################################PROBLEM 2.2, 2.3###############################################
img1 = cv2.imread('tsucuba_left.png',0)
img2 = cv2.imread('tsucuba_right.png',0)
sift = cv2.xfeatures2d.SIFT_create()
kp1, des1 = sift.detectAndCompute(img1,None)
kp2, des2 = sift.detectAndCompute(img2,None)
FLANN_INDEX_KDTREE = 0
index_params = dict(algorithm = FLANN_INDEX_KDTREE, trees = 5)
search_params = dict(checks=50)
flann = cv2.FlannBasedMatcher(index_params,search_params)
matches = flann.knnMatch(des1,des2,k=2)
good = []
pts1 = []
pts2 = []
pts11 = []
pts22 = []
for i,(m,n) in enumerate(matches):
if m.distance < 0.75*n.distance:
good.append(m)
pts2.append(kp2[m.trainIdx].pt)
pts1.append(kp1[m.queryIdx].pt)

pts1 = np.int32(pts1)
pts2 = np.int32(pts2)
F, mask = cv2.findFundamentalMat(pts1,pts2,cv2.FM_LMEDS)
with open('fundmentalmatrix.txt','w') as f:
for line in F:
np.savetxt(f, line, fmt='%.2f')
pts1 = pts1[mask.ravel()==1]
pts2 = pts2[mask.ravel()==1]
rnd = np.random.choice(len(pts1), 10)
pts11 = pts1[rnd]
pts22 = pts2[rnd]
def drawlines(img1,img2,lines,pts11,pts22,color):
r,c = img1.shape
img1 = cv2.cvtColor(img1,cv2.COLOR_GRAY2BGR)
img2 = cv2.cvtColor(img2,cv2.COLOR_GRAY2BGR)
for r,pt1,pt2,color in zip(lines,pts11,pts22,color):
x0,y0 = map(int, [0, -r[2]/r[1] ])
x1,y1 = map(int, [c, -(r[2]+r[0]*c)/r[1] ])
img1 = cv2.line(img1, (x0,y0), (x1,y1), color,1)
img1 = cv2.circle(img1,tuple(pt1),5,color,-1)
img2 = cv2.circle(img2,tuple(pt2),5,color,-1)
return img1,img2
lines1 = cv2.computeCorrespondEpilines(pts22.reshape(-1,1,2), 2,F)
lines1 = lines1.reshape(-1,3)
color = tuple(np.random.randint(0,255, size=(10, 3)).tolist())
img5,img6 = drawlines(img1,img2,lines1,pts11,pts22,color)
lines2 = cv2.computeCorrespondEpilines(pts11.reshape(-1,1,2), 1,F)
lines2 = lines2.reshape(-1,3)
img3,img4 = drawlines(img2,img1,lines2,pts22,pts11,color)
cv2.imwrite('task2_epi_left.jpg',img5)
cv2.imwrite('task2_epi_right.jpg',img3)
##########################################PROBLEM 2.4####################################################
imgL = cv2.imread('tsucuba_left.png',0)
imgR = cv2.imread('tsucuba_right.png',0)

window_size = 3
StereoMatcher = cv2.StereoSGBM_create(
minDisparity = 16,
numDisparities = 48,
blockSize = 9,
P1 = 8*3*window_size**2,
P2 = 32*3*window_size**2,
disp12MaxDiff = 1,
uniquenessRatio = 10,
speckleWindowSize = 50,
speckleRange = 32)
disparity = StereoMatcher.compute(imgL, imgR)
plt.imshow(disparity,'gray')
plt.savefig('task2_disparity.jpg')