# Cartoonify 

A very simple code to slightly make an image cartoon-ish. 

## setup

download all the files in the folder and install the necessary libraries using the following command:

`pip install -r requirements.txt`

Open the python file and run the code.

<img src="https://brandslogos.com/wp-content/uploads/images/large/python-logo-1.png" width="10%" height="10%" />&nbsp;&nbsp;&nbsp;&nbsp;<img src="https://opencv.org/wp-content/uploads/2020/07/cropped-OpenCV_logo_white_600x.png" width="3%" height="3%" />
***

## How  it works

The code basically  performs multiple image transformation to give a cartoon-like result.

First the Image is converted to grayscale and the grayscale image is smoothened. Then the in the image are extracted and smoothened color image is generated. Once that is done, the edges are masked on aa colored smoothened image toget the cartooned image.

The different transformation images are stored in "images" folder