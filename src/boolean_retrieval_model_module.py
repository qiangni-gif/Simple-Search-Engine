#!/usr/bin/env python
# coding: utf-8

# In[130]:


import inverted_index_construction_module as iic
import importlib
importlib.reload(iic)
import os
import json


# In[109]:


s = 'printer AND ( laser OR ink )'
#https://stackoverflow.com/questions/1059559/split-strings-into-words-with-multiple-word-boundary-delimiters
#https://runestone.academy/runestone/books/published/pythonds/BasicDS/InfixPrefixandPostfixExpressions.html
#https://stackoverflow.com/questions/1720421/how-do-i-concatenate-two-lists-in-python
#https://stackoverflow.com/questions/3697432/how-to-find-list-intersection
#Assume there are always spaces between Brackets and words, all connectors are cap
# NOT is phrased as AND_NOT as shown in description


# In[57]:


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


# In[120]:


def findPostings(logicalOp, p1, p2):
    if logicalOp == 'OR':
        return list(set(p1+p2))
    elif logicalOp == 'AND':
        return list(set(p1) & set(p2))
    elif logicalOp == 'AND_NOT':
        return p1


# In[ ]:


def wildCard_bigram_handle(token):
    


# In[128]:


def demo_processWithIndex(query, selectedCollection,index):
#     if os.path.exists(iic.indexPath):
#         with open(iic.indexPath, 'r') as file:
#             f = json.load(file)
            
            terms = []
            resultList = []
            totalPostings = []
            postfixList = queryToPostfix(query)
            for token in postfixList:
                if '*' in token:
                    wildCard_bigram_handle(token)
            
            # I would rather manipulate on list of postings rathe then on words
            for token in postfixList:
                if token == "OR" or token == "AND" or token == "AND_NOT":
                    totalPostings.append([token])
                else:
                    p1 = []
                    print(token+'!!!')
                    if token in index:
                        p1 = [d[0] for d in index[token]]
                    totalPostings.append(p1)
            print(totalPostings)
            for token in totalPostings:
                print(terms)
                if token[0] == "OR" or token[0] == "AND" or token[0] == "AND_NOT":
                    p1 = terms.pop()
                    p2 = terms.pop()
                    terms.append(findPostings(token[0],p1,p2))
                else:
                    terms.append(token)
            return terms


# In[129]:


demo_processWithIndex(s,[],index)


# In[72]:


l = [[1,2],[3,4],[5,6],[7,8],[9,0]]
print([d[0] for d in l])


# In[74]:


p1 = [1,2,3,5,6]
p2 = [1,3,5,6,9,8]
print(list(set(p1+p2)))


# In[78]:


y = [3,4,6,7,0]
t = [1,2,3,4,5,6,7,8,9,0]
pt = [2,3,5,7,9,0]
print(list(set(y) & set([p for p in t if p not in pt])))


# In[125]:


index = {'printer':[[1,0],[3,0],[6,0],[11,0],[13,0],[16,0],[18,0],[19,0],[20,0]],
         'laser':[[2,0],[3,0],[5,0],[11,0],[12,0],[16,0],[17,0],[18,0],[20,0],[22,0],[23,0]],
         'ink': [[4,0],[5,0],[9,0],[10,0],[15,0],[19,0],[20,0]]         
        }


# In[127]:


list(set([2,3,4,5,9,10,11,12,15,16,19,20,17,18,22,23]) & set([1,3,6,11,13,16,18,19,20]))


# In[132]:


'*' in 'zx*c'

