#!/usr/bin/env python
# coding: utf-8

# In[21]:


import os
import json


# In[52]:


corpus = '../output/storage.json'
excerptLength = 50


# In[56]:


def getDocs(docIds):
    docIds.sort()
    if os.path.exists(corpus):
        output = []
        with open(corpus, 'r') as file:
            f = json.load(file)
            l = [d for d in f if d['docId'] in docIds]
        for course in l:
            s = course['desc']
            d = dict()
            if len(s) > excerptLength:
                s = s[:excerptLength]+'...'
            d['link'] = course['docId']
            d['title'] = course['title']
            d['desc'] = s
            output.append(d)
    return output


# In[57]:


#docIds = [1,3,2,4]


# In[58]:


#getDocs(docIds)

