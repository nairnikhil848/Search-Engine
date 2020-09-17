# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'

# %%
import pandas as pd
import numpy as np
import string
import random

import nltk
from nltk.corpus import brown
from nltk.corpus import reuters
# nltk.download('reuters')

from nltk.tokenize import word_tokenize
from nltk.tokenize import RegexpTokenizer

from nltk.corpus import stopwords

from nltk.stem.porter import PorterStemmer
from nltk.stem import SnowballStemmer

import math
from textblob import TextBlob as tb

import pickle
import re
from collections import Counter
import os


def hello():
    pass


def docslist():
    punctuations = set(string.punctuation)
    docslist = []
    for index, i in enumerate(reuters.fileids()):
        text = reuters.raw(fileids=[i])
        text = ''.join(ch for ch in text if ch not in punctuations)
        docslist.append(text)
    return docslist


def unique_words():
    punctuations = set(string.punctuation)
    count = 0
    docslist = []
    for index, i in enumerate(reuters.fileids()):
        text = reuters.raw(fileids=[i])
        text = ''.join(ch for ch in text if ch not in punctuations)
        docslist.append(text)

    tokenized_doc = []

    for doc in docslist:
        tokentext = word_tokenize(doc)
        tokenized_doc.append(tokentext)

    for x in range(len(reuters.fileids())):
        lowers = [word.lower() for word in tokenized_doc[x]]
        tokenized_doc[x] = lowers

    l = tokenized_doc
    allwords = [item for sublist in l for item in sublist]
    # print(allwords[0:100])
    wordsunique = set(allwords)
    wordsunique = list(wordsunique)
    return wordsunique


def search(searchsentence):
    wordsunique = unique_words()

    if(os.path.exists('D:\Projects\sem-6project\worddic_1000')):

        pickle_in = open("D:\Projects\sem-6project\worddic_1000", "rb")
        worddic = pickle.load(pickle_in)

    else:
        print("its gonna take a lot of time")

        docslist = docslist()

        for doc in docslist:
            tokentext = word_tokenize(doc)
            tokenized_doc.append(tokentext)

        for x in range(len(reuters.fileids())):
            lowers = [word.lower() for word in tokenized_doc[x]]
            tokenized_doc[x] = lowers

        def tf(word, doc):
            return doc.count(word) / len(doc)

        def n_containing(word, doclist):
            return sum(1 for doc in doclist if word in doc)

        def idf(word, doclist):
            return math.log(len(doclist) / (0.01 + n_containing(word, doclist)))

        def tfidf(word, doc, doclist):
            return (tf(word, doc) * idf(word, doclist))

        plottest = tokenized_doc[0:1000]

        worddic = {}

        for doc in plottest:
            for word in wordsunique:
                if word in doc:
                    word = str(word)
                    index = plottest.index(doc)
                    positions = list(
                        np.where(np.array(plottest[index]) == word)[0])
                    idfs = tfidf(word, doc, plottest)
                    try:
                        worddic[word].append([index, positions, idfs])
                    except:
                        worddic[word] = []
                        worddic[word].append([index, positions, idfs])

    try:
        # split sentence into individual words
        searchsentence = searchsentence.lower()
        try:
            words = searchsentence.split(' ')
        except:
            words = list(words)
        enddic = {}
        idfdic = {}
        closedic = {}
        # remove words if not in worddic
        realwords = []
        for word in words:
            if word in list(worddic.keys()):
                realwords.append(word)
        words = realwords
        numwords = len(words)

        # make metric of number of occurances of all words in each doc & largest total IDF
        for word in words:
            for indpos in worddic[word]:
                index = indpos[0]
                amount = len(indpos[1])
                idfscore = indpos[2]
                #enddic[index] = amount

                try:
                    enddic[index].append(amount)
                except:
                    enddic[index] = []
                    enddic[index].append(amount)

                try:
                    idfdic[index].append(idfscore)
                except:
                    idfdic[index] = []
                    idfdic[index].append(idfscore)

                fullcount_order = sorted(
                    enddic.items(), key=lambda x: np.sum(x[1]), reverse=True)
                fullidf_order = sorted(
                    idfdic.items(), key=lambda x: np.sum(x[1]), reverse=True)
            # print(fullcount_order)
        # print(idfdic)
        # print(fullidf_order)

        # make metric of what percentage of words appear in each doc
        combo = []
        alloptions = {k: worddic.get(k, None) for k in (words)}
        # print(alloptions.values)
        for worddex in list(alloptions.values()):
            for indexpos in worddex:
                for indexz in indexpos:
                    combo.append(indexz)
        # print(combo)

        comboindex = combo[::3]

        combocount = Counter(comboindex)

        # print(combocount)
        for key in combocount:
            combocount[key] = combocount[key] / numwords
        combocount_order = sorted(
            combocount.items(), key=lambda x: x[1], reverse=True)

        # make metric for if words appear in same order as in search
        if len(words) > 1:
            x = []
            y = []

            # for record in [worddic[z] for z in words]:
            # for index in record:
            #      x.append(index[0])

            x = comboindex

            for i in x:
                if x.count(i) > 1:
                    y.append(i)
            y = list(set(y))

            closedic = {}
            for wordbig in [worddic[x] for x in words]:
                for record in wordbig:
                    if record[0] in y:
                        index = record[0]
                        positions = record[1]
                        try:
                            closedic[index].append(positions)
                        except:
                            closedic[index] = []
                            closedic[index].append(positions)

            x = 0
            fdic = {}
            for index in y:
                csum = []
                for seqlist in closedic[index]:
                    # print(seqlist)
                    while x > 0:
                        secondlist = seqlist
                        # print("firstlist-->",firstlist)
                        # print("secondlist-->",secondlist)
                        x = 0
                        sol = [1 for i in firstlist if i + 1 in secondlist]
                        csum.append(sol)
                        fsum = [item for sublist in csum for item in sublist]
                        fsum = sum(fsum)
                        fdic[index] = fsum
                        # print(fdic)
                        fdic_order = sorted(
                            fdic.items(), key=lambda x: x[1], reverse=True)
                        # print(seqlist)
                    while x == 0:
                        firstlist = seqlist
                        x = x + 1
        else:
            fdic_order = 0

        # print(fdic_order)
        # # also the one above should be given a big boost if ALL found together

        # #could make another metric for if they are not next to each other but still close

        return(searchsentence, words, fullcount_order, combocount_order, fullidf_order, fdic_order)

    except:

        return("")


