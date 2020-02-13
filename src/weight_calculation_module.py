import importlib
import os
import json
import math
import inverted_index_construction_module as iic

indexPath = '../output/index.json'
storagePath = '../output/storage.json'
termPath = '../output/terms.json'
weightedindexPath = '../output/weightedindex.json'

def getinvertedindex():
    return iic.getIndex()

#set up list of terms with corresponding docId and tf_idf
def tf_idf():
    tfidf = {}
    docId = 0
    tfreq = 0
    with open(indexPath, 'r') as inde, open(termPath, 'r') as ter , open(storagePath, 'r') as storag:
        indexf = json.load(inde)
        termf = json.load(ter)
        storagef = json.load(storag)
        n = len(storagef)
        for q in indexf:
            lis = []
            idf = math.log10(n / len(indexf[q]))
            for t in indexf[q]:
                docId = t[0]
                #tfreq = t[1]/findMaxfrequency(f,docId)
                num = findNumOfterms(docId,termf)
                tfreq = t[1]/num
                lis.append([docId,tfreq*idf,num])
            tfidf[q] = lis
        return tfidf




#def findMaxfrequency(file, docId):
#    maxfreq = 0
#    for f in file:
#        for t in file[f]:
#            if docId == t[0] and maxfreq <= t[1]:
#                maxfreq = t[1]
#    return maxfreq

def findNumOfterms(docId,termf):
    maxNum = 0
    for g in termf:
        maxNum = len(termf[g][docId-1])
    return maxNum

def getweightedindex():
    weightedindex = tf_idf()
    with open(weightedindexPath,'w') as f:
        json.dump(weightedindex, f, sort_keys=True, indent=4,ensure_ascii=False)

#getweightedindex()
