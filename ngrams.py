from zipf_law import read_czech_words, read_voynich_words
from typing import Dict
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import nltk
from nltk.util import ngrams


def extract_ngrams(text, num) -> Dict:
    n_grams = ngrams(text, num)
    fdist = nltk.FreqDist(n_grams)
    fdist_sorted = dict(sorted(fdist.items(), key=lambda x: x[1], reverse=True))
    return fdist_sorted


if __name__ == "__main__":
    for i in range(2, 6):
        print(f'\n{i}-grams:')
        czech_ngram_dict = extract_ngrams(read_czech_words(), i)
        czech_words_ngrams = pd.DataFrame(list(zip(czech_ngram_dict.keys(), czech_ngram_dict.values())),
                                          columns=['words', 'occurrences'])
        print('czech:')
        print(czech_words_ngrams.head())

        voynich_ngram_dict = extract_ngrams(read_voynich_words(), i)
        voynich_words_ngrams = pd.DataFrame(list(zip(voynich_ngram_dict.keys(), voynich_ngram_dict.values())),
                                            columns=['words', 'occurrences'])
        print('voynich:')
        print(voynich_words_ngrams.head())
