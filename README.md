# openCV-Basic

Belajar opencv dari dasar
0. Install Virtual Environment
    - `$ sudo apt-get install python3-pip`
    - `$ sudo pip3 install virtualenv`
1. Create Virtual Environment namely Env 
    - `$ python -m venv Env`
    or
    - `$ virtualenv .venv`
2. Go to Env 
    - `$ Env\Scripts\activate.bat`
    or 
    - `$ source .venvUbuntu/bin/activate`
3. Check pip list `$ pip list`. If need to upgrade, please upgrade first. `$ python.exe -m pip install --upgrade pip`
4. Check again `$ pip list`
5. Install Numpy `$ pip install numpy`. Check again `$ pip list`
6. Install opencv `$ pip install opencv-contrib-python`
7. How to check opencv already installed:

- Type `$ python`
- Type `import cv2`
- Type `cv2.__version__`

> NB: if point no 6 not work, try `$ pip install opencv-contrib-python-headless` or `$ pip install opencv-python`.

8. Install matplotlib `$ pip install matplotlib`




///////////////////////////////////////////////////////////////////////////////////
# Step 1: Update your repositories
sudo apt-get update

# Step 2: Install pip for Python 3
sudo apt-get install build-essential libssl-dev libffi-dev python-dev
sudo apt install python3-pip

# Step 3: Use pip to install virtualenv
sudo pip3 install virtualenv 

# Step 4: Launch your Python 3 virtual environment, here the name of my virtual environment will be env3
virtualenv -p python3 env3

# Step 5: Activate your new Python 3 environment. There are two ways to do this
. env3/bin/activate # or source env3/bin/activate which does exactly the same thing

# you can make sure you are now working with Python 3
python -- version
# this command will show you what is going on: the python executable you are using is now located inside your virtualenv repository
which python 

# Step 6: code your stuff

# Step 7: done? leave the virtual environment
deactivate



# 23_Face_Detection
1. Download [trained classifier XML file](https://raw.githubusercontent.com/opencv/opencv/master/data/haarcascades/haarcascade_frontalface_default.xml)
2. Save it to your project directory