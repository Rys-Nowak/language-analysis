from zipf_law import read_czech_words, read_voynich_words
from typing import List, Dict
import matplotlib.pyplot as plt
import numpy as np
import nltk
from nltk.util import ngrams


def extract_ngrams(text, num):
    n_grams = ngrams(text, num)
    fdist = nltk.FreqDist(n_grams)
    fdist_sorted = dict(sorted(fdist.items(), key=lambda x: x[1], reverse=True))
    return fdist_sorted


if __name__ == "__main__":
    for k, v in extract_ngrams(read_czech_words(), 2).items():
        print(k, v)

