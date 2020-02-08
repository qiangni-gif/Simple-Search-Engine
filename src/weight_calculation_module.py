import importlib
import os
import json
import math
import inverted_index_construction_module as iic

indexPath = '../output/index.json'
storagePath = '../output/storage.json'
weightedindexPath = '../output/weightedindex.json'

def getinvertedindex():
    return iic.getIndex()

#set up list of terms with corresponding docId and tf_idf
def tf_idf():
    tfidf = {}
    docId = 0
    tfreq = 0
    with open(indexPath, 'r') as file:
        f = json.load(file)
        for q in f:
            lis = []
            try:
                idf = math.log10(numberOfdoc() / len(f[q]))
                for t in f[q]:
                    docId = t[0]
                    tfreq = t[1]/findMaxfrequency(f,docId)
                    lis.append([docId,tfreq*idf])
                tfidf[q] = lis
            except KeyError:
                print(q+" is not in the collection")
        return tfidf




def findMaxfrequency(file, docId):
    maxfreq = 0
    for f in file:
        for t in file[f]:
            if docId == t[0] and maxfreq <= t[1]:
                maxfreq = t[1]
    return maxfreq

def numberOfdoc():
    with open(storagePath, 'r') as doc:
        d = json.load(doc)
        return len(d)

def getweightedindex():
    weightedindex = tf_idf()
    with open(weightedindexPath,'w') as f:
        json.dump(weightedindex, f, sort_keys=True, indent=4,ensure_ascii=False)

#getweightedindex()
