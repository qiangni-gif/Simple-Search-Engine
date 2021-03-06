#!/usr/bin/env python
# coding: utf-8

# In[2]:


import inverted_index_construction_module as iic
import dictionary_building_module as db
import importlib
importlib.reload(iic)
importlib.reload(db)
import os
import json
import nltk
from nltk import bigrams


# In[3]:


#https://stackoverflow.com/questions/1059559/split-strings-into-words-with-multiple-word-boundary-delimiters
#https://runestone.academy/runestone/books/published/pythonds/BasicDS/InfixPrefixandPostfixExpressions.html
#https://stackoverflow.com/questions/1720421/how-do-i-concatenate-two-lists-in-python
#https://stackoverflow.com/questions/3697432/how-to-find-list-intersection
#Assume there are always spaces between Brackets and words, all connectors are cap
# NOT is phrased as AND_NOT as shown in description
#https://www.programiz.com/python-programming/methods/string/startswith


# In[4]:


def queryToPostfix(query):
    tokenList = query.split()
    postfixList = []
    opStack = []
    for token in tokenList:
            if token == '(':
                opStack.append(token)
            elif token == ')':
                topToken = opStack.pop()
                while topToken != '(':
                    postfixList.append(topToken)
                    topToken = opStack.pop()
            elif token == "OR" or token == "AND" or token == "AND_NOT":
                opStack.append(token)
            else:
                postfixList.append(token)

    while opStack:
        postfixList.append(opStack.pop())
    print(postfixList)
    return postfixList


# In[5]:


def findPostings(logicalOp, p1, p2):
    if logicalOp == 'OR':
        return list(set(p1+p2))
    elif logicalOp == 'AND':
        return list(set(p1) & set(p2))
    elif logicalOp == 'AND_NOT': # is it the correct way?
        if not p2:# p2 is empty
#             return [x for x in p1 if x not in p2]
            return []
#         return [x for x in p2 if x not in p1]
        return list(set(p2)-set(p1))


# In[32]:


def wildCard_bigram_handle(token,index): # return a new string
    # remember to filter our the incorrect word!!!!!!
    # are we guaranted that there is only one * in a token?
    wildCard = []
    
    if token[0] == "*": #ends with token *abc
        temp = token[1:]
        for bg in bigrams(temp+" "):
            t = "".join(bg).replace(" ","")
            wildCard.append(buildSecIndex(t,index,True))
        # postfilter                    intersection here will find intersection of these lists
        wildCard = [x for x in list(set.intersection(*map(set,wildCard))) if x.endswith(temp)]
                
    elif token[len(token)-1] == '*': # abx*
        temp = token[:-1]
        for bg in bigrams(" "+temp):
            print(bg)
            t = "".join(bg).replace(" ","")
            wildCard.append(buildSecIndex(t,index,False))
        wildCard = [x for x in list(set.intersection(*map(set,wildCard))) if x.startswith(temp)]
    else: #case where * not in the end or begining 
        temp = token.split('*')
        for bg in bigrams(" "+temp[0]): # $abc ???????
            t = "".join(bg).replace(" ","")
            wildCard.append(buildSecIndex(t,index,False))
        for bg in bigrams(temp[1]+" "): # zxc$
            t = "".join(bg).replace(" ","")
            wildCard.append(buildSecIndex(t,index,True))
        wildCard = [x for x in list(set.intersection(*map(set,wildCard))) if x.startswith(temp[0]) and x.endswith(temp[1])]

    
    return listToString(wildCard)


# In[33]:


def listToString(strList):
    return "( "+" OR ".join(strList)+" )"


# In[34]:


def buildSecIndex(bg,index, isEnd):
    secPosting = []
    if len(bg)==1 and not isEnd:
        for k in index:
            if k.startswith(bg): # abc*
                secPosting.append(k)
    elif len(bg)==1 and isEnd:
        for k in index:
            if k.endswith(bg): # *abc
                secPosting.append(k)
    else:
        for k in index:
            if bg in k:
                secPosting.append(k)
    return secPosting


# In[64]:


def demo_processWithIndex(query, selectedCollection,index):
          
            termsPostings = []
            #resultList = []
            totalPostings = []
            # need to apply stemming etc on query
            if '*' in query:
                completeTerms = getCompleteTerms(selectedCollection)
                pre = query.split(" ")
                for t in pre:
                    if '*' in t:
                        newStr = wildCard_bigram_handle(t,completeTerms)
                        query = query.replace(t,newStr)
            print(query)
            postfixList = queryToPostfix(query)

            # I would rather manipulate on list of postings rathe then on words
            for token in postfixList:
                if token == "OR" or token == "AND" or token == "AND_NOT":
                    totalPostings.append([token])
                else:
                    p1 = []
                    print(token+'!!!')
                    #atemming should be done here
                    t = db.normalization(db.wordStemming([token]))[0]
                    print("This is after: "+t)
                    if t in index:
                        p1 = [d[0] for d in index[t]]
                    #if no such token, append []
                    totalPostings.append(p1)
            print("Printing tootalpostings")
            print(totalPostings)
            for token in totalPostings:
                #print(termsPostings)
                if token and (token[0] == "OR" or token[0] == "AND" or token[0] == "AND_NOT"):
                    p1 = termsPostings.pop()
                    p2 = termsPostings.pop()
                    termsPostings.append(findPostings(token[0],p1,p2))
                else:
                    termsPostings.append(token)
            return termsPostings[0]


# In[19]:


def getCompleteTerms(collection):
    path = '../output/reuterTerms.json'
    if collection == "UofO catalog":
        path = '../output/UOterms.json'
        
    with open(path, 'r') as file:
        f = json.load(file)
        temp = []
        for l in f["terms"]:
            temp = list(set(temp+l))
    return temp


# In[13]:


#"( *er OR ink )"
# demo_processWithIndex("*er",[],index)


# In[12]:


index = {'zeroknowledg':[[1,0],[3,0],[6,0],[11,0],[13,0],[16,0],[18,0],[19,0],[20,0]],
         'printer':[[2,4]],
         'laser':[[2,0],[3,0],[5,0],[11,0],[12,0],[16,0],[17,0],[18,0],[20,0],[22,0],[23,0]],
         'ink': [[4,0],[5,0],[9,0],[10,0],[15,0],[19,0],[20,0]],
         'printas':[[1,0],[3,0],[6,0],[11,0],[13,0],[16,0],[18,0],[19,0],[20,0]],
         'prin':[[1,0],[3,0],[6,0],[11,0],[13,0],[16,0],[18,0],[19,0],[20,0]],
         'pri':[[1,0],[3,0],[6,0],[11,0],[13,0],[16,0],[18,0],[19,0],[20,0]],
         'goetc':[[1,0],[3,0],[6,0],[11,0],[13,0],[16,0],[18,0],[19,0],[20,0]],
         'zxctc':[[1,0],[3,0],[6,0],[11,0],[13,0],[16,0],[18,0],[19,0],[20,0]],
         'asdasetc':[[1,0],[3,0],[6,0],[11,0],[13,0],[16,0],[18,0],[19,0],[20,0]],
         'zasdvctc':[[1,0],[3,0],[6,0],[11,0],[13,0],[16,0],[18,0],[19,0],[20,0]],
        }
#print(demo_processWithIndex("( game AND_NOT math )","UofO catalog",json.load(open('../output/index.json', 'r'))))

