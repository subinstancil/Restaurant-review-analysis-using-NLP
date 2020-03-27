import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pickle
from sklearn.feature_extraction.text import CountVectorizer

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



filename = 'finalized_model.sav'

loaded_model = pickle.load(open(filename, 'rb'))



#text = "Had dinner with girl friends. Menu is perfect, something for everyone. Service was awesome and Jason was very accommodating. Will be back definitely!"
#text = "The food quality is very very bad had order some soup it was so terrible could eat more than a spoonful. They need to change the chef at the earliest."
def rate(file):
	f = open("reviews/"+file, "r")
	#x=f.readlines()
	flag=0
	counter=0
	for x in f:
		corpus2 = []
		review2 = re.sub("[^a-zA-z]", ' ', x)
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
		result = loaded_model.predict(my)

		counter+=1
		if result == 1:
			flag+=1
	print(counter)
	print(flag)
	avg = (flag/counter)*100

	print(avg)	
	if avg < (20):
		return "1", counter , flag;
	elif avg < (40):
		return "2", counter , flag;  
	elif avg < (60):
		return "3", counter , flag;
	elif avg < (80):
		return "4", counter , flag;
	else:
		return "5", counter , flag;
def pred(comment):
	corpus2 = []
	review2 = re.sub("[^a-zA-z]", ' ',comment)
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
	my_prediction = loaded_model.predict(my)
	return my_prediction



  


