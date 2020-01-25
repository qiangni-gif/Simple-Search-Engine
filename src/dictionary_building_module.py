#!/usr/bin/env python
# coding: utf-8

# In[108]:


import corpus_preprocess_module as cp
import nltk
import json
import importlib
import string
from langdetect import detect 
importlib.reload(cp)
nltk.download('punkt')
#nltk.download('wordnet')
nltk.download('stopwords')


# In[193]:


storagePath = dataStorage
stopWordFlag = True
wordStemmingFlag = True
normalizationFlag = True
ps = nltk.stem.PorterStemmer()
#https://stackoverflow.com/questions/265960/best-way-to-strip-punctuation-from-a-string
#https://stackoverflow.com/questions/1254370/reimport-a-module-in-python-while-interactive
#https://pythonprogramming.net/stemming-nltk-tutorial/
#https://stackoverflow.com/questions/21696649/filtering-out-strings-that-only-contains-digits-and-or-punctuation-python


# In[16]:


def toggleStopWordFlag():
    return not stopWordFlag


# In[17]:


def toggleWordStemmingFlag():
    return not wordStemmingFlag


# In[18]:


def toggleNormalizationFlag():
    return not normalizationFlag


# In[141]:


def extractTerms():
    # encoding="utf8" is required on win 
    data = dict()
    with open(storagePath, 'r') as file:
        f = json.load(file)
        for d in f:
            terms = tokenize(d['desc'])
            terms = stopWordRemoval(terms)
            terms = wordStemming(terms)
            terms = normalization(terms)
            #print(terms)
            data[d['docId']] = terms
    return data


# In[142]:


def tokenize(data):
    desc = removeFrenchWords(data)
    tokens = [i for i in nltk.word_tokenize(desc) if not all(j in set(string.punctuation) for j in i)]
    return list(set(tokens))
    


# In[97]:


def removeFrenchWords(desc):
    newTokens = []
    newDesc = ""
    descs = desc.split('/')
    for d in descs:
        if detect(d) == 'en':
            newDesc = newDesc+" "+d
    return newDesc


# In[119]:


def stopWordRemoval(data):
    newData = []
    if stopWordFlag:
        for d in data:
            if d.lower() not in nltk.corpus.stopwords.words('english'):
                newData.append(d)
        #logic for removing stopwords
    else:
        return data
    return newData


# In[206]:


def wordStemming(data):
    newData = []
    if wordStemmingFlag:
        #business logic
        for d in data:
            newData.append(ps.stem(d))
    else:
        return data
    return newData


# In[189]:


def normalization(data):
    if normalizationFlag:
        #logic
        newData = [x.translate(str.maketrans('','','-.')) for x in data if x.translate(str.maketrans('','','-.'))!='']
        print('nor')
    else:
        return data
    return newData


# In[26]:


def pre_dictionary_building():
    cp.getCorpus()

