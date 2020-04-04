# Run command: python _10_canny_edge.py
# Image gradients: To measure directional intensity
# Canny Edge: Find edges in image using Canny algorithm
# Further reading:
# https://docs.opencv.org/master/da/d22/tutorial_py_canny.html

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

    # Setup image gradients
    #  `cv2.CV_64F` is data type
    #  `ksize` is kernel size
    laplacian = cv2.Laplacian(frame, cv2.CV_64F)
    sobelx = cv2.Sobel(frame, cv2.CV_64F, 1, 0, ksize=5)
    sobely = cv2.Sobel(frame, cv2.CV_64F, 0, 1, ksize=5)

    # Edge detection
    edges = cv2.Canny(frame, 100, 200)

    # Show results
    cv2.imshow('Original', frame)
    cv2.imshow('Mask', mask)
    cv2.imshow('Laplacian', laplacian)
    cv2.imshow('Sobelx', sobelx)
    cv2.imshow('Sobely', sobely)
    cv2.imshow('Edges', edges)

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
