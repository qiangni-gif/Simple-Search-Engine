import importlib
import os
import json
import operator
import dictionary_building_module as db
import weight_calculation_module as wc

#https://stackoverflow.com/questions/26924812/python-sort-list-of-json-by-value

weightedindexPath = '../output/weightedindex.json'

def gettf_idf():
    wc.getweightedindex()


def extractQueryTerms(query):
    w = {}
    query = db.nltk.word_tokenize(query)
    query = db.stopWordRemoval(query)
    query = db.wordStemming(query)
    query = db.normalization(query)
    print(query)
    for x in query:
        if x not in w:
            y = query.count(x)
            w[x] = y
    return w

#search query -> list of ranked docId with score
def comput_score(query):
    score = {}
    with open(weightedindexPath,'r') as f:
        windex = json.load(f)
        wquery = extractQueryTerms(query)
        print(wquery)
        for q,w in wquery.items():
            for i,t in windex.items():
                for x in t:
                    if q == i:
                        #print(x)
                        if x[0] not in score:
                            score[x[0]] = x[1]*w
                        else:
                            score[x[0]] += x[1]*w
        #sort the list by score
        rank = sorted(score.items(), key=lambda item:item[1], reverse=True)
        #print(rank)
    return rank
