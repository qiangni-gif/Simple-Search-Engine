import nltk
import json
from nltk.corpus import wordnet
nltk.download('wordnet')

termPath = '../output/terms.json'
def expansion(query, model, collection):
    lis = {}
    if collection == "UofO catalog":
        tPath = termPath
    else:
        tPath = termPath
    terms = json.load(open(tPath,'r'))
    if model == "Vector Space Model":
        for q in query:
            synonyms = []
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
        
        return lis#return list of synonyms with its similarity score

    elif model == "Boolean Retrieval Model":
        tokenList = query.split()
        op = ['(',')','OR','AND','AND_NOT']
        for token in tokenList:
            synonyms = []
            if token not in op:
                for syn in wordnet.synsets(token):
                    for l in syn.lemmas():
                        if any(l.name() in t for t in terms["terms"]):
                            print(l.name())
                            synonyms.append(l.name())#get synonyms
                synonyms = list(filter(lambda a:a != token, synonyms))
                if synonyms != []:
                    lis[token] = synonyms
        return lis#return list of synonyms

print(expansion(["think"],"Vector Space Model",""))
print(expansion("think AND individuals","Boolean Retrieval Model",""))
