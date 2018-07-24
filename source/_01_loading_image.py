# Run command: python3 _01_loading_image.py

# Importing libraries as shortcut
import numpy as np
import cv2
import matplotlib.pyplot as plt

# Load the image and covert to greyscale color
img = cv2.imread('../data/fisher-anyer-beach-2016-raja-david.jpg', cv2.IMREAD_GRAYSCALE)

# # Show the image
# cv2.imshow('Image', img)
#
# # Wait until any key is pressed
# cv2.waitKey(0)
#
# # Close everything
# cv2.destroyAllWindows()

# Show the image using matplotlib
# OpenCV is using BGR and Matplotlib is using RGB, so we are using greyscale
plt.imshow(img, cmap='gray', interpolation='bicubic')
plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
plt.plot([100, 0], [100, 200], 'c', linewidth=5)  # draw cyan colored line in the image
plt.show()

# Saving image
# cv2.imwrite('fisher_gray.png', img)
