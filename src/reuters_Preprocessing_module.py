#!/usr/bin/env python
# coding: utf-8

# In[122]:


from bs4 import BeautifulSoup as bs
import os
import json


# In[123]:


rssPath = '../reutersRss/reuters21578'
dataStorage = '../output/reuterStorage.json'
#https://stackoverflow.com/questions/3964681/find-all-files-in-a-directory-with-extension-txt-in-python
#https://stackoverflow.com/questions/15863751/extracting-body-tags-from-smg-file-beautiful-soup-and-python


# In[128]:


def preProcess(dataPath):
    corpus = []
    docId = 1
    i = 0
    for file in os.listdir(dataPath):
        if file.endswith(".sgm"):
            with open(os.path.join(dataPath,file),'rb') as f:
                print(os.path.join(dataPath,file))
                data= f.read()
                reuters = bs(data,'html.parser')
                for s in reuters.find_all('reuters'):
                    container = dict()
                    container['docId'] = docId
                    title = s.find('title')

                    if not title is None and title.text:
                        container['title'] = title.text.strip()
                    else:
                        container['title'] = 'NO_TITLE'
                    topic = s.find('topics')
                    if not topic is None and topic.text:
                        container['topic'] = topic.text
                    else:
                         container['topic'] = 'NO_TOPIC'
                    body = s.find('body')
                    if not body is None and body.text:
                        # there is " x " quotation in the body. May need to think about it
                        container['desc'] = " ".join(body.text.split()).replace('\u0003', '')
                    else:
                        container['desc'] = 'NO_CONTENT'
                    corpus.append(container)
                    docId = docId + 1
    return corpus


# In[129]:


def getCorpus():
    data = preProcess(rssPath)
    with open(dataStorage,'w') as f:
        json.dump(data, f, sort_keys=True, indent=4,ensure_ascii=False)


# In[ ]:




