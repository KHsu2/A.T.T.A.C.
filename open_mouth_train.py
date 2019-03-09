"""
Author      : Kevin Hsu
Description : Extract open_mouth frames using yawning_segments.txt which contains the manually labeled open-mouth frames
"""
import time
import os
import face_recognition as fr
from PIL import Image
import cv2
import re

def resize_image(image, frame_size):
	height, width, channel = image.shape
	x_scale = train_frame_size/width
	y_scale = train_frame_size/height
	resized_im = cv2.resize(im, (0,0), fx = x_scale, fy = y_scale)
	return resized_im

def draw_face_landmarks(image, face_landmarks):
	for landmarks in face_landmarks:
		for facial_feature in landmarks.keys():
			for counter in range(0, len(landmarks[facial_feature])):
				cv2.line(image, landmarks[facial_feature][counter], landmarks[facial_feature][counter+1], (255, 255, 0), 2)
	return image

def main() :

	#########################################################################
	################## Preparing Data for Training ##########################
	#########################################################################

	source_dir = "yawning_vids/YawDD_dataset/Frames_v1_2"
	output_dir = "yawning_vids/YawDD_dataset/Frames_v1_3"

	###### Extract Facial Landmarks #######
	im = cv2.imread(source_dir + "/open/face1.png")

	train_frame_size = 50
	im = cv2.imread(source_dir + "/open/face1.png")
	resized_im = resize_image(im, train_frame_size)
	cv2.imwrite(output_dir + "open/face1.png", resized_im)


if __name__ == "__main__" :
    main()
