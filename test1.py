#! /usr/local/bin/python

import cv2
import numpy as np

def main():
	load()
	display()
	k = cv2.waitKey(0)
	if (k == ord('x')):
		print ("exiting and saving")
		cv2.destroyAllWindows()
		save()

def load():
	global img 
	img = cv2.imread("test_img.jpg", cv2.IMREAD_GRAYSCALE)
	cv2.imshow("hello", img)
	
def display():
	cv2.namedWindow('image', cv2.WINDOW_NORMAL)
	cv2.imshow('image',img)

def save():
	cv2.imwrite('test_img_gray.jpg', img)


if __name__ == "__main__":
    main()