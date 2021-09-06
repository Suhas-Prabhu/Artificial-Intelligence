
# import necessary libraries
from keras.models import load_model
from tkinter import *
import tkinter as tk
import win32gui
from PIL import ImageGrab, ImageOps
import numpy as np
import cv2

model = load_model('Artificial-Intelligence/Computer Vision projects/digit recognizer/models/digit_model1.h5')

def digit_prediction(imag):
  #resize the image to 28 by 28 size
  img = imag.resize((28,28))
  # convert RGB to grayscale
  img = img.convert('L')
  img = ImageOps.invert(img)
  img = np.array(img)
  imag = np.array(imag)
  # cv2.imshow('image',imag)
  # cv2.waitKey(0)
  # reshape the image to the model input dimension and normalize them
  img = img.reshape(1,28,28,1)
  img =  img/255.0
  # predicting the class
  result = model.predict([img])[0]
  # print(result)
  return np.argmax(result),max(result)


class App(tk.Tk):
  def __init__(self):
    tk.Tk.__init__(self)
    self.x = self.y =0
    
    #creating the elements
    self.canvas = tk.Canvas(self,width =300,height =300,bg ="white",cursor = "cross")
    self.label = tk.Label(self, text ="thinking ...", font=("Helvetica",48))
    self.cl_btn = tk.Button(self,text ="Recognize",command = self.digit_classify)
    self.clear_btn = tk.Button(self,text ="Clear",command = self.clear)
    
    # grid structure
    self.canvas.grid(row =0,column =0,pady =2,sticky =W)
    self.label.grid(row =0,column =1, pady=2,padx =2)
    self.cl_btn.grid(row =1,column =1,pady =2,padx =2)
    self.clear_btn.grid(row =1,column =0,pady =2)
    
    self.canvas.bind("<B1-Motion>",self.draw_lines)
    
  def clear(self):
    self.canvas.delete("all")
  
  def digit_classify(self):
    canvas_handle = self.canvas.winfo_id() # get the handle of canvas
    print(canvas_handle)
    rect = win32gui.GetWindowRect(canvas_handle) # get the co-ordinates of the canvas
    (a,b,c,d) = rect
    a += 20
    b += 20
    c += 80
    d += 80
    rect =(a,b,c,d)
    image =ImageGrab.grab(rect)
    digit, acc = digit_prediction(image)
    self.label.configure(text =str(digit)+', '+str(int(acc*100))+'%')
    
  def draw_lines(self, event):
    self.x = event.x
    self.y = event.y
    r =8
    self.canvas.create_oval(self.x-r,self.y-r, self.x+r,self.y+r,fill="black")
    
app = App()
mainloop()