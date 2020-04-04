# Run command: python _13_corner_detection.py
# The purpose of detecting corner is to track things like motion,
# do 3D modeling, and recognize objects, shapes, and characters
# Further reading:
# https://docs.opencv.org/master/d4/d8c/tutorial_py_shi_tomasi.html

# Importing libraries as shortcut
import numpy as np
import cv2
# import matplotlib.pyplot as plt

img = cv2.imread('../data/640px-Similar-geometric-shapes.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = np.float32(gray)  # We need to convert to float because `cv2.goodFeaturestoTrack` accepts only float values

# Detect corners
corners = cv2.goodFeaturesToTrack(gray, 100, 0.01, 10)

# Convert a numpy array to iterator
#  Source: https://stackoverflow.com/questions/54393177/convert-a-numpy-array-to-iterator
corners = iter(np.int0(corners))

# Make a circle at each point that is detected as a corner
for corner in corners:
    print(corner)
    x, y = corner.ravel()
    cv2.circle(img, (x, y), 3, 255, -1)

# Show the image
cv2.imshow('Corner', img)

# Wait until any key is pressed
cv2.waitKey(0)

# Close everything
cv2.destroyAllWindows()
