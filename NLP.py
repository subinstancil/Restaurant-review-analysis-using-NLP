
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pickle


dataset = pd.read_csv('Restaurant_Reviews.tsv', delimiter='\t',quoting = 3)


import re
import nltk
# nltk.download('stopwords')
from nltk.corpus import stopwords

from nltk.stem.porter import PorterStemmer
corpus = []
for i in range (0, 1000):
    review = re.sub('[^a-zA-Z]', ' ', dataset['Review'][i])
    
    review = review.lower()
    
    review = review.split()
   
    ps = PorterStemmer()
    review = [ps.stem(word) for word in review if not word in set(stopwords.words('english'))]
    
    review = ' '.join(review)
    corpus.append(review)
    

from sklearn.feature_extraction.text import CountVectorizer

cv = CountVectorizer(max_features = 1500)
X = cv.fit_transform(corpus).toarray()
y = dataset.iloc[:, 1].values

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.20, random_state = 0)

from sklearn.naive_bayes import GaussianNB
classifier = GaussianNB()
classifier.fit(X_train, y_train)


filename = 'finalized_model.sav'
pickle.dump(classifier, open(filename, 'wb'))



y_pred = classifier.predict(X_test)


from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test,y_pred)
print(cm)


text = "Had dinner with girl friends. Menu is perfect, something for everyone. Service was awesome and Jason was very accommodating. Will be back definitely!"
#text = "The food quality is very very bad had order some soup it was so terrible could eat more than a spoonful. They need to change the chef at the earliest."

corpus2 = []
review2 = re.sub("[^a-zA-z]", ' ', text)
review2 = review2.lower()
review2 = review2.split()
ps2 = PorterStemmer()
review2 = [ps2.stem(word) for word in review2 if not word in set(stopwords.words('english'))]
review2 = " ".join(review2)
corpus2.append(review2)
from sklearn.feature_extraction.text import CountVectorizer
cv2 = CountVectorizer(max_features = 1500)
X2 = cv2.fit_transform(corpus + corpus2).toarray()
my = X2[-1].reshape(1, -1)
result = classifier.predict(my)
if result == 1:
    answear = "Positive"
else:
    answear = "Negative"
    
print(answear)  