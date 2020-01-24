#!/usr/bin/env python
# coding: utf-8

# In[58]:


from bs4 import BeautifulSoup as bs
import os
import json
#conda install -c conda-forge langdetect
# with anaconda 3 envir
from langdetect import detect


# In[59]:


rssPath = '../resources'
dataStorage = '../output/storage.json'


# In[193]:


def preProcess(dataPath):
    data = []
    #assumptions
    #write it in the doc that we spilt all htmls into different files
    # keep the courses without description, store them with desc = 'nothing to see here'
    # if courses are available in both en and fr, keep the new title with english only
    #remove leading space in the desc or title
    
    #https://stackoverflow.com/questions/16780158/search-within-tags-with-beautifulsoup-python
    #https://stackoverflow.com/questions/19080957/how-to-remove-all-a-href-tags-from-text
    #https://www.freecodecamp.org/news/how-to-scrape-websites-with-python-and-beautifulsoup-5946935d93fe/
                
    i=0
    docId = 1
    for html in os.listdir(dataPath):
        ## temp, only process one file now
        if i==0:
            i=i+1
            with open(os.path.join(dataPath,html)) as f:
                file = bs(f,'html.parser')
                mainDiv = file.find('div', attrs={'class':'sc_sccoursedescs'})

            
                for courseblock in mainDiv.find_all('div', attrs={'class':'courseblock'}):
                    container = dict()
                    container['docId'] = docId
                    #print(docId)
                    docId = docId+1
                    title = courseblock.find('p',attrs={'class':'courseblocktitle noindent'}).string.rsplit('(',1)[0]
                    #print(title)
                    desc = courseblock.find('p',attrs={'class':'courseblockdesc noindent'})
                    if not desc is None:
                        for a in desc.findAll('a'):
                            a.replaceWithChildren()
                            #for some reasons desc.string sometimes returns NONE even though there indeed texts
                        container['desc'] = desc.text.strip()
                    else:
                        container['desc'] = 'Nothing to see here'
                    if '/' not in title:
                        container['title'] = title
                    else:
                        container['title'] = title.rsplit('/',1)[1].strip()
                    
                    
                    if detect(title) == 'en' and detect(container['desc']) == 'en':
                        data.append(container)
                
    return data


# In[195]:


data = preProcess(rssPath)


# In[196]:


with open(dataStorage,'w') as f:
        json.dump(data, f, sort_keys=True, indent=4)

