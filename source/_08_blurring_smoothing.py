# Run command: python _08_blurring_smoothing.py
# We are going to reduce noise from color filtering
# Further reading:
# https://docs.opencv.org/master/d4/d13/tutorial_py_filtering.html

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

    # Blurring process
    blur = cv2.GaussianBlur(result, (15, 15), 0)
    median = cv2.medianBlur(result, 15)
    bilateral = cv2.bilateralFilter(result, 15, 75, 75)

    # Smoothing process
    #  We are averaging per block of pixels. In this example, we use 15x15 square which in total 225 squares
    kernel = np.ones((15, 15), np.float32) / 225
    smoothed = cv2.filter2D(result, -1, kernel)

    # Show results
    cv2.imshow('Original', frame)
    cv2.imshow('Result', result)
    cv2.imshow('Averaging', smoothed)
    cv2.imshow('Blur', blur)
    cv2.imshow('Median Blur', median)
    cv2.imshow('Bilateral Blur', bilateral)

    # Wait until any key is pressed
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
