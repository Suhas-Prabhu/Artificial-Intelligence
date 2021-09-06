# Handwritten digit recognizer <img src="https://aigeekprogrammer.com/wp-content/uploads/2019/08/Handwriting-digit-recognition-Keras-MNIST.jpg" width="5%" height="5%" />


## setup

download all the files in the folder and install the necessary libraries using the following command:

`pip install -r requirements.txt`

Open the jupyter notebook file and run the code to train the models on the given architecture or to run dataset on your custom architecture.

The `main.py` contains the code for GUI application.

The 2 trained models are stored in the models folder.

<img src="https://brandslogos.com/wp-content/uploads/images/large/python-logo-1.png" width="10%" height="10%" />&nbsp;&nbsp;&nbsp;&nbsp;<img src="https://opencv.org/wp-content/uploads/2020/07/cropped-OpenCV_logo_white_600x.png" width="3%" height="3%" />&nbsp;&nbsp;&nbsp;&nbsp;<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/2/2d/Tensorflow_logo.svg/1200px-Tensorflow_logo.svg.png" width="5%" height="5%" />&nbsp;&nbsp;&nbsp;&nbsp;<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/a/ae/Keras_logo.svg/1200px-Keras_logo.svg.png" width="5%" height="5%" /> 
***


# MNIST Dataset

This project is used to recognize a handwritten digit. It is a difficult task for the machine to recognize the digit as handwritten digits are not perfect. Hence we will be training a large data on a deep learning model to achieve the objective.

The [**MNIST dataset**](http://yann.lecun.com/exdb/mnist/) is used for training the model for handwritten digit recognizer. 

The first obstacle faced here is getting the data in the right format. When the data is downloaded from MNIST website it is in **.IDX** format.**IDX** file format is a binary file format, Hence the data needs to be converted to suitable format before we can use it in our code.The steps to convert it to image array format is shown in [**mnist.py**]() file.


# Digit recognizer

The digit recognizer script follows the below steps:

## step 1: Import the libraries and load the data

The data can also be simply used from the keras library.The Keras library already contains some datasets and MNIST is one of them.

## step 2: process the data

The data loaded is raw data of dimensions (60000,28,28) and The CNN model requires data to be pushed in the dimension of (60000,28,28,1). Hence the data needs to be preproccessed before it can be used.

## step 3: Create the Convolution Neural network

***First Attempt***
A *CNN model* generally consists of convolutional and pooling layers. It works better for data that are represented as grid structures, this is the reason why CNN works well for image classification problems. The dropout layer is used to deactivate some of the neurons and while training, it reduces ***offer fitting of the model***. We will then compile the model with the *Adadelta* optimizer.

***Second Attempt***
CNN architechture : [[Conv2D->relu]*2 -> MaxPool2D -> Dropout]*2 -> Flatten -> Dense -> Dropout -> Out
In this model RMSProp optimizer is used and the number of layers  have inccreased. Further ReduceLROnPlateau is used as the model will benefit by reducing the learning rate if there is no improvement for a few number of epochs.

## step 4: Train the model

Once both the models are trained they will be saved as `'digit_model.h5'`  and `'digit_model1.h5'` respectively. They give an approx of 92% and 98% accuracy respectively.

## step 5: create a GUI for digit recognition

Using Tkinter a GUI application is used to recognize the digits.
The application has a canvas where the user can write a digit. Then the application captures the image of the digit for recognition. The image is processed and evaluated by the model. The result can be displayed on the application screen.





