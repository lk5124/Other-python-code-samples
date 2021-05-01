import nltk
nltk.download("book")
from nltk.book import *
import pandas as pd
import numpy as np




with open('moby.txt', 'r') as f:
    moby_raw = f.read()


moby_tokens = nltk.word_tokenize(moby_raw)
text1 = nltk.Text(moby_tokens)

def answer_one():

    answ = len(set(text1))/len(text1)

    return answ

def answer_two():

    dist = FreqDist(nltk.word_tokenize(moby_raw))
    answ = (dist['whale'] + dist['Whale'])/len(text1)*100

    return answ

def answer_three():

    dist = FreqDist(nltk.word_tokenize(moby_raw))
    n_dist = dict(sorted(dist.items(), reverse=True, key=lambda item: item[1]))
    answ = []
    c = 0
    n = 20
    for item in n_dist.keys() :
        answ.append((item,n_dist[item]))
        c+=1
        if c==n:
            break
    return answ

def answer_four():

    dist = FreqDist(nltk.word_tokenize(moby_raw))
    vocab1 = dist.keys()

    freqwords = [w for w in vocab1 if len(w) > 5 and dist[w] > 150]
    answ = sorted(freqwords)
    return answ

#answer_four()

def answer_five():

    max_w = ''
    max_l =0

    for word in set(nltk.word_tokenize(moby_raw.lower())) :
        if len(word) > max_l :
            max_w = word
            max_l = len(word)

    answ = (max_w, max_l)

    return answ

def answer_six():

    dist = FreqDist(nltk.word_tokenize(moby_raw))
    n_dist = dict(sorted(dist.items(), reverse=True, key=lambda item: item[1]))

    answ = []
    for item in n_dist.keys() :
        if n_dist[item] > 2000 and item.isalpha() :
            answ.append((n_dist[item], item))

    return answ

def answer_seven():

    sentences = nltk.sent_tokenize(moby_raw)

    answ = len(text1)/len(sentences)

    return answ

def answer_eight():

    pos = nltk.pos_tag(text1)

    pos_freqs = {}

    for pair in pos :
        if pair[1] in pos_freqs :
            pos_freqs[pair[1]] += 1
        else :
            pos_freqs[pair[1]] = 1

    pos_freqs_sorted = dict(sorted(pos_freqs.items(), reverse=True, key=lambda item: item[1]))

    #print(pos_freqs)
    #print(pos_freqs_sorted)
    answ = []

    c = 0
    for item in pos_freqs_sorted.keys() :
        answ.append((item,pos_freqs[item]))
        c+=1
        if c==5 :
            break

    return answ
