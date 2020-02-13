#https://stackoverflow.com/questions/53015099/calculating-minimum-edit-distance-for-unequal-strings-python
#https://web.stanford.edu/class/cs124/lec/med.pdf

import math
import numpy
import json

vowel = ["a","e","i","o","u"]
ins_cost = 1
del_cost = 1
sub_vowel_vowel = 1
sub_consonant_consonant = 1
sub_vowel_consonant = 1

indexPath = '../output/index.json'

maxNum = 6

def weightedEditDistance(source, target): 

    matrix = numpy.zeros((len(source)+1,len(target)+1), dtype=numpy.int)

    for i in range(len(source)+1): 
        for j in range(len(target)+1): 

            #if source or target string is empty so directly adding insertion cost
            if i == 0 and j == 0:
                matrix[i][j] = 0
            #if source is shorter than target string so adding del_cost
            elif i == 0:  
                matrix[i][j] = matrix[i][j-1] + del_cost
            #if source is lenger than target string so adding ins_cost
            elif j == 0: 
                matrix[i][j] = matrix[i-1][j] + ins_cost
            else:
                if source[0] == target[0]: # assume that the first letter are always correct
            ## Adjusted the cost accordinly, insertion = 1 deletion=1 vowel-vowel substitution = 0.5 vowel-consonant substitution = 2 consonant-consonant substitution = 1
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

def getCorrection(terms):
    correction = {}
    with open(indexPath, 'r') as file:
        f = json.load(file)
        for q in terms:
            list = {}
            for i in f:
                distance = weightedEditDistance(q,i)
                if distance < len(q) and distance != False:
                    list[i] = distance
            list = sorted(list.items(), key=lambda item:item[1], reverse=False)
            correction[q] = list
            for a,b in correction.items():
                if len(correction[a]) >= maxNum:
                    correction[a] = b[:maxNum]
    return correction


def check(terms):
    l = []
    with open(indexPath, 'r') as file:
        f = json.load(file)
        for q in terms:
            if q not in f:
                l.append(q)
    return l

#print(getCorrection(["operot"]))
#print(getCorrection(["lienar"]))
#print("operot lienar")

#print(weightedEditDistance('neihgbor','neighbour'))
#print(weightedEditDistance('levenshtein','levels'))
