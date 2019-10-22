import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('image_copy.png',0)
edges = cv2.Canny(img,100,200) # 800*800
dist = cv2.distanceTransform(edges, cv2.DIST_L1, 3) 
cv2.normalize(dist, dist, 0, 1.0, cv2.NORM_MINMAX) #Normalize the distance image for range = {0.0, 1.0}

plt.subplot(121),plt.imshow(dist,cmap = 'gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(edges,cmap = 'gray')
plt.title('Edge Image'), plt.xticks([]), plt.yticks([])

plt.show()

cv2.imshow('Distance Transform Image', dist)
cv2.waitKey(20000)
