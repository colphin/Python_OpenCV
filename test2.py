#! /usr/local/bin/python

import sys
import numpy as np
import cv2

def main():

	e1 = cv2.getTickCount()

	#Loading the images
	img1 = load("test_img1.jpg")
	img2 = load("test_img2.jpg")

	#checking if they exist
	if img1 is None:
		print "Error: Img1 does not exist"
		sys.exit()
	if img2 is None:
		print "Error: Img2 does not exist"
		sys.exit()


	img1Height, img1Width = getDimension(img1)
	img2Height, img2Width = getDimension(img2)

	img1Crop = crop(img1,25,325,100,300);

	e2 = cv2.getTickCount()
	time = (e2-e1)/cv2.getTickFrequency()
	print str(time) +  " seconds"


	#addColorBar()
	cv2.imshow("IMAGE_1",img1)
	k = cv2.waitKey(0)
	if (k == ord(' ')):
		print ("exiting")
		cv2.destroyAllWindows()
	cv2.imshow("IMAGE_2",img1Crop)
	k = cv2.waitKey(0)
	if (k == ord(' ')):
		print ("exiting")
		cv2.destroyAllWindows()



def  load(name): 
	img = cv2.imread(name, 1)
	#cv2.imshow("hello", img)
	return img

def crop(image, int1, int2, int3, int4):
	#face  = img[25:325:3, 100:300:3]
	result = image[int1:int2, int3:int4]
	return result


def getDimension(image):
	height, width, depth = image.shape
	print (height, width, depth) 
	return height, width

def addColorBar(image):
	for i in range(0, height/4):
		for j in range (0, width):
			image[i,j] = [0,255,0];

if __name__ == "__main__":
	main()