#!/usr/bin/python
from collections import defaultdict

def open_source_text(filename):
    with open(filename,"r") as infile:
        source_text = infile.read()
    return source_text

def clean_source(source):
    source = source.replace("_","")
    source = source.replace(",","")
    source = source.replace("--"," -- ")
    source = source.replace(";","")
    source = source.replace("\n"," ")
    return source

def build_markov_chain(source, order=1):
    markov = {}
    source = clean_source(source)
    sourcelist = source.split()
    
    for i in range(0,len(sourcelist)-order):
        t = tuple(sourcelist[i:i+order])
        if not t in markov.keys():
            markov[t] = []
        markov[t].append(sourcelist[i+order])
    return markov


