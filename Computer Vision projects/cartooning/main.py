#image processing libraries
import cv2 

#GUI libraries
import easygui

#system libraries
import sys


'''We'll use easygui to open a dialog box to chose the file and store the path'''
def upload():
  Img_path = easygui.fileopenbox()
  ctn(Img_path)
  
def ctn(path):
  # read the image
  img = cv2.imread(path)
  rgbimg = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
  
  # make sure the image is loaded
  if img is None:
    print("Image not loaded. choose an image file")
    sys.exit()
  
  # resize the image
  resized = cv2.resize(rgbimg,(960,540))
  cv2.imwrite('Computer Vision projects\cartooning\images/rgb.jpg',resized)
  
  '''To convert an image to a cartoon, multiple transformations are done. 
  '''
  # convert to grayscale
  gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
  resized_gray = cv2.resize(gray,(960,540))
  cv2.imwrite('Computer Vision projects\cartooning\images/gray.jpg',resized_gray)
  
  #smoothening the grayscale
  gray_smooth = cv2.medianBlur(gray,5)
  resized_smooth = cv2.resize(gray_smooth,(960,540))
  cv2.imwrite('Computer Vision projects\cartooning\images/smooth_gray.jpg',resized_smooth)
  
  #retrieving the edges by using thresholding technique
  getEdge = cv2.adaptiveThreshold(gray_smooth,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,9,9)
  
  resized_edge = cv2.resize(getEdge,(960,540))
  cv2.imwrite('Computer Vision projects\cartooning\images/edge.jpg',resized_edge)
  
  
  # keep edge sharp and remove noise using bilateral filter
  color_img = cv2.bilateralFilter(img, 9, 300, 300)
  resized_col = cv2.resize(color_img,(960,540))
  cv2.imwrite('Computer Vision projects\cartooning\images/clr.jpg',resized_col)
  
  #masking edge image with color image
  cartoon_img = cv2.bitwise_and(color_img,color_img,mask =getEdge)
  resized_cartoon = cv2.resize(cartoon_img,(960,540))
  cv2.imwrite('Computer Vision projects\cartooning\images/cartoon.jpg',resized_cartoon)
  
  
  
if __name__ =='__main__':
  upload()  