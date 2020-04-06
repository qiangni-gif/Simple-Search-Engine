import importlib
import os
import json
import operator
import weight_calculation_module as wc

#https://stackoverflow.com/questions/26924812/python-sort-list-of-json-by-value

weightedindexPath = '../output/weightedindex.json'
reuterWindexPath = '../output/reuter_weightedindex.json'
countMax = 20

def gettf_idf():
    wc.getweightedindex()


def extractQueryTerms(query):
    w = {}
    query = wc.iic.db.nltk.word_tokenize(query)
    query = wc.iic.db.stopWordRemoval(query)
    query = wc.iic.db.wordStemming(query)
    query = wc.iic.db.normalization(query)
    return query

def count(query):
    w = {}
    for x in query:
        if x not in w:
            y = query.count(x)
            w[x] = y
    return w
#search query -> list of ranked docId with score
def comput_score(query,collection):
    c = 0
    wquery = count(query)
    score = {}

    if collection == "UofO catalog":
        windexPath = weightedindexPath
    elif collection == "Reuters21578":
        windexPath = reuterWindexPath

    with open(windexPath,'r') as f:
        windex = json.load(f)
        for q,w in wquery.items():
            for i,t in windex.items():
                for x in t:
                    if q == i:
                        c = c + 1
                        if x[0] not in score:
                            score[x[0]] = x[1]*w
                        else:
                            score[x[0]] += x[1]*w
        #sort the list by score
        if score != {}:
            rank = sorted(score.items(), key=lambda item:item[1], reverse=True)
            rank = rank[:countMax]
            score = {}
            c = 0
        else:
            rank = None
            score = {}
            c = 0
        print(rank)
    return rank

# print(comput_score(extractQueryTerms("text"),"Reuters21578"))
# print(count(extractQueryTerms("text")))
