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


# In this method you can focus on detecting the rotation of link 1
def detect(image, target, quadrant):
	# find the center of the link
	center = (yellow_center + blue_center) / 2

	# Isolate the region of interest in the thresholded image
	# (select an 160 by 160 window around the center of the link)
	mask = extractBlack(image)
	#cv2.imshow('LINK_OUTLINE',mask)
	ROI = mask[(center[1] - (target.shape[0] / 2)) : (center[1] + (target.shape[0] / 2)) + 1 , (center[0] - (target.shape[1] / 2)) : (center[0] + (target.shape[1] / 2)) + 1]
	#cv2.waitKey(2000)
	ROI = ROI[0:target.shape[0], 0:target.shape[1]]  # making sure it has the same size as the template
	
	# Apply the distance transform
	dist = cv2.distanceTransform(cv2.bitwise_not(ROI), cv2.DIST_L2, 0)

	# rotate the template by small step sizes around the angles that was already estimated from lab 1 and compare
	# it with the cropped image of the link
	sumlist = np.array([])
	step = 1  # degree increment in the search
	rows, cols = target.shape
	quadrant = quadrant - 90 # there is  90 degree difference between the robot frame and frame for rotating the
	# template
	angle_iteration = np.arange(quadrant[0], quadrant[1], step)
	for i in angle_iteration:
	  # Rotate the template to the desired rotation configuration
	  M = cv2.getRotationMatrix2D((cols / 2, rows / 2), i, 1)
	  # Apply rotation to the template
	  rotatedTemplate = cv2.warpAffine(target, M, (cols, rows))
	  # Combine the template and region of interest together to obtain only the values that are inside the template
	  img = dist * rotatedTemplate
	  # Sum the distances and append to the list
	  sumlist = np.append(sumlist, np.sum(img))


	# Once all configurations have been searched then select the one with the smallest distance and convert
	# to radians.
	return (angle_iteration[np.argmin(sumlist)] * np.pi) / 180.0

img = cv2.imread("image_copy.png")
link1 = cv2.imread("link1.png")
link2 = cv2.imread("link2.png")
link3 = cv2.imread("link2.png")
black_image = extractBlack(img)
link1 = extractWhite(link1) #shape = (100,60)
link2 = extractWhite(link2) #shape = (100,60)
link3 = extractWhite(link3) #shape = (100,60)



#cv2.imshow('LINK_OUTLINE',black_image)
#cv2.waitKey(2000)

yellow_center = np.array([389, 543])
blue_center   = np.array([308, 493])
green_center  = np.array([231, 445])
red_center    = np.array([151, 396])
link1_angle   = -2.5885612094391526
link2_angle   = 0.5574310915759405
link3_angle   = -2.5920326400634135
link1_center  = mean(yellow_center,blue_center)
link2_center  = mean(blue_center ,green_center)
link3_center  = mean(green_center,red_center)

print(detect(img, link1, [90,180]))

