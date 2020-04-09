import nltk
import json
from nltk.corpus import wordnet
nltk.download('wordnet')

# https://stackoverflow.com/questions/13226629/wordnet-query-expansion-step-by-step
# https://pythonprogramming.net/wordnet-nltk-tutorial/

termPath = '../output/terms.json'
UotermPath = '../output/UOterms.json'
def expansion(query, model, collection):
    lis = {}
    if collection == "UofO catalog":
        tPath = UotermPath
    else:
        tPath = termPath
    terms = json.load(open(tPath,'r'))
    tokenList = query.split()
    if model == "Vector Space Model":
        for q in tokenList:
            synonyms = []
            if q not in lis:
                for syn in wordnet.synsets(q):
                    for l in syn.lemmas():
                        if any(l.name() in t for t in terms["terms"]):
                            synonyms.append(l.name())#get synonyms
                            # synonyms.append([l.name(),q.wup_similarity(l)])#get synonyms with its similarity score
            synonyms = list(filter(lambda a:a != q, synonyms))
            if synonyms != []:
                lis[q] = synonyms
        # if lis != {}:
        #     lis = sorted(lis.items(), key=lambda item:item[1], reverse=True)
        
        return lis#return list of synonyms

    elif model == "Boolean Retrieval Model":
        op = ['(',')','OR','AND','AND_NOT']
        for token in tokenList:
            synonyms = []
            if token not in op and token not in lis:
                for syn in wordnet.synsets(token):
                    for l in syn.lemmas():
                        if any(l.name() in t for t in terms["terms"]):
                            #print(l.name())
                            synonyms.append(l.name())#get synonyms
                synonyms = list(filter(lambda a:a != token, synonyms))
                if synonyms != []:
                    lis[token] = synonyms
        return lis#return list of synonyms
# q = "think"
# p = "think quick"
# print(q.split())
# print(p.split())
# v = expansion("think","Vector Space Model","")
# b = expansion("think AND individuals","Boolean Retrieval Model","")
# print(v)
# print(b)

# for i in expansion("think AND individuals","Boolean Retrieval Model",""):
#     print(i)
#     print(b[i])
