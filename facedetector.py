import cv2

# load some pre trained data on face data
face = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

## This is Picture

'''
# image to detect faces in
img = cv2.imread('download.jpeg')

# convert to greyscale
grayscaled_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# detect faces
face_coordinates = face.detectMultiScale(grayscaled_img)

# draw green rectangle around face hard coded
cv2.rectangle(img, (86, 21), (86+96, 21+96), (0,255,0), 2 )

# draw a green rectangle around face dynamically
(x, y, w, h) = face_coordinates[0]
cv2.rectangle(img, (x, y), (x+w, y+h), (0,255,0), 2 )

# show the location of face in image
# print(face_coordinates)

# this will show the image
cv2.imshow('Clever Programmer Face Detector', img)

# this will keep the image open till a key is pressed
cv2.waitKey()
'''

## This is Webacm

# To capture video from webcam
webcam = cv2.VideoCapture(0)

# Iterate forever over frames
while True:
    # read the current frame
    successful_frame_read, frame = webcam.read()
    
    # convert to greyscale
    grayscaled_img = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    
    # detect faces
    face_coordinates = face.detectMultiScale(grayscaled_img)

    # draw a green rectangle around face dynamically
    (x, y, w, h) = face_coordinates[0]
    cv2.rectangle(frame, (x, y), (x+w, y+h), (0,255,0), 2 )

    # this will show the image
    cv2.imshow('Clever Programmer Face Detector', frame)
    cv2.waitKey(1)
    
    


print('Code Completed')