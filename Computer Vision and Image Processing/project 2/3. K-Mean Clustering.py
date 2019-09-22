UBIT = 'sagnikgh';
import numpy as np;
np.random.seed(sum([ord(c) for c in UBIT]))
from copy import deepcopy
import math
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from copy import deepcopy
import cv2
plt.rcParams['figure.figsize'] = (16, 9)
plt.style.use('ggplot')
##########################################PROBLEM 3.1, 3.2, 3.3##########################################

k=3
fig = plt.figure()
ax = fig.add_subplot(111)
def dist(a, b, ax=1):
return np.linalg.norm(a - b, axis=ax)
f1 = [5.9,4.6,6.2,4.7,5.5,5.0,4.9,6.7,5.1,6.0]
f2 = [3.2,2.9,2.8,3.2,4.2,3.0,3.1,3.1,3.8,3.0]
X = np.array(list(zip(f1, f2)))
C_x = [6.2,6.6,6.5]
C_y = [3.2,3.7,3.0]
C = np.array(list(zip(C_x, C_y)))
plt.scatter(f1, f2, s=80, facecolors='none', edgecolors='b', marker="^")
plt.scatter(C_x, C_y, color=['red','green','blue'])
for xy in zip(f1, f2):
ax.annotate('(%s, %s)' % xy, xy=xy, textcoords='data')
for xy in zip(C_x, C_y):
ax.annotate('(%s, %s)' % xy, xy=xy, textcoords='data')
plt.savefig('task3_iter0.jpg')
plt.show()
dis = []
cluster_red = []
cluster_green = []
cluster_blue = []
c_r_new = []
c_g_new = []
c_b_new = []
for m in range(k):
for i in range(len(X)):
for j in range(len(C)):
d = (X[i][0]-C[j][0])**2 + (X[i][1]-C[j][1])**2
dd = math.sqrt(d)
dis.append(dd)
if(dis.index(min(dis)) == 0):
cluster_red.append(X[i])
elif(dis.index(min(dis)) == 1):
cluster_green.append(X[i])
elif(dis.index(min(dis)) == 2):
cluster_blue.append(X[i])

dis = []
cluster_red = np.array(cluster_red)
cluster_green = np.array(cluster_green)
cluster_blue = np.array(cluster_blue)
c_x = sum(cluster_red[:,0])/len(cluster_red)
c_r_new.append(c_x)
c_y = sum(cluster_red[:,1])/len(cluster_red)
c_r_new.append(c_y)
c_x = sum(cluster_green[:,0])/len(cluster_green)
c_g_new.append(c_x)
c_y = sum(cluster_green[:,1])/len(cluster_green)
c_g_new.append(c_y)
c_x = sum(cluster_blue[:,0])/len(cluster_blue)
c_b_new.append(c_x)
c_y = sum(cluster_blue[:,1])/len(cluster_blue)
c_b_new.append(c_y)
C = []
C = [c_r_new,c_g_new,c_b_new]
C = np.array(C)
C_x = C[:,0]
C_y = C[:,1]
r_x = cluster_red[:,0]
r_y = cluster_red[:,1]
plt.scatter(r_x, r_y, s=80, facecolors='r', edgecolors='r', marker="^")
g_x = cluster_green[:,0]
g_y = cluster_green[:,1]
plt.scatter(g_x, g_y, s=80, facecolors='g', edgecolors='g', marker="^")
b_x = cluster_blue[:,0]
b_y = cluster_blue[:,1]
plt.scatter(b_x, b_y, s=80, facecolors='b', edgecolors='b', marker="^")
plt.scatter(C_x, C_y, color=['red','green','blue'])
plt.savefig('task3_iter'+str(m+1)+'.jpg')
plt.show()
cluster_red = []
cluster_green = []
cluster_blue = []
c_r_new = []
c_g_new = []
c_b_new = []
##########################################PROBLEM 3.4####################################################
k = 5

c = 3
image = cv2.imread('baboon.jpg')
image_new = np.zeros(image.shape)
rep_mat = np.zeros((image.shape[0],image.shape[1]))
clus = [[[0,0,0],[0,0,0],[0,0,0]]]*c
centroid = np.random.randint(0,255, size=(c, 3))
dm = []
for n in range(k):
print(n)
for i in range (len(image)):
for j in range(len(image)):
for k in range (len(centroid)):
d = (image[i][j]-centroid[k])
d = math.sqrt(d[0]**2 + d[1]**2 + d[2]**2)
dm.append(d)
x = dm.index(min(dm))
rep_mat[i][j] = x
clus[x].append(image[i][j])
dm = []
for m in range(len(centroid)):
centroid[m] = np.mean(clus[m], axis=0)
for i in range(len(image_new)):
for j in range(len(image_new)):
z = int(rep_mat[i][j])
image_new[i][j] = centroid[z]
cv2.imwrite('task3_baboon_'+str(k)+'.jpg',image_new)