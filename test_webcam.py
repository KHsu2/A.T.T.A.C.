"""
Author      : Kevin Hsu
Description : Testing webcam features
"""

import face_recognition as fr
import matplotlib.pyplot as plt 
from PIL import Image
import cv2

def main() :
	
	# Get a reference to webcam #0 (the default one)
	video_capture = cv2.VideoCapture(0)

	# Initialize some variables
	face_locations = []

	while True:
		# Grab a single frame of video
		ret, frame = video_capture.read()

    	# Resize frame of video to 1/4 size for faster face detection processing
		small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

		# Find all the faces and face encodings in the current frame of video
    	#face_locations = face_recognition.face_locations(small_frame, model="cnn")
		#face_locations = fr.face_locations(small_frame)
		#face_locations = fr.face_locations(frame, number_of_times_to_upsample = 2)
		face_locations = fr.face_locations(frame)

		face_landmarks_list = fr.face_landmarks(frame, face_locations=face_locations)

		for face_landmarks in face_landmarks_list:
			for facial_feature in face_landmarks.keys():
				for counter in range(0, len(face_landmarks[facial_feature])-1):
					cv2.line(frame, face_landmarks[facial_feature][counter], face_landmarks[facial_feature][counter+1], (255, 255, 0), 2)

    	# Display the results
		#for top, right, bottom, left in face_locations:
	        # Scale back up face locations since the frame we detected in was scaled to 1/4 size
			#top *= 4
			#right *= 4
			#bottom *= 4
			#left *= 4

			#rect = cv2.rectangle(frame, (right, top), (left, bottom), (255, 255, 0), 2)
			
        	# Extract the region of the image that contains the face
        	#face_image = frame[top:bottom, left:right]

        	# Blur the face image
        	#face_image = cv2.GaussianBlur(face_image, (99, 99), 30)

        	# Put the blurred face region back into the frame image
        	#frame[top:bottom, left:right] = face_image

    	# Display the resulting image
		cv2.imshow('Video', frame)

    	# Hit 'q' on the keyboard to quit!
		if cv2.waitKey(1) & 0xFF == ord('q'):
			break

	# Release handle to the webcam
	video_capture.release()
	cv2.destroyAllWindows()

if __name__ == "__main__" :
    main()
