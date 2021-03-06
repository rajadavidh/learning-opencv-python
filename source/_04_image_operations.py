# Run command: python _04_image_operations.py
# Further reading:
# https://docs.opencv.org/master/d3/df2/tutorial_py_basic_ops.html

# Importing libraries as shortcut
# import numpy as np
import cv2
# import matplotlib.pyplot as plt

# Load the image and covert to greyscale color
img = cv2.imread('../data/fisher-anyer-beach-2016-raja-david.jpg', cv2.IMREAD_COLOR)

# Reference specific pixels
# px = img[55, 55]
# print(px)  # produce actual color for specific pixel

# Modify specific pixel color value
img[55, 55] = [255, 0, 255]
px = img[55, 55]
print(px)

# Reference ROI (Region of Image)
# roi = img[0:100, 100:150]
# print(roi)

# Modify ROI color value
img[100:200, 100:150] = [255, 0, 255]

# Get cropped area
cropped_area = img[290:350, 250:330]
img[0:60, 0:80] = cropped_area

# Show the image
cv2.imshow('Image', img)

# Wait until any key is pressed
cv2.waitKey(0)

# Close everything
cv2.destroyAllWindows()
