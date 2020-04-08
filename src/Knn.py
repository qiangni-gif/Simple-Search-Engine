#!/usr/bin/env python
# coding: utf-8

# In[14]:


import json
import pandas as pd

from sklearn.neighbors import KNeighborsClassifier

from sklearn.model_selection import train_test_split 
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score,hamming_loss,f1_score

from sklearn.preprocessing import MultiLabelBinarizer

import dictionary_building_module as db


# In[2]:


#dataPath = '../output/test.json'
dataPath = '../output/reuterStorage.json'

X_data = []
y_data = []
X_unknown = []
all_topics = set()
#https://stats.stackexchange.com/questions/233275/multilabel-classification-metrics-on-scikit
#https://stackoverflow.com/questions/10715965/add-one-row-to-pandas-dataframe?answertab=active#tab-top
#https://en.wikipedia.org/wiki/Multi-label_classification
#https://www.kaggle.com/roccoli/multi-label-classification-with-sklearn
#https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.MultiLabelBinarizer.html
#https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsClassifier.html
#https://scikit-learn.org/stable/tutorial/text_analytics/working_with_text_data.html
#https://stackoverflow.com/questions/48467669/tfidf-transformer-sklearn-results-in-no-supported-conversion-for-types-dt


# In[4]:


with open(dataPath, 'r') as f:
    data = []
    df = pd.DataFrame(columns=['docId', 'desc', 'topics'])
    documents = json.load(f)
    i=0
    for doc in documents:
        if (doc['topic'][0] != "NO_TOPIC") and (doc['desc'] != "NO_CONTENT"): # append new row to df
            df.loc[i] = [doc['docId']] + [stringProcess(doc['desc'])]+[tuple(sorted(doc['topic']))]
            i = i+1

            
        elif doc['topic'][0] == "NO_TOPIC" and doc['desc'] != "NO_CONTENT" :
            X_unknown.append((doc['docId'], stringProcess(doc['desc'])))
        #ignore file with not desc/no topics


# In[3]:


def stringProcess(desc):
    return ' '.join(db.normalization(
                    db.wordStemming(
                        db.stopWordRemoval(
                            db.tokenize(desc))))) # strings preprocess


# In[7]:


len(X_unknown)


# In[8]:


df.head()


# In[9]:


multilabel_binarizer = MultiLabelBinarizer()
y = multilabel_binarizer.fit_transform(df['topics'])

X_train,X_test,y_train,y_test = train_test_split(df['desc'], y, test_size = 0.25, random_state = 0)

vectorizer = TfidfVectorizer(strip_accents='unicode', analyzer='word', ngram_range=(1,3), norm='l2')
X_train = vectorizer.fit_transform(X_train)
X_test = vectorizer.transform(X_test)


# In[10]:


classifier = KNeighborsClassifier(n_neighbors = 5,metric = 'minkowski', p=2)
classifier.fit(X_train,y_train)


# In[15]:


predicts = classifier.predict(X_test)
print("Hamming loss =",hamming_loss(y_test,predicts))
print("F1 score =",f1_score(y_test,predicts,average='micro'))


# In[12]:


for docId,des in X_unknown:
    topics = classifier.predict(vectorizer.transform([des]))
    topi = multilabel_binarizer.inverse_transform(topics)
    top = topi[0]
    temp = {"topic": top}
    for d in documents:
        if d['docId'] == docId:
            d.update(temp)


# In[13]:


with open("../output/new.json", "w") as jsonFile: # to replace original corpus
    json.dump(documents, jsonFile)

