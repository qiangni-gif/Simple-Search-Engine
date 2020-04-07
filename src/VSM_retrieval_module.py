import importlib
import os
import json
import operator
import weight_calculation_module as wc
import nltk
import relevance_feedback_model as rfm
Alpha = 1
Beta = 0.3
Lambda = 0.1

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

# count number of same words in search query for weighted query
def count(query):
    w = {}
    for x in query:
        if x not in w:
            y = query.count(x)
            w[x] = y
    return w
#search query -> list of ranked docId with score
def comput_score(query,collection):
    wquery = count(query)
    score = {}

    if collection == "UofO catalog":
        windexPath = weightedindexPath
    elif collection == "Reuters21578":
        windexPath = reuterWindexPath

    with open(windexPath,'r') as f:
        windex = json.load(f)
        expanded_query = Rocchio(wquery,windex,collection)

        for q,w in expanded_query.items():
            for i,t in windex.items():
                for x in t:
                    if q == i:
                        if x[0] not in score:
                            score[x[0]] = x[1]*x[2]*w
                        else:
                            score[x[0]] += x[1]*x[2]*w
        #sort the list by score
        if score != {}:
            rank = sorted(score.items(), key=lambda item:item[1], reverse=True)
            rank = rank[:countMax]
            score = {}
        else:
            rank = None
            score = {}
        print(rank)
    return rank


def Rocchio(query,windex,collection):
    fb = rfm.loadfb(collection)
    relevant = {}
    irrelevant = {}
    count_relevant = 0
    count_irrelevant = 0

    if fb != {}:
        for q in fb:
            token = q.split()
            for term in token:
                for i in windex[term]:
                    docID = i[0]
                    tfreq = i[2]
                    if docID in fb[q]['relevant']:
                        count_relevant += 1
                        if term in relevant:
                            relevant[term] += tfreq
                        else:
                            relevant[term] = tfreq
                    elif docID in fb[q]['not relevant']:
                        count_irrelevant += 1
                        if term in irrelevant:
                            irrelevant[term] += tfreq
                        else:
                            irrelevant[term] = tfreq
    else:
        print("no feedback")

    print(count_relevant)
    print(count_irrelevant)
    for term in query:
        value = Alpha*query[term]
        query[term] = value

    for term in relevant:
        value = Beta*(relevant[term] / count_relevant)
        if term in query:
            query[term] += value
        else:
            query[term] = value

    for term in irrelevant:
        value = -Lambda*(irrelevant[term] / count_irrelevant)
        print(term)
        if term in query:
            query[term] += value
        else:
            query[term] = value
    print(query)
    return query

t = count(extractQueryTerms("text text book"))
tindex = json.load(open(weightedindexPath,'r'))
print(t)
print(Rocchio(t,tindex,"UofO catalog"))
print(Rocchio(t,tindex,"Reuters21578"))
# print(comput_score(extractQueryTerms("text"),"Reuters21578"))
# print(count(extractQueryTerms("text")))
