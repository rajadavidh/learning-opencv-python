# Run command: python _06_thresholding.py
# We practice thresholding using lowlight image
# What thresholding can do is convert everything to white or black, based on a threshold value.
# Let's say we want the threshold to be 125 (out of 255),
# then everything that was 125 and under would be converted to 0, or black.
# Everything above 125 would be converted to 255, or white

# Importing libraries as shortcut
import numpy as np
import cv2
# import matplotlib.pyplot as plt

# Show the image
# cv2.imshow('result', img)

# Wait until any key is pressed
cv2.waitKey(0)

# Close everything
cv2.destroyAllWindows()
