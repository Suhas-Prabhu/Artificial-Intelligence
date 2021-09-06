import tkinter as tk
from tkinter import *
import pickle
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import SnowballStemmer
import re
import numpy as np

with open('Artificial-Intelligence/Sentiment Analysis/Movie review sentiment analysis/model/Movie_review_model.pkl','rb') as file:
  bb = pickle.load(file)
with open('Artificial-Intelligence/Sentiment Analysis/Movie review sentiment analysis/model/bow.pkl','rb') as file:
  word_dict = pickle.load(file)
  
  
def clean_tags(text):
  cleaned = re.compile(r'<.*?>')
  return re.sub(cleaned,'',text)

def clean_special(text):
  rem = ''
  for i in text:
    if i.isalnum():
      rem = rem + i
    else:
      rem = rem + ' '
  return rem

def lower(text):
  return text.lower()

def clean_stopwords(text):
  stop_words = set(stopwords.words('english'))
  words = word_tokenize(text)
  return [w for w in words if w not in stop_words]

def clean_stem(text):
  stem_snow = SnowballStemmer('english')
  return " ".join([stem_snow.stem(w) for w in text])

  
class App(tk.Tk):
  def __init__(self):
    tk.Tk.__init__(self)
    self.x = self.y =0
    self.label = tk.Label(self, text ="write a movie review", font=("Helvetica",24))
    self.inputtxt = Text(self, height = 10,width = 45,bg = "light yellow")
    self.outputtxt = Text(self, height = 2,width = 45,bg = "light yellow")
    self.cl_btn = tk.Button(self,text ="Recognize",command = self.review_classify)
    self.clear_btn = tk.Button(self,text ="Clear",command = self.clear)
    
    self.label.pack()
    self.inputtxt.pack()
    self.cl_btn.pack()
    self.outputtxt.pack()
    self.clear_btn.pack()
      
  def clear(self):
    self.inputtxt.delete("1.0","end")
    self.outputtxt.delete("1.0","end")
    
  def review_classify(self):
    INPUT = self.inputtxt.get("1.0", "end-1c")
    text = clean_tags(INPUT)
    text = clean_special(text)
    text = lower(text)
    text = clean_stopwords(text)
    text = clean_stem(text)
    inp =[]
    for i in word_dict:
      inp.append(text.count(i[0]))
    pred = bb.predict(np.array(inp).reshape(1,1000))
      
    if(pred == 0):
        self.outputtxt.insert(END, 'Negative review')
    else:
        self.outputtxt.insert(END, "Positive review")
    
app = App()
mainloop()
    
  
 