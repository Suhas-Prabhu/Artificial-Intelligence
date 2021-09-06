# import necessary libraries

import numpy as np
import pandas as pd # data processing
import re # for regex
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize # returns the syllables from a single word
from nltk.stem import SnowballStemmer # it is a stemming algorithm
from sklearn.feature_extraction.text import CountVectorizer #  transform a given text into a vector on the basis of the frequency (count) of each word that occurs in the entire text
from sklearn.model_selection import train_test_split # split the dataset into train and test data set
from sklearn.naive_bayes import GaussianNB, MultinomialNB, BernoulliNB
from sklearn.metrics import accuracy_score
import pickle

# load the dataset
data = pd.read_csv('Artificial-Intelligence/Sentiment Analysis/Movie review sentiment analysis/data/IMDB-Dataset.csv')
print(data.shape)
data.head()
data.info()

""" [OUTPUT]
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 50000 entries, 0 to 49999
 #   Column     Non-Null Count  Dtype
---  ------     --------------  -----
 0   review     50000 non-null  object
 1   sentiment  50000 non-null  object
dtypes: object(2)
memory usage: 781.4+ KB
"""

# no null values in the dataset
data.sentiment.value_counts()

"""[OUTPUT]
positive    25000
negative    25000
Name: sentiment, dtype: int64
"""
# encode the sentiments to by mapping positive to 0 and negative to 1
data.sentiment.replace('positive',1, inplace = True)
data.sentiment.replace('negative',0, inplace = True)
data.head(10)

# data.review[0]

# step 1: Remove the HTML Tags

def clean_tags(text):
  cleaned = re.compile(r'<.*?>')
  return re.sub(cleaned,'',text)

data.review = data.review.apply(clean_tags)
# data.review[0]

# step 2: Remove all the special charecters
def clean_special(text):
  rem = ''
  for i in text:
    if i.isalnum():
      rem = rem + i
    else:
      rem = rem + ' '
  return rem

data.review = data.review.apply(clean_special)
# data.review[0]

# step 3: Converting to lowercases
def lower(text):
  return text.lower()

data_review = data.review.apply(lower)
# data_review[0]

# step 4: Remove stopwords

def clean_stopwords(text):
  stop_words = set(stopwords.words('english'))
  words = word_tokenize(text)
  return [w for w in words if w not in stop_words]

data.review = data.review.apply(clean_stopwords)
# data.review[0]

# step 5: Stem the words
def clean_stem(text):
  stem_snow = SnowballStemmer('english')
  return " ".join([stem_snow.stem(w) for w in text])

data.review = data.review.apply(clean_stem)
# data.review[0] 
# data.head()

# creating The model
# creating a bag of words
X = np.array(data.iloc[:0].values)
y = np.array(data.sentiment.values)
cv = CountVectorizer(max_features=1000)
X = cv.fit_transform(data.review).toarray()
print("X shape =",X.shape)
print("Y shape =",y.shape)
# print(X)

# split the dataset in training and test dataset
trainx,testx,trainy,testy = train_test_split(X,y,test_size =0.2,random_state =9)
print("Train shapes : X = {}, y = {}".format(trainx.shape,trainy.shape))
print("Test shapes : X = {}, y = {}".format(testx.shape,testy.shape))

# Model defination and training
gb,mb,bb = GaussianNB(), MultinomialNB(alpha =1 , fit_prior=True ),BernoulliNB(alpha =1.0, fit_prior=True)
gb.fit(trainx, trainy)
mb.fit(trainx, trainy)
bb.fit(trainx, trainy)

pred_gb = gb.predict(testx)
pred_mb = mb.predict(testx)
pred_bb = bb.predict(testx)

print("Gaussian = ",accuracy_score(testy,pred_gb))
print("Multinomial = ",accuracy_score(testy,pred_mb))
print("Bernoulli = ",accuracy_score(testy,pred_bb))

"""[output]
Gaussian =  0.7817
Multinomial =  0.8299
Bernoulli =  0.8371
"""
# save the model
pickle.dump(bb, open('Movie_review_model.pkl','wb'))

word_dict = cv.vocabulary_
pickle.dump(word_dict,open('bow.pkl','wb'))