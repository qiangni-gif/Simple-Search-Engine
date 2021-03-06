#!/usr/bin/env python
# coding: utf-8

# In[1]:


import dictionary_building_module as db
import importlib
import os
import json
import operator
importlib.reload(db)


# In[2]:


#https://stackoverflow.com/questions/4233476/sort-a-list-by-multiple-attributes
#https://stackoverflow.com/questions/45340785/update-counter-collection-in-python-with-string-not-letter
#https://www.programiz.com/python-programming/methods/dictionary/update
#https://docs.python.org/3.3/howto/sorting.html


# In[3]:


#indexPath = '../output/index.json'
indexPath = '../output/reuterIndex.json'


# In[4]:


def getTermsAndFrequency():
    return db.extractTerms()


# In[5]:


# word -> [[list of docIds],[list of frequencies(map to docId)]]
def buildIndex():
    terms,frequency,t = getTermsAndFrequency()
    # create all terms to be used in wildcard
#     with open('../output/terms.json','w') as f:
#         json.dump({"terms":t}, f, sort_keys=True, indent=4,ensure_ascii=False)
     #return a posting list dict (with weight in it)
    l,p = buildTermIdPairAndTotalPostings(terms)
    # sort list based on term
    l = sorted(l, key = operator.itemgetter(0))
    return buildPostings(l,frequency,p)
        


# In[6]:


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


# In[7]:


def buildPostings(pairContainer,frequency,totalPostings):
    postings = dict()

    for pair in pairContainer:
        term=pair[0]
        if term not in postings:
            postings[term] = []
            # [(docIds, wordCounts in that doc normalized by doc length)]
            # well.... when dumps into json, tuple becomes lisst
        postings[term].append((pair[1], frequency[pair[1]][term]))
    # remove duplicates: if a word appear more than once in a doc, above algo will append it more than once
    for k,v in postings.items():
        postings.update({k:sorted(list(set(v)))})
    return postings


# In[8]:


# terms => terms[docId] = list(terms)
def buildTermIdPairAndTotalPostings(terms):
    listContainer = []
    postings = []
    for k,v in terms.items():
        #k is docId, v is list of terms
        for d in v:
            #[term,id]
            pair = [d,k]
            listContainer.append(pair)
            postings.append(k)
    # return a list of term/docID pair
    return listContainer, sorted(list(set(postings)))


# In[9]:


#get call if the file doesn;t exist (I think..)
def getIndex():
    index = buildIndex()
    with open(indexPath,'w') as f:
        json.dump(index, f, sort_keys=True, indent=4,ensure_ascii=False)

