#https://stackoverflow.com/questions/53015099/calculating-minimum-edit-distance-for-unequal-strings-python
#https://web.stanford.edu/class/cs124/lec/med.pdf

import math
import numpy
import json
import importlib

vowel = ["a","e","i","o","u"]
ins_cost = 1
del_cost = 1
sub_vowel_vowel = 1
sub_consonant_consonant = 1
sub_vowel_consonant = 1

indexPath = '../output/index.json'
reuterIndexPath = '../output/reuterIndex.json'
termsPath = '../output/reuterTerms.json'
maxNum = 100

def weightedEditDistance(source, target): 

    matrix = numpy.zeros((len(source)+1,len(target)+1), dtype=numpy.int)

    for i in range(len(source)+1): 
        for j in range(len(target)+1): 

            #if source or target string is empty so directly adding insertion cost
            if i == 0 and j == 0:
                matrix[i][j] = 0
            #if source is shorter than target string so adding del_cost
            elif i == 0:  
                matrix[i][j] = matrix[i][j-1] + del_cost + 0.5
            #if source is lenger than target string so adding ins_cost
            elif j == 0: 
                matrix[i][j] = matrix[i-1][j] + ins_cost + 0.5
            else:
                if source[0] == target[0]: # assume that the first letter are always correct
            ## Adjusted the cost accordinly, insertion = 1 deletion=1 vowel-vowel substitution = 0.5 vowel-consonant substitution = 1.5 consonant-consonant substitution = 1
                    if source[i-1] in vowel and target[j-1] not in vowel:
                        matrix[i][j] = min( matrix[i][j-1] + del_cost,  
                                            matrix[i-1][j] + ins_cost,
                                            matrix[i-1][j-1] + sub_vowel_consonant if source[i-1] != target[j-1] else matrix[i-1][j-1] + 0)
                    elif source[i-1] in vowel and target[j-1] in vowel:
                        matrix[i][j] = min( matrix[i][j-1] + del_cost,  
                                            matrix[i-1][j] + ins_cost,
                                            matrix[i-1][j-1] + sub_vowel_vowel if source[i-1] != target[j-1] else matrix[i-1][j-1] + 0)
                    else:
                        matrix[i][j] = min( matrix[i][j-1] + del_cost,  
                                            matrix[i-1][j] + ins_cost,
                                            matrix[i-1][j-1] + sub_consonant_consonant if source[i-1] != target[j-1] else matrix[i-1][j-1] + 0)
                else:
                    return False
    return matrix[len(source)][len(target)]

# def getCorrection(terms):
#     correction = {}
#     f = json.load(open(indexPath, 'r'))
#     for q in terms:
#         list = {}
#         for i in f:
#             distance = weightedEditDistance(q,i)
#             if distance < len(q) and distance != False:
#                 list[i] = distance
#         list = sorted(list.items(), key=lambda item:item[1], reverse=False)
#         correction[q] = list
#         for a,b in correction.items():
#             if len(correction[a]) >= maxNum:
#                 correction[a] = b[:maxNum]
#     return correction

def getCorrection(terms,collection):
    correction = {}
    f = getterms(collection)
    for q in terms:
        lis = {}
        for i in f:
            if i.isalpha() and len(q) >= len(i):
                distance = weightedEditDistance(q,i)#match query with term
                if distance < len(q) and distance != False:
                    lis[i] = distance
        print(lis)
        lis = sorted(lis.items(), key=lambda item:item[1], reverse=False)
        correction[q] = lis
        for a,b in correction.items():
            if len(correction[a]) >= maxNum:
                correction[a] = b[:maxNum]
    return correction

def getterms(collection):
    if collection == "UofO catalog":
        tPath = indexPath
    elif collection == "Reuters21578":
        tPath = reuterIndexPath

    f = json.load(open(tPath, 'r'))
    lis = []
    for i in f:
        if i not in lis:
            lis.append(i)
    # for i in f["terms"]:
    #     for l in i:
    #         if l not in lis:
    #             lis.append(l)
    #             #print(l)
    return lis





def check(terms,collection):
    if collection == "UofO catalog":
        iPath = indexPath
    elif collection == "Reuters21578":
        iPath = reuterIndexPath

    l = []
    f = json.load(open(iPath, 'r'))
    for q in terms:
        if q not in f:
            l.append(q)
    return l

#print(getCorrection(["operoting"]))
# print(getCorrection(["lienar"]))
# print(check(['text']))
# print("operot lienar")

# print(weightedEditDistance('neihgbor','neighbour'))
# print(weightedEditDistance('levenshtein','levels'))
#print(weightedEditDistance('operot','operat'))
#print(weightedEditDistance('operoting','operating'))
