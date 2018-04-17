# simple-face_detection

### Features:
- Uses open CV and trained haarcascades to detect faces and eyes in the input image.

### Requirements:
- numpy
```
pip install numpy
```
- openCV
```
sudo apt-get install build-essential cmake git pkg-config
sudo apt-get install libjpeg8-dev libtiff4-dev libjasper-dev libpng12-dev
sudo apt-get install libgtk2.0-dev
sudo apt-get install libavcodec-dev libavformat-dev libswscale-dev libv4l-dev
sudo apt-get install libatlas-base-dev gfortran
pip install opencv-python
```

### Sample output:
```
python simple-face_detection.py
```
![Alt text](prince_det.jpg?raw=true "Detected faces")

### Note:
- While copying the haarcascades from Github, click on Raw and then save it as a haarcascades file.
