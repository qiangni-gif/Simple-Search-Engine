#!/usr/bin/env python
# coding: utf-8

# In[6]:


from nltk.corpus import reuters
from nltk import bigrams
import dictionary_building_module as db
import json
from collections import defaultdict,Counter,OrderedDict


# In[7]:


#corpusPath = '../output/test.json'
corpusPath = '../output/reuterStorage.json'
allTerms = '../output/reuterTerms.json'
#allTerms = '../output/testTerms.json'

#https://web.stanford.edu/~jurafsky/slp3/slides/LM_4.pdf
#https://towardsdatascience.com/learning-nlp-language-models-with-real-data-cdff04c51c25
#https://www.analyticsvidhya.com/blog/2019/08/comprehensive-guide-language-model-nlp-python-code/
#https://stackoverflow.com/questions/46566402/forming-bigrams-of-words-in-list-of-sentences-and-counting-bigrams-using-python
#http://www.phontron.com/slides/nlp-programming-en-02-bigramlm.pdf


# In[8]:


def bigram():
    with open (corpusPath,'r') as f:
        file = json.load(f)
        pre_model = defaultdict(lambda: defaultdict(lambda: 0))
        model = defaultdict(lambda: defaultdict(lambda: 0))
        m = dict()
        i = 0
        f = open(allTerms,'r')
        terms = json.load(f)
       # term = Counter(terms['terms'][0])
        counter = Counter()
        for t in terms['terms']:
            for word in db.normalization(db.stopWordRemoval(t)):
                counter.update({word:1})
        f.close()

        for doc in file:
            # remove stop words, nltk tokenize
            sentence = db.normalization(db.stopWordRemoval(db.tokenize(doc['desc'])))
            for w1,w2 in bigrams(sentence,pad_right=True, pad_left=True):
                if not w1 is None and not w2 is None:
                    pre_model[w1][w2] +=1


            for w1, w2 in pre_model.items(): # only keep words with min frequenct > x 
                for k,v in w2.items():
#                     if v >+ 4:
                    if v > 3:
                        model[w1][k] = v
        
    #         f = open(allTerms,'r')
    #         terms = json.load(f)
    #         term = Counter(terms["0"])
            # P(w2|w1) = Count(w1w2)/Count(W2)
            
            for w1 in model:
                # total_count should be number of counts of W2 

                for w2 in model[w1]:
                    total_count = counter[w2]
                    model[w1][w2] = model[w1][w2]/total_count 
        return model


# In[9]:


def callOnce():
    model = bigram()
    with open('../output/bigramModel.json','w') as f:
        json.dump(model, f, sort_keys=True, indent=4,ensure_ascii=False)

