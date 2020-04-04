# Run command: python _14_feature_matching.py
# We are going to implement object recognition by finding NEARLY identical
# regions of an image that match a template we provide.

# The template does not need to be the same lighting, angle, rotation, etc.
# Further reading:
# https://docs.opencv.org/master/dc/dc3/tutorial_py_matcher.html
# https://docs.opencv.org/master/d1/de0/tutorial_py_feature_homography.html

# Importing libraries as shortcut
# import numpy as np
import cv2
import matplotlib.pyplot as plt

img1 = cv2.imread('../data/lido-lake-bogor-2013-raja-david.jpg', 0)  # queryImage
img2 = cv2.imread('../data/lido-lake-tree-rotated-pattern.png', 0)   # trainImage

# Initiate ORB detector
orb = cv2.ORB_create()

# Find the keypoints and descriptors with ORB
keypoint1, descriptor1 = orb.detectAndCompute(img1, None)
keypoint2, descriptor2 = orb.detectAndCompute(img2, None)

# Create Brute-Force Matcher object
bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

# Match descriptors
matches = bf.match(descriptor1, descriptor2)

# Sort them in the order of their distance
matches = sorted(matches, key=lambda x: x.distance)

# Draw first 10 matches
img3 = cv2.drawMatches(img1, keypoint1, img2, keypoint2, matches[:10], None, flags=2)

# Show the image using matplotlib
plt.imshow(img3)
plt.show()

# Wait until any key is pressed
cv2.waitKey(0)

# Close everything
cv2.destroyAllWindows()
