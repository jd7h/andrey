#!/usr/bin/python
import random
from collections import defaultdict

def open_source_text(filename):
    with open(filename,"r") as infile:
        source_text = infile.read()
    return source_text

def clean_source(source):
    """Clean source text by fixing capitalization and special chars."""
    source = source.replace("_","")
    source = source.replace("."," . ")
    source = source.replace(","," , ")
    source = source.replace("--"," -- ")
    source = source.replace(";"," ; ")
    source = source.replace("\n"," ")

    wordset = set(source.split())
    for word in wordset:
        if not word.lower() in wordset:
            pass # for names
        else:
            source = source.replace(word,word.lower())
    return source

def build_markov_chain(source, n=1):
    """Build a nth-n markov chain based on a source text.
    
    Keyword arguments:
    source -- cleaned source text
    n -- the desired order of the markov chain (default 1)
    """
    markov = {}
    sourcelist = source.split()
    
    for i in range(0,len(sourcelist)-n):
        t = tuple(sourcelist[i:i+n])
        if not t in markov.keys():
            markov[t] = []
        markov[t].append(sourcelist[i+n])
    return markov

def generate_text(markovchain,length=50):
    """Generate a new text based on the given Markov chain.
    
    Keyword arguments:
    markovchain -- the markov chain
    length -- desired length in words of the text (default 50)
    """
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
    source = clean_source(source)
    mkv = build_markov_chain(source,2)
    text = generate_text(mkv,300)
    print(" ".join(text))
    return text

if __name__ == "__main__":
    main()

