# Learning OpenCV in Python (in progress)
Thanks to Harrison Kinsley for his tutorials, OpenCV with Python Intro and loading Images.  

If you are looking for the complete explanation, you can find it here: https://pythonprogramming.net/loading-images-python-opencv-tutorial/

This project includes code examples from his tutorials.

## Code Examples
1. Loading Image
1. Loading Video Source
1. Drawing and Writing on image 
1. Image Operations
1. Image Arithmetics
1. Thresholding
1. Color filtering
1. Blurring and Smoothing
1. Morphological Transformations
1. Canny Edge Detection and Gradients
1. Template Matching
1. GrabCut Foreground Extraction
1. Corner Detection
1. Feature Matching (Homography) Brute force
1. MOG background reduction
1. Haar Cascade Object Detection Face & Eye
1. Creating your own Haar Cascade

Further reading for tutorials:
* https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_gui/py_image_display/py_image_display.html

## Preparation
### For Mac OSX
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

#### Install OpenCV
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

#### Troubleshooting installation
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

### For Ubuntu
#### Install Python
Todo
#### Install OpenCV
Todo