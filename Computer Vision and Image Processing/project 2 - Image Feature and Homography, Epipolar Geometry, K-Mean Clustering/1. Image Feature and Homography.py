UBIT = 'sagnikgh'
import numpy as np
np.random.seed(sum([ord(c) for c in UBIT]))
import numpy as np
import sys
import cv2
import numpy as np
from matplotlib import pyplot as plt
import random
##########################################PROBLEM 1.1, 1.2, 1.4##########################################
img1 = cv2.imread('mountain1.jpg',0)
img2 = cv2.imread('mountain2.jpg',0)
sift = cv2.xfeatures2d.SIFT_create()
kp1, des1 = sift.detectAndCompute(img1,None)
kp2, des2 = sift.detectAndCompute(img2,None)

kp1 = sift.detect(img1,None)
kp2 = sift.detect(img2,None)
img1 =
cv2.drawKeypoints(img1,kp1,None,flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
img2 =
cv2.drawKeypoints(img2,kp2,None,flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
bf = cv2.BFMatcher()
matches = bf.knnMatch(des1,des2, k=2)
good_match= []
gm_random = []
for m,n in matches:
if m.distance < 0.75*n.distance:
good_match.append([m])
gm_random = random.sample(good_match, 10)
img4=cv2.drawMatchesKnn(img1,kp1,img2,kp2,gm_random,None,flags=2)
img3=cv2.drawMatchesKnn(img1,kp1,img2,kp2,good_match,None,flags=2)
cv2.imwrite('task1_sift1.jpg',img1)
cv2.imwrite('task1_sift2.jpg',img2)
cv2.imwrite('task1_matches_knn.jpg',img3)
cv2.imwrite('task1_matches.jpg.jpg',img4)
##########################################PROBLEM 1.3, 1.5###############################################
def get_stitched_image(img1, img2, M):
w1,h1 = img1.shape[:2]
w2,h2 = img2.shape[:2]
img1_dims =
np.float32([ [0,0], [0,w1], [h1, w1], [h1,0] ]).reshape(-1,1,2)
img2_dims_temp =
np.float32([ [0,0], [0,w2], [h2, w2], [h2,0] ]).reshape(-1,1,2)
img2_dims = cv2.perspectiveTransform(img2_dims_temp, M)
result_dims = np.concatenate( (img1_dims, img2_dims), axis = 0)

[x_min, y_min] = np.int32(result_dims.min(axis=0).ravel() - 0.5)
[x_max, y_max] = np.int32(result_dims.max(axis=0).ravel() + 0.5)
transform_dist = [-x_min,-y_min]
transform_array =
np.array([[1, 0, transform_dist[0]], [0, 1, transform_dist[1]], [0,0,1]])
result_img = cv2.warpPerspective
(img2, transform_array.dot(M), (x_max-x_min, y_max-y_min))
result_img[transform_dist[1]:w1+transform_dist[1],
transform_dist[0]:h1+transform_dist[0]] = img1
return result_img
def get_sift_homography(img1, img2):
sift = cv2.xfeatures2d.SIFT_create()
k1, d1 = sift.detectAndCompute(img1, None)
k2, d2 = sift.detectAndCompute(img2, None)
bf = cv2.BFMatcher()
matches = bf.knnMatch(d1,d2, k=2)
good_match = []
for m1,m2 in matches:
if m1.distance < 0.75 * m2.distance:
good_match.append(m1)
min_matches = 8
if len(good_match) > min_matches:
img1_pts = []
img2_pts = []
for match in good_match:
img1_pts.append(k1[match.queryIdx].pt)
img2_pts.append(k2[match.trainIdx].pt)
img1_pts = np.float32(img1_pts).reshape(-1,1,2)
img2_pts = np.float32(img2_pts).reshape(-1,1,2)
M, mask = cv2.findHomography(img1_pts, img2_pts, cv2.RANSAC, 5.0)
return M

else:
print ('Error: Not enough matches')
exit()
def main():
img1 = cv2.imread('mountain1.jpg',0)
img2 = cv2.imread('mountain2.jpg',0)
M = get_sift_homography(img1, img2)
with open('homographymatrix.txt','w') as f:
for line in M:
np.savetxt(f, line, fmt='%.2f')
result_image = get_stitched_image(img2, img1, M)
cv2.imwrite('task1_pano.jpg',result_image)
if __name__=='__main__':
main()