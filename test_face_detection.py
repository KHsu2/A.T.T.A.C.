"""
Author      : Kevin Hsu
Description : Testing face_detection
"""
import time
import face_recognition as fr
import matplotlib.pyplot as plt 
from PIL import Image
import cv2
#print(time.perf_counter())

def main() :
	#Assign filename from current directory
	#fileName = "Pictures/IMG-3473.jpg"
	fileName = "yawning_vids/YawDD_dataset/Frames_v1_1/1-FemaleNoGlasses-CloseMouth/frame1.png"

	#Load image
	image = fr.load_image_file(fileName)
	
	img = cv2.imread(fileName)
	small_img = cv2.resize(img, (0, 0), fx=0.25, fy=0.25)

	#Find faces in image. face_locations is a n long list, each element being 
	#4 coordinates of the top (y1), right (x1), bottom (y2), left (x2) corners 
	#of the bounding box
	start = time.time()
	face_locations = fr.face_locations(image)
	end = time.time()
	if face_locations:
		print("Normal scale face_location: " + str(end-start))

	start = time.time()
	face_locations_small = fr.face_locations(small_img)
	end = time.time()
	if face_locations_small:
		print("Down-scaled face_location: " + str(end-start))

	#print(time.perf_counter())

	#for fl in face_locations:
	#	top, right, bottom, left = fl
	#	face_image = image[top:bottom, left:right]
	#	pil_image = Image.fromarray(face_image)
	#	pil_image.show()

		#Bounding box
	#	rect = cv2.rectangle(image, (right, top), (left, bottom), (255, 255, 0), 2)
	#	pil_image = Image.fromarray(image)
	#	pil_image.show()

	for fls in face_locations_small:
		top, right, bottom, left = fls
		top *= 4
		right *= 4
		bottom *= 4
		left *= 4

		rect = cv2.rectangle(img, (right, top), (left, bottom), (255, 255, 0), 2)
		face_image = img[top:bottom, left:right]
		#cv2.imshow('Image', img)
		cv2.imshow('Image', face_image)
		cv2.waitKey(0)
		cv2.destroyAllWindows()
		cv2.imwrite('frame1.png', face_image)

	#print(time.perf_counter())
if __name__ == "__main__" :
    main()

