#!/bin/python
import requests
from text_utils import *
from typing import List, Dict
import os
import matplotlib.pyplot as plt
import numpy as np

OUT_PATH = "out"


def create_zipf_dict(words: List[str]):
    zipf = {}
    for word in words:
        if zipf.get(word):
            zipf[word] += 1
        else:
            zipf[word] = 1

    return dict(sorted(zipf.items(), key=lambda item: -item[1]))


def plot(x, y, xlabel, ylabel, path):
    plt.figure()
    plt.plot(x, y)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.savefig(os.path.join(OUT_PATH, path))


def plot_zipf(words: Dict[str, int], path):
    ranks = np.arange(1, len(words) + 1)
    values = np.array(list(words.values()))

    plot(ranks, values, "rank", "occurencies",
         os.path.join(path, "zipf_all.jpg"))
    plot(ranks, values, "rank", "rank*occurencies",
         os.path.join(path, "zipf_coef_all.jpg"))
    plot(ranks[:300], values[:300], "rank", "occurencies",
         os.path.join(path, "zipf_300.jpg"))
    plot(ranks[:300], np.multiply(values[:300], ranks[:300]), "rank",
         "rank*occurencies", os.path.join(path, "zipf_coef_300.jpg"))
    plot(ranks[:100], values[:100], "rank", "occurencies",
         os.path.join(path, "zipf_100.jpg"))
    plot(ranks[:100], np.multiply(values[:100], ranks[:100]), "rank",
         "rank*occurencies", os.path.join(path, "zipf_coef_100.jpg"))


def read_voynich_words() -> List[str]:
    lines = requests.get(
        "https://www.ic.unicamp.br/~stolfi/voynich/mirror/reeds/docs/FSG.txt").content.decode().split("\n")
    text = filter_comments(lines)
    words = split_words_voynich(text)
    return remove_uncertain_words(words)


def dump_zipf_data(zipf: Dict[str, int], path: str):
    with open(os.path.join(OUT_PATH, path, "zipf.dat"), "w") as f:
        for word, value in zipf.items():
            f.write(f"{word}: {value}\n")

    plot_zipf(zipf, path)


def read_czech_words() -> List[str]:
    with open("kamen_a_bolest.txt", "r") as f:
        lines = f.readlines()

    text = filter_punctuation_czech(lines)
    return split_words_natural(text)


def main():
    zipf_voynich = create_zipf_dict(read_voynich_words())
    dump_zipf_data(zipf_voynich, "voynich")

    zipf_czech = create_zipf_dict(read_czech_words())
    dump_zipf_data(zipf_czech, "czech")


if __name__ == "__main__":
    main()
