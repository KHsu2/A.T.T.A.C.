"""
Author      : Kevin Hsu
Description : Extract open_mouth frames using yawning_segments.txt which contains the manually labeled open-mouth frames
"""
import time
import os
import ffmpy
import face_recognition as fr
import matplotlib.pyplot as plt 
from PIL import Image
import cv2
import re
from shutil import copyfile
import math

frameDir = "yawning_vids/YawDD_dataset/Frames_v1"

def convert2frames(directory) :
	vids = os.listdir(directory)
	for filename in vids:
		if (filename.endswith(".avi")):
			file = str.split(filename,".")
			os.mkdir(frameDir+"/"+file[0]+"-Mirror")
			os.system("ffmpeg -i {0} -f image2 -vf fps=fps=1 {1}".format(directory+"/"+filename, frameDir+"/"+file[0]+"-Mirror/output%d.png"))
		else:
			continue

def extract_segments(in_string, out_string, begin, end, fps):
	beg_time = time.strftime('%M:%S', time.gmtime(begin))
	end_time = time.strftime('%M:%S', time.gmtime(end))
	os.system("ffmpeg -i {0} -ss {1} -to {2} -f image2 -vf fps=fps={3} {4}".format(in_string, beg_time+'.400', end_time+'.600', fps, out_string))

#If frameNum is not in the segment specified by segEnds, then return true
def not_in_segment(frameNum, segEnds):
	if (int(segEnds[0]) <= frameNum and int(segEnds[1]) >= frameNum):
		return False
	else:
		return True

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

	#Convert video in directory to frames, 1 per second, for labeling
	#directory_female = "yawning_vids/YawDD_dataset/Dash/Female"
	#directory_male = "yawning_vids/YawDD_dataset/Dash/Male"
	#convert2frames(directory_female)
	#convert2frames(directory_male)

	#Extract frames that have open mouths
	#file = open("{0}/yawn_segments.txt".format(frameDir), "r")
	#lines = file.readlines(0)
	#for line in lines:
	#for line in lines[:1]:	#Run loop for first video
	#	splitLine = line.split()
	#	fem_male = splitLine[0].split("-")

		#########################################################################
		############# Extracting Open-Mouth Frames from videos ##################
		#########################################################################
		
		#Assign male and female directory
		#if "Fem" == fem_male[1][:3]:
			#directory = directory_female
		#Handling fixed filename errors
			#if "1" == fem_male[0]: #or "13" == fem_male[0] or "12" == fem_male[0]:
				#timeOpenMouth = splitLine[1].split(",")
				#for i in range(0, len(timeOpenMouth)):
					#segEnds = timeOpenMouth[i].split("-")
					#in_string = directory+"/"+splitLine[0]+".avi"
					#out_string = frameDir+"/"+splitLine[0]+"-OpenMouth/"+str(i)+"-frame%d.png"
					#extract_segments(in_string, out_string, int(segEnds[0])-1, int(segEnds[1])-1, 5)
		#elif "Mal" == fem_male[1][:3]:
			#directory = directory_male

		#Create directories for open mouth frames
		#timeOpenMouth = splitLine[1].split(",")
		#os.mkdir(frameDir+"/"+splitLine[0]+"-OpenMouth")

		#Extract  open mouth frames at 5 fps
		#for i in range(0, len(timeOpenMouth)):
			#segEnds = timeOpenMouth[i].split("-")
			#in_string = directory+"/"+splitLine[0]+".avi"
			#out_string = frameDir+"/"+splitLine[0]+"-OpenMouth/"+str(i)+"-frame%d.png"
			#extract_segments(in_string, out_string, int(segEnds[0])-1, int(segEnds[1])-1, 5)

		#########################################################################
		################## Isolating Closed-Mouth Frames ########################
		#########################################################################

		#v1_2_frame_dir = "yawning_vids/YawDD_dataset/Frames_v1_1/"+splitLine[0]+"-CloseMouth"
		#os.mkdir(v1_2_frame_dir)
		#timeOpenMouth = splitLine[1].split(",")
		#segEnds = list()
		#for numSegs in range(0, len(timeOpenMouth)):
		#	segEnds.append(timeOpenMouth[numSegs].split("-"))

		#file_names = os.listdir(frameDir+"/"+splitLine[0])
		#counter = 1;
		#for output_num in file_names:
		#	frameNum = re.findall(r'\d+', output_num)
		#	frameNum = int(frameNum[0])

			#Handling videos having varying number of closed mouth segments
		#	if numSegs == 0:
		#		if not_in_segment(frameNum, segEnds[0]):
		#			copyfile(frameDir+"/"+splitLine[0]+"/"+output_num ,v1_2_frame_dir+"/frame{0}.png".format(counter))
		#			counter += 1
		#	elif numSegs == 1:
		#		if not_in_segment(frameNum, segEnds[0]) and not_in_segment(frameNum, segEnds[1]):
		#			copyfile(frameDir+"/"+splitLine[0]+"/"+output_num ,v1_2_frame_dir+"/frame{0}.png".format(counter))
		#			counter += 1
		#	elif numSegs == 2:
		#		if not_in_segment(frameNum,segEnds[0]) and not_in_segment(frameNum,segEnds[1]) and not_in_segment(frameNum, segEnds[2]):
		#			copyfile(frameDir+"/"+splitLine[0]+"/"+output_num ,v1_2_frame_dir+"/frame{0}.png".format(counter))
		#			counter += 1
		#	elif numSegs == 3:
		#		if not_in_segment(frameNum,segEnds[0]) and not_in_segment(frameNum,segEnds[1]) and not_in_segment(frameNum, segEnds[2]) and not_in_segment(frameNum, segEnds[3]):
		#			copyfile(frameDir+"/"+splitLine[0]+"/"+output_num ,v1_2_frame_dir+"/frame{0}.png".format(counter))
		#			counter += 1

	file.close()
		#########################################################################
		########################## Extracting Faces #############################
		#########################################################################
	#Input directory
	frames_v1_1_dir = "yawning_vids/YawDD_dataset/Frames_v1_1"

	#directories = os.listdir(frames_v1_1_dir)
	#open_counter = 1
	#close_counter = 1

	#for directory in directories:
	#	splitLine = directory.split("-")
	#	if splitLine[2] == "CloseMouth":
	#		open_close = "close"
	#	elif splitLine[2] == "OpenMouth":
	#		open_close = "open"

		#Outputs to either open directory or close directory
	#	out_dir = "yawning_vids/YawDD_dataset/Frames_v1_2/" + open_close
	#	images = os.listdir(frames_v1_1_dir + "/" + directory)
	#	for image in images:
	#		im = cv2.imread(frames_v1_1_dir + "/" + directory + "/" + image)

			#Down-sample image to speed up facial detection
	#		small_im = cv2.resize(im, (0, 0), fx=0.25, fy=0.25)
	#		face_locations = fr.face_locations(small_im)

			## If a face is detected
	#		if face_locations:
	#			top, right, bottom, left = face_locations[0]
				
				#Resize
	#			top *= 4
	#			right *= 4
	#			bottom *= 4
	#			left *= 4

	#			face_image = im[top:bottom, left:right]
	#			if open_close == "close":
	#				cv2.imwrite(out_dir + "/face{0}.png".format(close_counter), face_image)
	#				close_counter += 1
	#			else:
	#				cv2.imwrite(out_dir + "/face{0}.png".format(open_counter), face_image)
	#				open_counter += 1
	#		else: 

	#			print(directory + "/" + image)

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
