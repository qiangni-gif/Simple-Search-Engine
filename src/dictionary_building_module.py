#!/usr/bin/env python
# coding: utf-8

# In[32]:


import corpus_preprocess_module as cp
import nltk
import json
import importlib
import string
from langdetect import detect 
from collections import Counter
import re
importlib.reload(cp)
nltk.download('punkt')
#nltk.download('wordnet')
nltk.download('stopwords')


# In[33]:


storagePath = cp.dataStorage
stopWordFlag = True
wordStemmingFlag = True
normalizationFlag = True
ps = nltk.stem.PorterStemmer()
#https://stackoverflow.com/questions/265960/best-way-to-strip-punctuation-from-a-string
#https://stackoverflow.com/questions/1254370/reimport-a-module-in-python-while-interactive
#https://pythonprogramming.net/stemming-nltk-tutorial/
#https://stackoverflow.com/questions/2600191/how-can-i-count-the-occurrences-of-a-list-item
#https://stackoverflow.com/questions/17542152/python-split-without-creating-blanks
#https://stackoverflow.com/questions/21696649/filtering-out-strings-that-only-contains-digits-and-or-punctuation-python


# In[34]:


def toggleStopWordFlag():
    return not stopWordFlag


# In[35]:


def toggleWordStemmingFlag():
    return not wordStemmingFlag


# In[36]:


def toggleNormalizationFlag():
    return not normalizationFlag


# In[54]:


def getTermsForBoolean():
    return termsForBoolean


# In[57]:


def extractTerms():
    # encoding="utf8" is required on win 
    data = dict()
    container = dict()
    termsForBoolean = []
    with open(storagePath, 'r') as file:
        f = json.load(file)
        for d in f:
            terms = tokenize(d['desc'])
            terms = stopWordRemoval(terms)
            termsForBoolean.append(terms)
            
            terms = wordStemming(terms)
            terms = normalization(terms)
            frequencyPerDoc(container,terms,d['docId'])
            #print(terms)
            data[d['docId']] = terms
            
    return data,container,termsForBoolean


# In[48]:


def tokenize(data):
    desc = removeFrenchWords(data)
    tokens = [i for i in nltk.word_tokenize(desc) if not all(j in set(string.punctuation) for j in i)]
    #
    #return list(set(tokens))
    return tokens
    


# In[51]:


def removeFrenchWords(desc):
    newTokens = []
    newDesc = ""
    desctemp = re.sub('[/]', '', desc)
    for d in filter(None, desctemp.split('.')):
        if detect(d) == 'en':
            newDesc = newDesc+""+d
    return newDesc


# In[41]:


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


# In[42]:


def wordStemming(data):
    newData = []
    if wordStemmingFlag:
        #business logic
        for d in data:
            newData.append(ps.stem(d))
    else:
        return data
    return newData


# In[43]:


def normalization(data):
    if normalizationFlag:
        #logic
        newData = [x.translate(str.maketrans('','','-.')) for x in data if x.translate(str.maketrans('','','-.'))!='']
        #print('nor')
    else:
        return data
    return newData


# In[44]:


def pre_dictionary_building():
    cp.getCorpus()


# In[45]:


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

