# Installing GUI using PyQt5

## TODO
- [ ] Install Qt libraries. Requires ~14GB of disk space
- [ ] Install SIP Python package
- [ ] Install PyQt5 Python package

## Steps to install
1. Python 3
1. Xcode and command-line tools
1. Qt libraries
1. Virtual environment
1. SIP Python package
1. PyQt5 Python package

## Install Xcode and command-line tools
It's available in the root [README.md](https://github.com/rajadavidh/learning-opencv-python#install-xcode)

## Install Qt libraries
* Download Qt libraries from http://www.qt.io/download-open-source/
* Install Qt into the directory `/opt/qt`
  * Requires ~14GB of disk space
* Qt5 book: http://qmlbook.github.io/

### Apps and Utilities
* `Qt Creator.app` - IDE with a graphical GUI designer
* `5.6/clang_64/bin/Designer.app` - the GUI designer
* `5.6/clang_64/bin/pixeltool.app` - a tool to inspect the pixels around the mouse cursor
* `5.6/clang_64/bin/qmlscene` - execute scenes from .QML files
* `5.6/clang_64/bin/qtdiag` - prints diagnostic output about the Qt library

## Create Virtual environment
```shell
# Create the directory
$ mkdir -p ~/.venv

# Create the virtual environment
$ python3 -m venv ~/.venv/qtproject

# Activate the virtual environment
$ . ~/.venv/qtproject/bin/activate

# Test the virtual environment
$ which python3  
# The result should be `~/.venv/qtproject/bin/python3`
```

## Install SIP
Download manually: https://riverbankcomputing.com/software/sip/download

or you can Install it using `pip` or mercurial `hg`.

### Installing using pip (recommended)
```sh
$ pip install sip
```

### Installing using mercurial
```sh
# Clone the source code
$ cd /tmp/
$ hg clone http://www.riverbankcomputing.com/hg/sip
$ cd sip

# Generate the build configuration
$ python2.7 build.py prepare  # build.py is a Python 2 script
$ python3.4 configure.py -d ~/.venv/qtproject/lib/python3.4/site-packages

# Make and install
$ make
$ sudo make install
$ sudo make clean
```

## Install PyQt5
Installation tutorial: https://www.riverbankcomputing.com/static/Docs/PyQt5/installation.html

Download manually: https://riverbankcomputing.com/software/pyqt/download5

or you can Install it using `pip` or mercurial `hg`.

First program in PyQt5: http://zetcode.com/gui/pyqt5/firstprograms/

### Installing using pip (recommended)
```sh
# Install
$ pip install PyQt5

# Uninstall
$ pip uninstall PyQt5
```

## References:
* https://www.metachris.com/2016/03/how-to-install-qt56-pyqt5-virtualenv-python3/