def rank(term):

    results = search(term)
    # print(results[0])

    # get metrics
    num_score = results[2]
    per_score = results[3]
    tfscore = results[4]
    order_score = results[5]

    final_candidates = []

    # rule1: if high word order score & 100% percentage terms then put at top position
    try:
        first_candidates = []

        for candidates in order_score:
            if candidates[1] > 1:
                first_candidates.append(candidates[0])
        # print(first_candidates)

        second_candidates = []

        for match_candidates in per_score:
            if match_candidates[1] == 1:
                second_candidates.append(match_candidates[0])
            if match_candidates[1] == 1 and match_candidates[0] in first_candidates:
                final_candidates.append(match_candidates[0])
        # print(first_candidates)

    # rule2: next add other word order score which are greater than 1

        t3_order = first_candidates[0:3]
        # print(t3_order)
        for each in t3_order:
            if each not in final_candidates:
                final_candidates.insert(len(final_candidates), each)

    # rule3: next add top td-idf results
        final_candidates.insert(len(final_candidates), tfscore[0][0])
        final_candidates.insert(len(final_candidates), tfscore[1][0])

    # rule4: next add other high percentage score
        t3_per = second_candidates[0:3]
        for each in t3_per:
            if each not in final_candidates:
                final_candidates.insert(len(final_candidates), each)

    # rule5: next add any other top results for metrics
        othertops = [num_score[0][0], per_score[0]
                     [0], tfscore[0][0], order_score[0][0]]
        for top in othertops:
            if top not in final_candidates:
                final_candidates.insert(len(final_candidates), top)

    # unless single term searched, in which case just return
    except:
        othertops = [num_score[0][0], num_score[1][0],
                     num_score[2][0], per_score[0][0], tfscore[0][0]]
        for top in othertops:
            if top not in final_candidates:
                final_candidates.insert(len(final_candidates), top)

    final_candidates = list(set(final_candidates))

    return final_candidates


def result(word):

    final_candidates = rank(word)

    document_list = docslist()

    res = {}
    for i in final_candidates:
        res[i] = document_list[i][0:100]

    return res

#result('indonesia crude palm oil')
#result('indonesia palm oil')


# %%
