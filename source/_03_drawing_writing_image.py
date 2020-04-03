# Run command: python _03_drawing_writing_image.py

# Importing libraries as shortcut
import numpy as np
import cv2
# import matplotlib.pyplot as plt

# Load the image and covert to greyscale color
img = cv2.imread('../data/fisher-anyer-beach-2016-raja-david.jpg', cv2.IMREAD_COLOR)

# Drawing line
cv2.line(img, (0, 0), (20, 100), (245, 245, 245), 10)

# Drawing rectangle
cv2.rectangle(img, (15, 25), (200, 150), (255, 0, 255), 10)

# Drawing circle
#  x'-1' for thickness means we will get a filled in circle.
cv2.circle(img, (447, 63), 63, (0, 255, 0), -1)

# Drawing polygons
pts = np.array([[10, 5], [20, 30], [70, 20], [50, 10]], np.int32)  # array of coordinates
pts = pts.reshape((-1, 1, 2))
cv2.polylines(img, [pts], True, (0, 255, 255), 3)

# Put Text
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, 'Learning OpenCV Python', (10, 500), font, 2, (200, 255, 155), 10, cv2.LINE_AA)

# Show the image
cv2.imshow('Image', img)

# Wait until any key is pressed
cv2.waitKey(0)

# Close everything
cv2.destroyAllWindows()
