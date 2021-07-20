# Dino Game control <img src="https://upload.wikimedia.org/wikipedia/commons/f/f0/Chromium_T-Rex-error-offline.png" width="10%" height="10%" />


## setup

download all the files in the folder and install the necessary libraries using the following command:

`pip install -r requirements.txt`

Open the jupyter notebook file and run the code.

<img src="https://brandslogos.com/wp-content/uploads/images/large/python-logo-1.png" width="10%" height="10%" />&nbsp;&nbsp;&nbsp;&nbsp;<img src="https://opencv.org/wp-content/uploads/2020/07/cropped-OpenCV_logo_white_600x.png" width="3%" height="3%" />&nbsp;&nbsp;&nbsp;&nbsp;<img src="https://upload.wikimedia.org/wikipedia/en/d/d9/Dlib_c%2B%2B_library_logo.png" width="5%" height="5%" />&nbsp;&nbsp;&nbsp;&nbsp; PyAutoGUI 
***
## How  it works

The Dinosaur Game (Chrome Dino) is a built-in browser game in the Google Chrome web browser.The player guides a T-rex across a side-scrolling landscape, avoiding obstacles to achieve a higher score.
It is one of the simplest games you might have ever played. The only two controls that you need to worry about is making the Dino Jump or Crouch in order to avoid obstacles.
The aim is to programmatically press those buttons, we can easily do that by utilizing the **pyautogui** library which will allow us to control our keyboard with python.
To trigger these controls I have set certain ations that will be captured using **opencv**.

### Jump Action
An open mouth acts as trigger for the dino to jump. This can be achieved using facial landmark detection from **Dlib** library to determine an open or closed mouth

### Crouch Action
The face distance with respect to camera is taken as trigger for crouch action. so if the face is closer to the camera the detected size is bigger and the dino should crouch. 
This way we’re controlling the dino by measuring the proximity between the detected face and the camera. So now you can make the dino crouch by moving your face closer and farther
from the camera.

### Steps Taken to achieve the above actions

#### Step 1: Real-time Face Detection

There are different methods available for face detection like OpenCV’s Haar cascades or Dlib’s HOG-based face detector.
Here a more robust deep learning-based SSD face detector with OpenCV’s DNN module is implemeted.The SSD face detector provided by OpenCV is a Caffe model and you will need two 
files to do inference with it. A .prototxt file that defines the model architecture and a .caffemodel file that contains the pre-trained weights for the layers in the
architecture. Both the Caffe model and .prototxt file will be available in the same folder.

We will also need to do some preprocessing steps before we can pass our image to the model, these steps are:

  * Resizing images to 300×300:

  * Applying mean subtraction of values (104, 177, 123):

  * And formating the array structure to a 4D tensor.

Fortunately all these processes will be taken care of by DNN module’s dnn.blobFromImage() function.After preprocessing we can feed the processed image to the network and 
then post-process the results. So the model returns a 4-dimensional array, the shape of which in our case is **(1, 1, 200, 7)**. The resulting array consists of confidence
score for each detection in the image along with 4 coordinates of the detection scaled down to **0-1 range**. For each image, the array also returns 200 detections, 
But we are only interested in detecting a single face,Hence we will extract the face with the highest confidence.

Finally, the true coordinates for the bounding box rectangle can be then retrieved by
**multiplying the scaled-down coordinates by the width and height of the original image before resizing**.

#### Step 2: Find the landmarks for the detected face

To implement the jump mechanism, we need information about whether the mouth is open or closed. For this, we need to detect facial landmarks so we can determine the 
position of upper and lower lips.By using Dlib’s 68 landmark detector, we’ll be able to detect below 68 landmarks on the face.To initialize the landmark detector,
you will use dlib.shape_predictor() function, which will load the pre-trained landmark detector from the disk. Download the pretrained model from [here](https://drive.google.com/file/d/1rVVYuvM9Hb2-NHUWHNsCQ-_YfjGBXZvn/view?usp=sharing)

#### Step 3: Build the Jump Control mechanism for the Dino

In this step, jump control mechanism is implemented.The jump control mechanism used here simply utilizes the euclidean distance between a pair of landmark points indicated below to 
calculate a ratio of mouth height to its width. Using a threshold value for comparison the mouth can then be evaluated as being close or open.

#### Step 4: Build the Crouch Control mechanism

The Crouch control mechanism will utilize the euclidean distance between the top-left corner and bottom-right corner of the face bounding box. When the face is near the camera
the distance will be greater, and when the face is close enough a key down event will be triggered causing the Dino to crouch.The *face_proximity* function calculates the diagonal 
distance and compares it with the *proximity_threshold* to return either True or False.

#### Step 5: Perform Calibration

Caliberate the triggers and tweak it for optimal results

#### Step 6: Keyboard Automation with PyautoGUI

PyAutoGUI which is a simple API that lets a python script control the mouse and keyboard, it’s used to automate processes.

####  Step 7: Build the Final Application

The final application brings all of the components together.

Run the code below and go to Chrome://Dino in your browser. 

Make sure your threshold values are calibrated correctly according to your current posture
