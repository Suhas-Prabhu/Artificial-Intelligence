# Movie Review classification <img src="http://assets.stickpng.com/images/5f47fabc554fc70004db57a7.png" width="5%" height="5%" />


## setup

download all the files in the folder and install the necessary libraries using the following command:

`pip install -r requirements.txt`

`main.py` contains the code where the data is processed and trained.

The `classify_review.py` contains the code for GUI application for prediction.

The models folder consists of the trained model and the bag of words generated during training.x

<img src="https://brandslogos.com/wp-content/uploads/images/large/python-logo-1.png" width="10%" height="10%" />&nbsp;&nbsp;&nbsp;&nbsp;<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/0/05/Scikit_learn_logo_small.svg/1200px-Scikit_learn_logo_small.svg.png" width="5%" height="5%" />&nbsp;&nbsp;&nbsp;&nbsp;<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/3/31/NumPy_logo_2020.svg/1280px-NumPy_logo_2020.svg.png" width="8%" height="8%" />&nbsp;&nbsp;&nbsp;&nbsp;<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/e/ed/Pandas_logo.svg/1200px-Pandas_logo.svg.png" width="8%" height="8%" />&nbsp;&nbsp;&nbsp;&nbsp;<img src="https://miro.medium.com/max/592/0*zKRz1UgqpOZ4bvuA" width="5%" height="5%" />  
***

## Description

The dataset is the Imdb dataset which contains 2 columns. The data hass to be processed before it can pass through the model.
STEPS TO CLEAN THE REVIEWS :
- Remove HTML tags
- Remove special characters
- Convert everything to lowercase
- Remove stopwords

    Stopwords are those words that do not provide any useful information to decide in which category a text should be classified.

- Stemming

    Stemming is the process of reducing the word to its word stem. In simple words stemming is reducing a word to its base word or stem in such a way that the words of similar kind lie under a common stem. For example – The words care, cared and caring lie under the same stem ‘care’.

The review classification GUI looks as follows

<img src="https://github.com/Suhas-Prabhu/Artificial-Intelligence/blob/master/Sentiment%20Analysis/Movie%20review%20sentiment%20analysis/model/image1.jpg" width="32%" height="70%" />&nbsp;&nbsp;&nbsp;&nbsp;<img src="https://github.com/Suhas-Prabhu/Artificial-Intelligence/blob/master/Sentiment%20Analysis/Movie%20review%20sentiment%20analysis/model/image2.jpg" width="32%" height="70%" />&nbsp;&nbsp;&nbsp;&nbsp;<img src="https://github.com/Suhas-Prabhu/Artificial-Intelligence/blob/master/Sentiment%20Analysis/Movie%20review%20sentiment%20analysis/model/image3.jpg" width="32%" height="70%" />

