#!/usr/bin/env python
# coding: utf-8

# In[1]:


from bs4 import BeautifulSoup as bs
import os
import json
#conda install -c conda-forge langdetect
# with anaconda 3 envir
from langdetect import detect


# In[41]:


rssPath = '../resources'
dataStorage = '../output/storage.json'


# In[42]:


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
    #https://stackoverflow.com/questions/18337407/saving-utf-8-texts-in-json-dumps-as-utf8-not-as-u-escape-sequence

    docId = 1
    for html in os.listdir(dataPath):
        ## temp, only process one file now

        with open(os.path.join(dataPath,html)) as f:
            print(os.path.join(dataPath,html))
            if not '.DS_Store' in os.path.join(dataPath,html):    
                file = bs(f,'html.parser')
                mainDiv = file.find('div', attrs={'class':'sc_sccoursedescs'})


                for courseblock in mainDiv.find_all('div', attrs={'class':'courseblock'}):
                    container = dict()
                    container['docId'] = docId
                        #print(docId)
                    docId = docId+1
                    title = courseblock.find('p',attrs={'class':'courseblocktitle noindent'}).string.rsplit('(',1)[0]
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
                        string = title.rsplit('/',1)
                        temp = string[0].split(' ')
                        container['title'] = temp[0]+' '+temp[1]+string[1]
                        #print(container['title'])
                    # usually a '/' means there are en and fr
#                     if detect(container['title']) == 'en' and detect(container['desc'].split('/',1)[1]) == 'en':
#                             data.append(container)
#                     if detect(container['title']) == 'en':
#                         print(container['title'])
                    data.append(container)
                
    return data


# In[43]:


def getCorpus():    
    data = preProcess(rssPath)
    with open(dataStorage,'w') as f:
            json.dump(data, f, sort_keys=True, indent=4,ensure_ascii=False)

