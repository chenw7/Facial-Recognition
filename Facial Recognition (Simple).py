#This program uses the face_recognition library and opencv library to identify faces stored by the user in the same folder as this program.
#Author @Wei-cen Chen
#Version March 21, 2022

#Importing the necessary libraries to run the program
import face_recognition
import cv2
import numpy as np

#Get video from default webcam
video_capture = cv2.VideoCapture(0)

#Load sample picture and learn to recognize
obama_image = face_recognition.load_image_file("obama.jpeg")
obama_face_encoding = face_recognition.face_encodings(obama_image)[0]

#Load second sample picture and learn to recognize
biden_image = face_recognition.load_image_file("biden.jpeg")
biden_face_encoding = face_recognition.face_encodings(biden_image)[0]

#Create array of known face encodings & corresponding names
known_face_encodings = [obama_face_encoding, biden_face_encoding]
known_face_names = ["Barack Obama", "Joe Biden"]

#Initialize variables and arrays to store variables in later
face_locations = []
face_encodings = []
face_names = []
process_this_frame = True

while True:
    #grab single frame of video
    ret, frame = video_capture.read()
    small_frame = cv2.resize(frame, (0,0), fx=0.25, fy=0.25)
    
    #convert image from BGR color to RGB color
    rgb_small_frame = small_frame[:, :, ::-1]
    
    #process less frames to save time
    if process_this_frame:
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)
        
        #compare faces captured in image to images stored in folder
        face_names =[]
        for face_encoding in face_encodings:
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
            name = "Unknown"
            
            #Using numpy to find the best match for identified faces
            face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
            best_match_index = np.argmin(face_distances)
            if matches[best_match_index]:
                name = known_face_names[best_match_index]
            
            face_names.append(name)
            
    process_this_frame = not process_this_frame
    
    #Display results
    for (top, right, bottom, left), name in zip(face_locations, face_names):
        top *=4
        right *=4
        bottom *=4
        left *=4
        
        #draw box around face
        cv2.rectangle(frame, (left, top), (right, bottom), (0,0, 255), 2)
        
        #label face with name
        cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0,0,255), cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)
        
    #display results    
    cv2.imshow('Video',frame)

    #type "q" to stop web cam execution
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

#release handle to webcam
video_capture.release()
cv2.destroyAllWindows()
