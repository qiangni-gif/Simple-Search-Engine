#!/usr/bin/env python
# coding: utf-8

# In[1]:


import corpus_preprocess_module as cp
import nltk
import json
import importlib
import string
from langdetect import detect 
from collections import Counter
importlib.reload(cp)
nltk.download('punkt')
#nltk.download('wordnet')
nltk.download('stopwords')


# In[2]:


storagePath = cp.dataStorage
stopWordFlag = True
wordStemmingFlag = True
normalizationFlag = True
ps = nltk.stem.PorterStemmer()
#https://stackoverflow.com/questions/265960/best-way-to-strip-punctuation-from-a-string
#https://stackoverflow.com/questions/1254370/reimport-a-module-in-python-while-interactive
#https://pythonprogramming.net/stemming-nltk-tutorial/
#https://stackoverflow.com/questions/2600191/how-can-i-count-the-occurrences-of-a-list-item
#https://stackoverflow.com/questions/21696649/filtering-out-strings-that-only-contains-digits-and-or-punctuation-python


# In[3]:


def toggleStopWordFlag():
    return not stopWordFlag


# In[4]:


def toggleWordStemmingFlag():
    return not wordStemmingFlag


# In[5]:


def toggleNormalizationFlag():
    return not normalizationFlag


# In[13]:


def extractTerms():
    # encoding="utf8" is required on win 
    data = dict()
    container = dict()
    with open(storagePath, 'r') as file:
        f = json.load(file)
        for d in f:
            terms = tokenize(d['desc'])
            terms = stopWordRemoval(terms)
            terms = wordStemming(terms)
            terms = normalization(terms)
            frequencyPerDoc(container,terms,d['docId'])
            #print(terms)
            data[d['docId']] = terms
            
    return data,container


# In[6]:


def tokenize(data):
    desc = removeFrenchWords(data)
    tokens = [i for i in nltk.word_tokenize(desc) if not all(j in set(string.punctuation) for j in i)]
    #
    #return list(set(tokens))
    return tokens
    


# In[7]:


def removeFrenchWords(desc):
    newTokens = []
    newDesc = ""
    descs = desc.split('/')
    for d in descs:
        if detect(d) == 'en':
            newDesc = newDesc+" "+d
    return newDesc


# In[8]:


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


# In[9]:


def wordStemming(data):
    newData = []
    if wordStemmingFlag:
        #business logic
        for d in data:
            newData.append(ps.stem(d))
    else:
        return data
    return newData


# In[10]:


def normalization(data):
    if normalizationFlag:
        #logic
        newData = [x.translate(str.maketrans('','','-.')) for x in data if x.translate(str.maketrans('','','-.'))!='']
        #print('nor')
    else:
        return data
    return newData


# In[26]:


def pre_dictionary_building():
    cp.getCorpus()


# In[11]:


#dict('docId') -> dict{'word':frequency}
def frequencyPerDoc(container,terms,docId):
    container[docId] = Counter(terms)
    return container
    


# In[227]:


b = ['one','three','one','four','five','six','six','one','nine']
c = ['three','one','one','one','ten','seven','one','one','nine','two','two','three']
d = ['right','cool','fuck','computer','go','what','the','hee']


# In[228]:


dic = dict()
dic[1] = Counter(b)
dic[2] = Counter(c)
dic[3] = Counter(d)


# In[243]:


dic


# In[241]:


counter = Counter()
for k,v in dic.items():
    print(v)
    for x in v:
        counter.update({x:v[x]})


# In[242]:


counter
