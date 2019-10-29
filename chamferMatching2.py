import cv2
import math
import numpy as np
from cv2 import imread
import statistics
from matplotlib import pyplot as plt


def extractBlack(image):
	red_part = cv2.inRange(image, np.array([0,0,0]), np.array([5,5,5]))
	return red_part
def extractWhite(image):
	red_part = cv2.inRange(image, np.array([250,250,250]), np.array([255,255,255]))
	return red_part
def mean (x,y):
	cX = (x[0]+y[0])/2
	cY = (x[1]+y[1])/2
	return (cX,cY)


img = cv2.imread("image_copy.png")
link1 = cv2.imread("link1.png")
link2 = cv2.imread("link2.png")
link3 = cv2.imread("link2.png")
black_image = extractBlack(img)
link1 = extractWhite(link1) #shape = (100,60)
link2 = extractWhite(link2) #shape = (100,60)
link3 = extractWhite(link3) #shape = (100,60)


#plt.subplot(131),plt.imshow(link1,cmap = 'gray')
#plt.title('LINK1'), plt.xticks([]), plt.yticks([])
#plt.subplot(132),plt.imshow(link2,cmap = 'gray')
#plt.title('LINK2'), plt.xticks([]), plt.yticks([])
#plt.subplot(133),plt.imshow(link3,cmap = 'gray')
#plt.title('LINK3'), plt.xticks([]), plt.yticks([])
#plt.show()
#cv2.imshow('LINK_OUTLINE',black_image)
#cv2.waitKey(2000)

yellow_center = (389, 543)
blue_center   = (308, 493)
green_center  = (231, 445)
red_center    = (151, 396)
link1_angle   = -2.5885612094391526
link2_angle   = 0.5574310915759405
link3_angle   = -2.5920326400634135
link1_center  = mean(yellow_center,blue_center)
link2_center  = mean(blue_center ,green_center)
link3_center  = mean(green_center,red_center)


