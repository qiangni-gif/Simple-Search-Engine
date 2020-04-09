import importlib
import os
import json
import math
import inverted_index_construction_module as iic

indexPath = '../output/index.json'
storagePath = '../output/storage.json'
reuterIndexPath = '../output/reuterIndex.json'
reuterStorage = '../output/reuterStorage.json'
termPath = '../output/terms.json'
UOtermPath = '../output/UOterms.json'
weightedindexPath = '../output/weightedindex.json'
reuterWindexPath = '../output/reuter_weightedindex.json'

def getinvertedindex():
    return iic.getIndex()

#set up list of terms with corresponding docId and tf_idf
def tf_idf(iPath,tPath,sPath):
    tfidf = {}
    docId = 0
    tfreq = 0
    with open(iPath, 'r') as inde, open(tPath, 'r') as ter , open(sPath, 'r') as storag:
        indexf = json.load(inde)
        termf = json.load(ter)
        storagef = json.load(storag)
        n = len(storagef)
        for q in indexf:
            lis = []
            idf = math.log10(n / len(indexf[q]))
            for t in indexf[q]:
                docId = t[0]
                num = findNumOfterms(docId,termf)
                #comput term frequency
                #tfreq = t[1]/findMaxfrequency(f,docId)
                #tfreq = t[1]/num
                tfreq = t[1]
                #tfreq = 1 + math.log10(t[1])
                lis.append([docId,idf,tfreq,num])
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
    weightedindex = tf_idf(indexPath,UOtermPath,storagePath)
    with open(weightedindexPath,'w') as f:
        json.dump(weightedindex, f, sort_keys=True, indent=4,ensure_ascii=False)

    reuterWindex = tf_idf(reuterIndexPath,termPath,reuterStorage)
    with open(reuterWindexPath,'w') as f:
        json.dump(reuterWindex, f, sort_keys=True, indent=4,ensure_ascii=False)

#getweightedindex()
