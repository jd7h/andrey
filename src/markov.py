#!/usr/bin/python
from collections import defaultdict

def open_source_text(filename):
    with open(filename,"r") as infile:
        source_text = infile.read()
    return source_text

def build_markov_chain(source, order=1):
    markov = {}
    source = source.replace("\n"," ")
    sourcelist = source.split()
    
    for i in range(0,len(sourcelist)-order):
        t = tuple(sourcelist[i:i+order])
        if not t in markov.keys():
            markov[t] = []
        markov[t].append(sourcelist[i+order])
    return markov


