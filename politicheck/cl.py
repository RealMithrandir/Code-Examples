# coding=utf-8

from __future__ import division
import os,pickle,copy
import re
from collections import Counter
#import loader

def score(bag, score_bag):
    #sb = set(bag)
    #ssb = set(score_bag)
    #s = sb.intersection(ssb)
    #tot = 0.0
    #for w in s:
    #    tot+=1/dfreqs[w]
    #return tot
    
    #score_words = set(score_bag)
    #words = list(set(score_bag))
    #score = 0.0
    #for w in score_words:
    #    s = [tail_distance(w,wt) for wt in words]
    #    score+=max(s)
    #score = score/float(len(score_words))
    #return score
    return len([b for b in bag if b in score_bag])/float(len(bag))

def tail_distance(w1,w2):
    """return the difference between two words, in the form of the lenth of the differeing suffixes (eg. the
    differences between the largest and smallest, should handle most conjugations and small differences)"""
    l = min([len(w1),len(w2)])
    i = 0
    while i < l:
        if w1[i] != w2[i]: break
        i+=1
    #diff_per = -(l-max([len(w1),len(w2)]))
    diff_per = i/float(max([len(w1),len(w2)]))
    return diff_per

def words(text): return re.findall('[a-z]+', text.lower())

def Dfs(corpus):
    """calculate the document frequency for all terms in the corpus"""
    cnt = Counter()
    for d in corpus:
        s = set(d['bag'])
        for word in s:
            cnt[word] += 1
    return cnt

def parse(text, items):
    article_bag = [w for w in words(text) if len(w) > len_limit]
    for p in items:
        p['score'] = score(p['bag'],article_bag)
    #print 'sorting'
    #find some high-scoring things
    items.sort(key=lambda p:p['score'])
    items.reverse()
    return items

def pprint(item):
    print '\n'
    print item[2]+': '+item[3]
    print 'Status: '+item[0]+', '+item[1]

if __name__ == '__main__':
    print "Loading Corpus"
    path = os.getcwd()
    f_scraped = os.path.join(path,'scraper_output_1437237126.pickle')
    #f_scraped = os.path.join(path,'scraper_output.pickle')

    f = open(f_scraped,'rb')
    statements = pickle.load(f)
    f.close()
    print "Preprocessing"
    len_limit = 3
    #create statement bags
    proc = [{'statement':s,'bag':[w for w in words(s[2]+' '+s[3]) if len(w) > len_limit]} for s in statements[0:200]]
    #wait for, and parse, user input
    while True:
        txt = raw_input('Text to analyze:')
        it = parse(txt,copy.deepcopy(proc))
        for i in it[0:3]:
            print i['score']
            pprint(i['statement'])
        print '\n'
