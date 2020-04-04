# Run command: python _07_color_filtering.py
# To filter the color, we need to convert the color to HSV (Hue Saturation Value)

# Importing libraries as shortcut
import numpy as np
import cv2
# import matplotlib.pyplot as plt

# Get the image from video
#   `0` means camera #1
cap = cv2.VideoCapture(0)

# Set image size
#  Source: https://techoverflow.net/2018/12/18/how-to-set-cv2-videocapture-image-size/
# Set properties. Each returns == True on success (i.e. correct resolution)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 160)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 120)

# Looping the captures to get all images from camera
while 1:
    # What is the purpose of the single underscore `_` variable in Python?
    #  It's just a variable name, and it's conventional in python to use _ for throwaway variables.
    #  It just indicates that the loop variable isn't actually used.
    #  The python interpreter stores the last expression value to the special variable called _ .
    #  The underscore _ is also used for ignoring the specific values
    #  Source:
    #  https://stackoverflow.com/questions/5893163/what-is-the-purpose-of-the-single-underscore-variable-in-python
    _, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Setup red color as target in HSV (Hue Saturation Value)
    #  What we see will be red color that is between the ranges 30-255, 150-255, and 50-180
    lower_red = np.array([30, 150, 50])
    upper_red = np.array([255, 255, 180])

    mask = cv2.inRange(hsv, lower_red, upper_red)
    result = cv2.bitwise_and(frame, frame, mask=mask)

    cv2.imshow('frame', frame)
    cv2.imshow('mask', mask)
    cv2.imshow('result', result)

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
