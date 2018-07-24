# Source: https://www.codingforentrepreneurs.com/blog/opencv-python-web-camera-quick-test/
# Run command: python test_webcam.py

# Importing libraries as shortcut
import numpy as np
import cv2
import matplotlib.pyplot as plt


# Setup webcam
cap = cv2.VideoCapture(0)

while True:
    # Capture frame-by-frame
    # "frame" will get the next frame in the camera (via "cap")
    # "ret" will obtain return value from getting the camera frame, either true of false
    # Source:
    # https://stackoverflow.com/questions/28773186/what-does-ret-and-frame-mean-here
    # https://docs.opencv.org/3.1.0/dd/d43/tutorial_py_video_display.html
    ret, frame = cap.read()

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Display the resulting frame
    cv2.imshow('frame', frame)
    cv2.imshow('gray', gray)
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
