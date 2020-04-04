# Run command: python _02_loading_video_source.py
# Further reading:
# https://docs.opencv.org/master/dd/d43/tutorial_py_video_display.html
# https://www.codingforentrepreneurs.com/blog/opencv-python-web-camera-quick-test/

# Importing libraries as shortcut
# import numpy as np
import cv2
# import matplotlib.pyplot as plt


# Setup webcam
#  This will return video from the first webcam on your computer. '0' means the first webcam
cap = cv2.VideoCapture(0)


while True:
    # Capture frame-by-frame
    #  "frame" will get the next frame in the camera (via "cap")
    #  "ret" will obtain return value from getting the camera frame, either true of false
    #  Source:
    #  https://stackoverflow.com/questions/28773186/what-does-ret-and-frame-mean-here
    #  https://docs.opencv.org/3.1.0/dd/d43/tutorial_py_video_display.html
    ret, frame = cap.read()

    # Our operations on the frame come here
    #  OpenCV reads colors as BGR (Blue Green Red), where most computer applications read as RGB (Red Green Blue)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Display the resulting frame
    cv2.imshow('frame', frame)
    cv2.imshow('gray', gray)

    # This statement just runs once per frame.
    #  If we click 'q' key, we will exit the while loop with a break,
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
