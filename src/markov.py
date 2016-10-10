#!/usr/bin/python
import random
from collections import defaultdict

def open_source_text(filename):
    with open(filename,"r") as infile:
        source_text = infile.read()
    return source_text

def clean_source(source):
    source = source.replace("_","")
    source = source.replace("."," . ")
    source = source.replace(","," , ")
    source = source.replace("--"," -- ")
    source = source.replace(";"," ; ")
    source = source.replace("\n"," ")

    wordset = set(source.split())
    for word in wordset:
        if not word.lower() in wordset:
            pass
        else:
            source = source.replace(word,word.lower())
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

def generate_text(markovchain,length):
    text = []

    # choose first sequence
    current_state = random.choice(list(markovchain.keys()))

    while len(text) < length:
        next_word = random.choice(markovchain[current_state])
        current_state = current_state[1:] + tuple([next_word])
        text.append(next_word)

    return text

def main():
    source = open_source_text("../texts/pride-and-prejudice")
    source2 = open_source_text("../texts/emma")
    source3 = open_source_text("../texts/sense-and-sensibility")
    source = source + source2 + source3
    mkv = build_markov_chain(source,4)
    text = generate_text(mkv,300)
    return text

if __name__ == "__main__":
    main()

