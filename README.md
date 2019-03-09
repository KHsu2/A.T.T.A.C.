# A.T.T.A.C.
The Autonomous Tasty Treat Accelerator (A.T.T.A.C.) is a robot that will detect the face of a user and launch a tasty treat (Skittles) into their mouth when triggered by an open mouth for a duration of time

## Overview
### Facial Detection
The facial detection method is from Github User Adam Geitguy which uses the Histogram of Oriented Gradients method to detect faces, and Kazemi and Sullivan's method for extracting face landmarks. 

links: * https://github.com/ageitgey/face_recognition 
* https://medium.com/@ageitgey/machine-learning-is-fun-part-4-modern-face-recognition-with-deep-learning-c3cffc121d78

### Open-Mouth Classifier
* An online dataset of people yawning was used to train the open-mouth classifer
* The file open_mouth_frame_extraction.py is a script that uses ffmpeg to extract open-mouth and close-mouth frames from the video files, based on the hand-labeled sections in yawn_segments.txt.

Citation: S. Abtahi, M. Omidyeganeh, S. Shirmohammadi, and B. Hariri, “YawDD: A Yawning Detection Dataset”, Proc. ACM Multimedia Systems, Singapore, March 19 -21 2014.

## In Progress
### Models
* Convolutional Neural Network (CNN)
    * Input: n x n image of facial landmarks
* Fully Connected Neural Network (FCN)
    * Input: 38 facial landmark points
