# Learning OpenCV in Python (in progress)
Thanks to Harrison Kinsley for his tutorials, OpenCV with Python Intro and loading Images.  

If you are looking for the complete explanation, you can find it [here](https://pythonprogramming.net/loading-images-python-opencv-tutorial/).

This project includes code examples from his tutorials and other resources.

## Contents
* [Code Examples](#code)
* [Reading resources](#read)
* [Run command](#run)
* [System setup and Troubleshooting](#setup-troubleshoot)
    * [For Mac OSX](#mac)
    * [For Ubuntu](#ubuntu)

## Code Examples <a name="code"></a>
- [x] [Loading Image](source/_01_loading_image.py)
- [x] [Loading Video Source](source/_02_loading_video_source.py)
- [x] [Drawing and Writing on image](source/_03_drawing_writing_image.py)
- [x] [Image Operations](source/_04_image_operations.py)
- [x] [Image Arithmetics](source/_05_image_arithmetics.py)
- [x] [Thresholding](source/_06_thresholding.py)
- [x] [Color filtering](source/_07_color_filtering.py)
- [x] [Blurring and Smoothing](source/_08_blurring_smoothing.py)
- [x] [Morphological Transformations](source/_09_morphological_transformation.py)
- [x] [Canny Edge Detection and Gradients](source/_10_canny_edge.py)
- [ ] [Template Matching](source/_11_template_matching.py)
- [ ] [GrabCut Foreground Extraction](source/_12_grabcut_foreground_extract.py)
- [ ] [Corner Detection](source/_13_corner_detection.py)
- [ ] [Feature Matching (Homography) Brute force](source/_14_feature_matching.py)
- [ ] [MOG background reduction](source/_15_mog_background_reduction.py)
- [ ] [Haar Cascade Object Detection Face & Eye](source/_16_haar_cascade.py)
- [ ] [Creating your own Haar Cascade](source/_17_haar_cascade_custom.py)
- [ ] [Gathering image for Haar Cascade]()
- [ ] [Cleaning images and creating description files]()
- [ ] [Training Haar Cascade object detection]()
- [ ] [Haar Cascade for image and video object classification]()

## Reading resources <a name="read"></a>
### Open CV Tutorial and Documentation
* Official master docs: https://docs.opencv.org/master/d6/d00/tutorial_py_root.html
* Unofficial docs: https://opencv-python-tutroals.readthedocs.io/en/latest/index.html
* All documentation: https://docs.opencv.org/

### Further reading
(TODO)

## Run command <a name="run"></a>
* Open terminal
* Go to each file and run this:
    ```sh
    python2 filename.py
    ```

## System setup and Troubleshooting <a name="setup-troubleshoot"></a>
### Setup for Mac OSX <a name="mac"></a>
#### Install Xcode
Open terminal and type:
```
xcode-select --install
```

#### Install HomeBrew
Type on terminal:
```
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```

To confirm Homebrew installed correctly, run this command:
```
$ brew doctor
Your system is ready to brew.
```

#### Install Python 2 and Python 3
```
brew update
brew install python   # for installing python3
brew install python2  # for installing python2
brew link python      # creates symlinks to python3 installation in Cellar
brew link python@2    # creates symlinks to python2 installation in Cellar
```

Check whether Python using homebrew install correctly:
```
which python2  # it should output /usr/local/bin/python2
which python3  # it should output /usr/local/bin/python3
```

Check Python versions:
```
python2 --version  # it should output Python 2.7.15
python3 --version  # it should output Python 3.7.0
```

#### Install OpenCV 3
Tap to repo:
```
brew tap brewsci/bio  # previous repo: homebrew/science
```
Below command produced error on my machine: 
```
brew install opencv3 --with-contrib --with-python3 --HEAD  # "Error: No head is defined for opencv"
```
This command worked on my machine:
```
brew install opencv3 --with-contrib --with-python3
```
Verifying that OpenCV 3 has been installed:
```
python
>>> import cv2
>>> cv2.__version__
'3.4.2'

python3
>>> import cv2
>>> cv2.__version__
'3.4.2'
```
Running code sample after installation:
```
python test_webcam.py
```

#### Troubleshooting OpenCV 3 installation
If found error after `import cv2` like:
```
RuntimeError: module compiled against API version 0xc but this version of numpy is 0xb
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ImportError: numpy.core.multiarray failed to import
```
We can solve it by [updating numpy installation](https://stackoverflow.com/questions/20518632/importerror-numpy-core-multiarray-failed-to-import):
```
pip install -U numpy   # for python2
pip3 install -U numpy  # for python3
```
#### References:
* http://docs.python-guide.org/en/latest/starting/install/osx/
* https://www.codingforentrepreneurs.com/blog/install-opencv-3-for-python-on-mac/
* https://github.com/Homebrew/homebrew-science/issues/6617
* https://www.pyimagesearch.com/2016/12/19/install-opencv-3-on-macos-with-homebrew-the-easy-way/
* https://www.learnopencv.com/install-opencv3-on-macos/

### Install OpenCV 4 (Update: January 2019)
OpenCV 4 was released on November 20th, 2018

Install supporting libraries
```
brew install cmake pkg-config
brew install jpeg libpng libtiff openexr
brew install eigen tbb
```

(TODO)

#### References:
* https://www.learnopencv.com/install-opencv-4-on-macos/
* https://www.pyimagesearch.com/2018/08/17/install-opencv-4-on-macos/

### Setup for Ubuntu <a name="ubuntu"></a>
#### Install Python
(TODO)
#### Install OpenCV
(TODO)