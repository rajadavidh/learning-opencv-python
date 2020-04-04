# Run command: python _12_grabcut_foreground_extract.py
# Comments from youtube video:
# The nice thing about Grab Cut is that you can improve the segmentation result
# by marking certain pixels as "definitely foreground" and others as "definitely background"
# Further reading:
# https://docs.opencv.org/master/d8/d83/tutorial_py_grabcut.html

# Importing libraries as shortcut
import numpy as np
import cv2
import matplotlib.pyplot as plt

img = cv2.imread('../data/lido-lake-bogor-2013-raja-david.jpg')
mask = np.zeros(img.shape[:2], np.uint8)

bgdModel = np.zeros((1, 65), np.float64)
fgdModel = np.zeros((1, 65), np.float64)

# Setup this rectangle region as the foreground
rect = (161, 79, 150, 150)

# 0 and 2 pixels are converted to the background
# 1 and 3 pixels are the foreground
cv2.grabCut(img, mask, rect, bgdModel, fgdModel, 5, cv2.GC_INIT_WITH_RECT)
mask2 = np.where((mask == 2) | (mask == 0), 0, 1).astype('uint8')
img = img * mask2[:, :, np.newaxis]

# Show the image using matplotlib
plt.imshow(img)
plt.colorbar()
plt.show()

# Wait until any key is pressed
cv2.waitKey(0)

# Close everything
cv2.destroyAllWindows()
