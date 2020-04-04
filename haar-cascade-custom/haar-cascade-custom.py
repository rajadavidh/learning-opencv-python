# Run command: python haar-cascade-custom.py
# We detect faces and eyes
# Further reading:
# https://docs.opencv.org/master/db/d28/tutorial_cascade_classifier.html

# Notes from https://cvdazzle.com/
#  Much of the content here was developed for the haarcascade face detection algorithm,
#  which was widely used between 2010-2015 but has now been deprecated as
#  neural networks face detection algorithms have become more widespread.

# Importing libraries as shortcut
import cv2
# import matplotlib.pyplot as plt

# Multiple cascades:
# https://github.com/Itseez/opencv/tree/master/data/haarcascades

# Utilize Face cascade:
# https://github.com/Itseez/opencv/blob/master/data/haarcascades/haarcascade_frontalface_default.xml
face_cascade = cv2.CascadeClassifier('../cascade/haarcascade_frontalface_default.xml')

# Utilize Eye cascade:
# https://github.com/Itseez/opencv/blob/master/data/haarcascades/haarcascade_eye.xml
eye_cascade = cv2.CascadeClassifier('../cascade/haarcascade_eye.xml')

# Utilize Watch cascade we just made
watch_cascade = cv2.CascadeClassifier('../data/stage0.xml')

# Get the video image from camera
#   `0` means camera #1
cap = cv2.VideoCapture(0)
fgbg = cv2.createBackgroundSubtractorMOG2()

# Set image size
#  Source: https://techoverflow.net/2018/12/18/how-to-set-cv2-videocapture-image-size/
# Set properties. Each returns == True on success (i.e. correct resolution)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 160)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 120)

# Looping the captures to get all images from camera
while 1:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Detect watches
    #  This is custom Haar Cascade
    #  image, reject levels, level weights.
    watches = watch_cascade.detectMultiScale(gray, 50, 50)
    for (x, y, w, h) in watches:
        # cv2.rectangle(img, (x, y), (x + w, y + h), (255, 255, 0), 2)

        # Since the rectangle is small, we change it as text
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(img, 'Watch', (x - w, y - h), font, 0.5, (11, 255, 255), 2, cv2.LINE_AA)

    # Detect faces
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
        roi_gray = gray[y:y + h, x:x + w]
        roi_color = img[y:y + h, x:x + w]

        # In each face, detect eyes
        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)

    # Show results
    cv2.imshow('result', img)

    # Wait until `Esc` key is pressed
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

# Close everything
cv2.destroyAllWindows()

# Stop video and Turn off camera
cap.release()
