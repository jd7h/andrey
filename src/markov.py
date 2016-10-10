#!/usr/bin/python
import random
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

def generate_text(markovchain,length):
    text = []

    # choose first sequence
    current_state = random.choice(list(markovchain.keys()))

    while len(text) < length:
        print("Current state:",current_state)
        next_word = random.choice(markovchain[current_state])
        print("next_word:",next_word)
        current_state = current_state[1:] + tuple([next_word])
        text.append(next_word)

    return text

def main():
    source = open_source_text("../texts/pride-and-prejudice-full-text")
    mkv = build_markov_chain(source,5)
    text = generate_text(mkv,1000)
    return text

if __name__ == "__main__":
    main()

