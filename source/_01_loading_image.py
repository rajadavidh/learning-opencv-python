# Run command: python3 _01_loading_image.py

# Importing libraries as shortcut
import numpy as np
import cv2
import matplotlib.pyplot as plt

# Load the image and covert to greyscale color
#  We must use relative link `../image_location` to avoid `cv2.error: (-215:Assertion failed) VScn::contains(scn)`
#  Source:
#  https://answers.opencv.org/question/212087/trying-to-convert-bgr-to-gray/
#  https://github.com/llSourcell/Object_Detection_demo_LIVE/issues/6#issue-353775712
#  https://stackoverflow.com/questions/52739143/opencv-error-215assertion-failed-vscncontainsscn-vdcncontainsdcn
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
#  OpenCV is using BGR and Matplotlib is using RGB, so we are using greyscale
plt.imshow(img, cmap='gray', interpolation='bicubic')
plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
plt.plot([100, 0], [100, 200], 'c', linewidth=5)  # draw cyan colored line in the image
plt.show()

# Saving image
# cv2.imwrite('fisher_gray.png', img)
