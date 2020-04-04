# Run command: python _05_image_arithmetics.py
# Further reading:
# https://docs.opencv.org/master/d0/d86/tutorial_py_image_arithmetics.html

# Importing libraries as shortcut
# import numpy as np
import cv2
# import matplotlib.pyplot as plt

# Load 2 images with same size = 1024 x 614
img1 = cv2.imread('../data/fisher-anyer-beach-2016-raja-david.jpg')
img2 = cv2.imread('../data/kali-ketabang-surabaya-2015-raja-david.jpg')

# -----------------------------------------------------------------------------------
# Using arithmetic operation
#  This produced a bit messy result
add1 = img1 + img2

# Using opencv 'add' function
#  (155, 211, 79) + (50, 170, 200) = (205, 381, 279) translated to (205, 255, 255)
#  This produced the image is very "white."
add2 = cv2.add(img1, img2)

# Show the image
cv2.imshow('Add using arithmetic', add1)
cv2.imshow('Add using opencv func', add2)
# -----------------------------------------------------------------------------------
# Using opencv 'addWeighted' function
weighted = cv2.addWeighted(img1, 0.6, img2, 0.4, 0)

# Show the image
cv2.imshow('Add weighted operation', weighted)
# -----------------------------------------------------------------------------------

# Load 2 images with different size
img3 = cv2.imread('../data/lido-lake-bogor-2013-raja-david.jpg')  # 1024 x 768
img4 = cv2.imread('../data/fisher-anyer-beach-2016-raja-david.jpg')  # 1024 x 614

# Taking 'img4' as foreground and add it to 'img3'
#  Create an ROI to put 'img4' on top-left corner
rows, cols, channels = img4.shape
roi = img3[0:rows, 0:cols]

# Now create a mask of 'img4' and create its inverse mask
img4gray = cv2.cvtColor(img4, cv2.COLOR_BGR2GRAY)

# Add a threshold
#  If the pixel value is above 220, it will be converted to 255
#  If the pixel value is below 220, it will be converted to black
ret, mask = cv2.threshold(img4gray, 220, 255, cv2.THRESH_BINARY_INV)

mask_invisible = cv2.bitwise_not(mask)

# Now black-out the area of 'img4' in ROI
img3_bg = cv2.bitwise_and(roi, roi, mask=mask_invisible)

# Take only region of 'img4' from 'img4' image
img4_fg = cv2.bitwise_and(img4, img4, mask=mask)

# Overlapping the image
dst = cv2.add(img3_bg, img4_fg)
img3[0:rows, 0:cols] = dst

# Show the image
cv2.imshow('result', img3)

# Wait until any key is pressed
cv2.waitKey(0)

# Close everything
cv2.destroyAllWindows()
