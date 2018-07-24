# Run command: python _02_loading_video_source.py

# Importing libraries as shortcut
import numpy as np
import cv2
import matplotlib.pyplot as plt


# This will return video from the first webcam on your computer.
# '0' means the first webcam
cap = cv2.VideoCapture(0)

while (True):
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.imshow('frame', gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()