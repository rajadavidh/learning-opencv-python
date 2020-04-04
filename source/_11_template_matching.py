# Run command: python _11_template_matching.py
# We are going to implement basic object recognition by
# finding identical regions of an image that match a template we provide
# Further reading:
# https://docs.opencv.org/master/d4/dc6/tutorial_py_template_matching.html

# Importing libraries as shortcut
import numpy as np
import cv2
# import matplotlib.pyplot as plt

# Converting image to greyscale
img_rgb = cv2.imread('../data/fisher-anyer-beach-2016-raja-david.jpg')
img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)

# template = cv2.imread('../data/palm-tree-pattern.png', 0)
template = cv2.imread('../data/palm-tree-pattern.jpg', 0)
width, height = template.shape[::-1]

# Load the template
result = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)

# Search the template pattern with 80% match
threshold = 0.8
loc = np.where(result >= threshold)

# Mark all the matches with yellow box
#  Read more about zip function: https://realpython.com/python-zip-function/
for point in zip(*loc[::-1]):
    cv2.rectangle(img_rgb, point, (point[0] + width, point[1] + height), (0, 255, 255), 2)

# Show the image
cv2.imshow('Detected', img_rgb)

# Wait until any key is pressed
cv2.waitKey(0)

# Close everything
cv2.destroyAllWindows()
