# Run command: python _15_mog_background_reduction.py
# We are extracting the moving foreground from the static background

# Further reading:
# https://docs.opencv.org/master/d1/dc5/tutorial_background_subtraction.html

# Importing libraries as shortcut
# import numpy as np
import cv2
# import matplotlib.pyplot as plt

# Get the image from sample video
# cap = cv2.VideoCapture('people-walking.mp4')

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
    ret, frame = cap.read()

    fgmask = fgbg.apply(frame)

    # Show results
    cv2.imshow('fgmask', frame)
    cv2.imshow('frame', fgmask)

    # Wait until any key is pressed
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

# Close everything
cv2.destroyAllWindows()

# Stop video and Turn off camera
cap.release()
