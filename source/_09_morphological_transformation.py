# Run command: python _09_morphological_transformation.py
# We are going to remove white noise
# There are 2 pairs on Morphological Transformations:
# 1. Erotion and Dilatation
#  Erotion --> using kernel/slider to erode the edge
#  Dilatation --> using kernel/slider to dilate the edge
# 2. Opening and Closing
#  Opening --> remove false positive (noise in the background)
#  Closing --> remove false negative (noise in the object)

# Further reading:
# https://docs.opencv.org/master/d9/d61/tutorial_py_morphological_ops.html

# Importing libraries as shortcut
import numpy as np
import cv2
# import matplotlib.pyplot as plt

# Get the video image from camera
#   `0` means camera #1
cap = cv2.VideoCapture(0)

# Set image size
#  Source: https://techoverflow.net/2018/12/18/how-to-set-cv2-videocapture-image-size/
# Set properties. Each returns == True on success (i.e. correct resolution)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 160)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 120)

# Looping the captures to get all images from camera
while 1:
    _, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Setup red color as target in HSV (Hue Saturation Value)
    #  What we see will be red color that is between the ranges 30-255, 150-255, and 50-180
    lower_red = np.array([30, 150, 50])
    upper_red = np.array([255, 255, 180])

    mask = cv2.inRange(hsv, lower_red, upper_red)
    result = cv2.bitwise_and(frame, frame, mask=mask)

    # 1. Erotion and Dilatation
    kernel = np.ones((5, 5), np.uint8)
    erosion = cv2.erode(mask, kernel, iterations=1)
    dilation = cv2.dilate(mask, kernel, iterations=1)

    # 2. Opening and Closing
    opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    closing = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)

    # Show results
    cv2.imshow('Original', frame)
    cv2.imshow('Mask', mask)
    cv2.imshow('Erosion', erosion)
    cv2.imshow('Dilation', dilation)
    cv2.imshow('Opening', opening)
    cv2.imshow('Closing', closing)

    # Wait until `Esc` key is pressed
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

    # Other alternative for pressing key
    #  If we use this the camera captures result per button click
    # cv2.waitKey(0)

# Close everything
cv2.destroyAllWindows()

# Stop video and Turn off camera
cap.release()
