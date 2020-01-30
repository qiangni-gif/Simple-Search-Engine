#!/usr/bin/env python
# coding: utf-8

# In[60]:


import dictionary_building_module as db
import importlib
import os
import json
import operator
importlib.reload(db)


# In[61]:


#https://stackoverflow.com/questions/4233476/sort-a-list-by-multiple-attributes
#https://stackoverflow.com/questions/45340785/update-counter-collection-in-python-with-string-not-letter
#https://www.programiz.com/python-programming/methods/dictionary/update
#https://docs.python.org/3.3/howto/sorting.html


# In[62]:


def getTermsAndFrequency():
    return db.extractTerms()


# In[63]:


# word -> [[list of docIds],[list of frequencies(map to docId)]]
def buildIndex():
    terms,frequency = getTermsAndFrequency()
     #return a posting list dict (with weight in it)
    l = buildTermIdPair(terms)
    # sort list based on term
    l = sorted(l, key = operator.itemgetter(0))
    return buildPostings(l,frequency)
        


# In[64]:


# not sure if we need this func

# #frequency is for each docID, term counts for each term
# def calculateDFPerTerm(frequency):
#     counter = Counter()
#     for k,v in frequency.items():
# #     print(v)
#         for x in v:
#             counter.update({x:v[x]})
#             # frequency of 
#     return counter


# In[72]:


def buildPostings(pairContainer,frequency):
    postings = dict()
#     for pair in pairContainer:
#         term = pair[0]
#         if term not in postings:
#             postings[term]=[]

#        #print(postings)
#         for p in pairContainer:
#             if p[0] in postings: # curious why if p[0] in postings and p[1] not in postings[p[0]] gives wrong result
#                 if p[1] not in postings[p[0]]:
#                     #p[0] is term, here we append corresponding docId and frequency of word in that doc as tuple
#                     postings[p[0]].append((p[1],frequency[p[1]]))
#             else:
#                 break
    for pair in pairContainer:
        term=pair[0]
        if term not in postings:
            postings[term] = []
            # [(docIds, wordCounts in that doc)]
        postings[term].append((pair[1], frequency[pair[1]][term]/sum(frequency[pair[1]].values())))
    # remove duplicates: if a word appear more than once in a doc, above algo will append it more than once
    for k,v in postings.items():
        postings.update({k:sorted(list(set(v)))})
    return postings


# In[73]:


# terms => terms[docId] = list(terms)
def buildTermIdPair(terms):
    listContainer = []
    for k,v in terms.items():
        #k is docId, v is list of terms
        for d in v:
            #[term,id]
            pair = [d,k]
            listContainer.append(pair)
    # return a list of term/docID pair
    return listContainer


# In[74]:


#get call if the file doesn;t exist (I think..)
def getIndex():
    index = buildIndex()
    with open('../output/index.json','w') as f:
        json.dump(index, f, sort_keys=True, indent=4,ensure_ascii=False)


# In[75]:


getIndex()


# In[13]:


terms = {1:['A','B','C'],2:['A','V'],3:['R','O','U','Q'],4:['S','Z','S','U'],5:['V','F','R','S','I'],6:['V','P','U','A']}


# In[14]:


t = buildTermIdPair(terms)
t = sorted(t, key = operator.itemgetter(0))


# In[15]:


print(t)


# In[23]:


#buildPostings(t,[]) #before


# In[18]:


#buildPostings(t,[])#after
