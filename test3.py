#! /usr/local/bin/python

import cv2
import numpy as np
from matplotlib import pyplot as plt


def main():

	filename = 'detection_test.png'
	if filename is None:
		print "Error: Filename is wrong"
	else:
		global img 
		img= cv2.imread(filename)
		global gray
		gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

	options = 	{
			1 : harrisDetection,
			2 : shiTomasiDetection,
			3 : SIFTDetection,
			4 : SURFDetection,
			5 : FASTDetection
			}

	for key, val in options.items():
		print str(key)+ ": " + val.__name__
	choice = input("Pick Detection Type:")
	options[choice]()


	#####################
	#Detection Types Below#
	#####################
	
def harrisDetection():

	print "Harris Detection Selected."
	gray1 = np.float32(gray)
	dst = cv2.cornerHarris(gray1,2,3,0.04)

	#result is dilated for marking the corners, not important
	dst = cv2.dilate(dst,None)

	cv2.imshow('dst',dst)
	if cv2.waitKey(0) & 0xff == 27:
	    cv2.destroyAllWindows()

	# Threshold for an optimal value, it may vary depending on the image.
	img[dst>0.01*dst.max()]=[0,255,0]

	cv2.imshow('dst',img)
	if cv2.waitKey(0) & 0xff == 27:
	    cv2.destroyAllWindows()

def shiTomasiDetection():

	print "Shi-Tomasi Detection Selected."

	corners = cv2.goodFeaturesToTrack(gray,25,0.01,10)
	corners = np.int0(corners)

	for i in corners:
	    	x,y = i.ravel()
	    	cv2.circle(img,(x,y),3,255,-1)

	plt.imshow(img)
	plt.show()

def SIFTDetection():
	print "SIFT Detection Selected"

	sift = cv2.SIFT()
	kp = sift.detect(gray,None)

	img=cv2.drawKeypoints(gray,kp)

	cv2.imshow('dst',img)
	if cv2.waitKey(0) & 0xff == 27:
		cv2.destroyAllWindows()

def SURFDetection():
	print "SURF Detection Selected"
	#creation of the SURF object
	#the Hessian Threshold to 400
	surf = cv2.SURF(400)

	#find key points and descriptions directly 
	kp, des = surf.detectAndCompute(img,None)

	print (len(kp))

	while (len(kp) > 25):
		surf.hessianThreshold = surf.hessianThreshold + 500
		kp, des = surf.detectAndCompute(img,None)
		print (len(kp))

	surf.upright = True

	kp = surf.detect(img,None)
	img2 = cv2.drawKeypoints(img,kp,None,(0,255,0),4)

	cv2.imshow('dst',img2)
	if cv2.waitKey(0) & 0xff == 27:
		cv2.destroyAllWindows()

def FASTDetection():
	#initiate the FAST object with default values
	fast = cv2.FastFeatureDetector()

	#Find and draw out the key points
	kp = fast.detect(img,None)
	img2 = cv2.drawKeypoints(img, kp, color = (0, 255, 0))

	#print all default params
	print "Threshold: ", fast.getInt('threshold')
	print "nonmaxSuppression: ", fast.getBool('nonmaxSuppression')
	#print "neighborhood: ", fast.getInt('type')
	print "Total Keypoints with nonmaxSuppression: ", len(kp)

	cv2.imshow('dst',img2)
	if cv2.waitKey(0) & 0xff == 27:
		cv2.destroyAllWindows()

	#Disable nomaxSuppression
	fast.setBool('nonmaxSuppression',0)
	kp = fast.detect(img, None)

	img3  = cv2.drawKeypoints(img, kp, color = (0 , 0 ,255))

	print "Total Keypoints with maxSuppression: ", len(kp)

	cv2.imshow('dst',img3)
	if cv2.waitKey(0) & 0xff == 27:
		cv2.destroyAllWindows()



if __name__ == "__main__":
	main()
