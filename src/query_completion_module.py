#!/usr/bin/env python
# coding: utf-8

# In[1]:


import json


# In[30]:


# modelPath = '../output/testBigramModel.json'
modelPath = '../output/bigramModel.json'
limit = 6
#https://stackoverflow.com/questions/35624064/sorting-dictionary-descending-in-python


# In[35]:


def findNext(query):
    # Let's assume the query is of form "abc cde "
    with open(modelPath,'r') as f:
        file = json.load(f)
        previousWord = query.split()[-1]
        d = file[previousWord]
        sortedProb = {k: v for k, v in sorted(d.items(), key=lambda item: item[1],reverse=True)}
        return [query + x for x in list(sortedProb)[0:limit]]


# In[19]:


list(newf)[0:3]


# In[37]:


findNext("U.S. would ")

