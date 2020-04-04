# Run command: python _06_thresholding.py
# What thresholding can do is convert everything to white or black, based on a threshold value.
# Let's say we want the threshold to be 125 (out of 255),
# then everything that was 125 and under would be converted to 0, or black.
# Everything above 125 would be converted to 255, or white

# We implement thresholding using lowlight image of bookpage
# The purpose is to make that book page readable from human eye
# In this case, we practice 3 samples of thresholding: Simple, Adaptive, and Otsu
# We can use these techniques based on problem we want to solve

# Further reading:
# https://docs.opencv.org/master/d7/d4d/tutorial_py_thresholding.html

# Importing libraries as shortcut
# import numpy as np
import cv2
# import matplotlib.pyplot as plt

# Load lowlight image
img = cv2.imread('../data/bookpage.jpg')

# Apply simple threshold
retval, threshold = cv2.threshold(img, 12, 255, cv2.THRESH_BINARY)  # Value lower than 12 --> black

# Convert to greyscale from original image and Apply threshold
greyscaled = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
retval2, threshold2 = cv2.threshold(greyscaled, 12, 255, cv2.THRESH_BINARY)  # Value lower than 12 --> black

# Apply adaptive thresholding from greyscaled image
gaus = cv2.adaptiveThreshold(greyscaled, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 1)

# Apply Otsu's threshold. However the result will not well for this case.
retval3, otsu = cv2.threshold(greyscaled, 125, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

# Show the image
cv2.imshow('original', img)
cv2.imshow('threshold', threshold)
cv2.imshow('threshold from grayscale', threshold2)
cv2.imshow('adaptive threshold', gaus)
cv2.imshow('Otsu threshold', otsu)

# Wait until any key is pressed
cv2.waitKey(0)

# Close everything
cv2.destroyAllWindows()
