# Object Detector in Image using YOLOv3

This is an implementation of YOLOv3 model for an Object Detector in images. This repository contains two parts:

#### Table of contents
 1. [Quick Setup](#quick-setup)
 2. [Python Implementation](#python-implementation)
 3. [Flask Application](#flask-application)


### Quick Setup
#### Note: Anaconda distribution is recommended to setup the scripts.

 1. Clone the repository <br>
 `git clone https://github.com/Vedant1202/YOLOv3-Object-Detector.git`
 2. Navigate into the repository <br>
 `cd YOLOv3-Object-Detector`
 3.  Install dependencies using conda <br>
 `conda create --name yolov3 --file requirements.txt`

 ##### It is recommended that a GPU based version of Tensorflow (v2.1) should be used for better  performance. This repository uses a GPU based tensorflow for its implementation.
##### For a CPU based version of Tensorflow use the command

    conda install tensorflow

### A [brief overview](https://medium.com/@ODSC/overview-of-the-yolo-object-detection-algorithm-7b52a745d3e0) on YOLO algorithm.


 ### Python Implementation

### File Structure

 1. **application/** - Contains the Flask Application.
 2. **weights/** - Directory to contain the parsed weights of the Pretrained YOLOv3 Model.
 3. **coco.names** - File containing label names for the pretrained model.
 4. **convert_weights.py** - Python script to parse weights of pretrained model.
 5. **dogandcat2.jpg** - Sample Image to test scripts.
 6. **image.py** - Main script.
 7. **requirements.txt** - File containing conda environment dependencies.
 8. **utils.py** - File containing utility functions for YOLOv3 model.
 9. **yolov3.cfg** - YOLOv3 configuration file.
 10. **yolov3.py** - Script containing the YOLOv3 model and network.
 11. **yolov3.weights** - File containing YOLOv3 pretrained model weights. This needs to be downloaded from this [link](https://drive.google.com/file/d/1aMrzvdsgqi3Md1O7X2R1DcbcClKbnQq_/view?usp=sharing).

 ### Steps to run the scripts:

 1. Activate the environment (if not already activated) <br>
 `conda activate yolov3`
 2. Create folder "**weights**"  (if not already present) in the root directory.
 3. Download the yolov3.weights file from this [link](https://drive.google.com/file/d/1aMrzvdsgqi3Md1O7X2R1DcbcClKbnQq_/view?usp=sharing).
 4. Run convert_weights.py. This will parse the weights and store them in weights directory. <br>
 `python convert_weights.py`
5. Finally run the image.py file. <br>
`python image.py` <br><br>
A sample output is as follows. This output is based on an image containing a dog and a cat.
The script filters only the box co-ordinates of the box containing a dog and outputs it as
was described in the code challenge page.
![enter image description here](https://raw.githubusercontent.com/Vedant1202/YOLOv3-Object-Detector/master/readme-images/output.PNG)



 ## Flask Application

This is a server-client application with a **Flask** backend to serve the model on a web service.
This application resides in the **application** directory in the root folder.

#### File Structure

 1. **client/** - Directory containing client side files.
 2. **client/css/** - Directory containing CSS files.
 3. **client/js/** - Directory containing JS files.
 4. **client/resources/** - Directory containing static resources like images.
 5. **client/views** - Directory containing HTML files.
 6. **server/** - Directory containing server side files.
 7. **server/controller/** - Directory containing controller services for server.
 8. **server/controller/detector/** - Directory containing python implementation modules for server. This directory is similar to the root directory and should be setup as explained in the above section.
 9. **server/controller/detector/cropped/** - This directory will contain the cropped images which are a result of the server processing. This directory should be created if not present.
 10. **server/controller/detector/input/** - This directory will contain the images received from the client which will be fed to the model. This directory should be created if not present.
 11. **server/controller/accept.py** - Script containing service to accept incoming images from client.
 12. **server/utils/** - Directory containing utility services for server.
 13. **app.py** - Initialisation for Flask Application.
 14. **server.py** - Script containing server routes and start-up script.

 ### Steps to setup the server (Only during the first time):

 1. Navigate to **application/server/controller/detector/** directory.
 2. Run convert_weights.py <br>
 `python convert_weights.py` <br>
*Note: Before running this, please make sure "weights" directory is present in the current directory and the weights have been downloaded from the google drive link mentioned above*

**You are done with setup for the flask app. Remember this step has to be done only during the first time. Once done only the startup scripts need to be run which are explained as follows.**

### Steps to start up the server:

 1. Navigate to **application/server/** directory.
 2. Run server.py <br>
 `python server.py` <br>
 **Server has been started on [http://localhost:4000/](http://localhost:4000/).**
 **Open home.html file from application/client/views/ directory in your browser.**

### How to use the application.
*The application also has a 'how it works' section on the top navigation bar. You can explore that as well.* <br>

#### [A youtube video for an example use case is on this link](https://youtu.be/fnke6UG_giM). 

 1. After starting the server, open the home.html file in your browser.

 2. The home.html page looks like this:
![enter image description here](https://raw.githubusercontent.com/Vedant1202/YOLOv3-Object-Detector/master/readme-images/home.PNG)

3. Select an image.
![enter image description here](https://raw.githubusercontent.com/Vedant1202/YOLOv3-Object-Detector/master/readme-images/choose.PNG)

4. Click submit and wait till server processes.
![enter image description here](https://raw.githubusercontent.com/Vedant1202/YOLOv3-Object-Detector/master/readme-images/loading.PNG)

5. View or Download the results.
![enter image description here](https://raw.githubusercontent.com/Vedant1202/YOLOv3-Object-Detector/master/readme-images/results.PNG)
