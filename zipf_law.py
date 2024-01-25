#!/bin/python
import requests
from TextReader import TextReader
from typing import List, Dict
import os
import matplotlib.pyplot as plt
import numpy as np

OUT_PATH = os.path.join("out", "voynich")


def create_zipf_dict(words: List[str]):
    zipf = {}
    for word in words:
        if zipf.get(word):
            zipf[word] += 1
        else:
            zipf[word] = 1

    return dict(sorted(zipf.items(), key=lambda item: -item[1]))


def plot_zipf(words: Dict[str, int]):
    ranks = np.arange(1, len(words) + 1)
    values = np.array(list(words.values()))

    plt.figure()
    plt.plot(ranks, values)
    plt.xlabel("rank")
    plt.ylabel("occurencies")
    plt.savefig(os.path.join(OUT_PATH, "zipf_all.jpg"))

    plt.figure()
    plt.xlabel("rank")
    plt.ylabel("rank*occurencies")
    plt.plot(ranks, np.multiply(values, ranks))
    plt.savefig(os.path.join(OUT_PATH, "zipf_coef_all.jpg"))

    plt.figure()
    plt.xlabel("rank")
    plt.ylabel("occurencies")
    plt.plot(ranks[:300], values[:300])
    plt.savefig(os.path.join(OUT_PATH, "zipf_300.jpg"))

    plt.figure()
    plt.xlabel("rank")
    plt.ylabel("rank*occurencies")
    plt.plot(ranks[:300], np.multiply(values[:300], ranks[:300]))
    plt.savefig(os.path.join(OUT_PATH, "zipf_coef_300.jpg"))

    plt.figure()
    plt.xlabel("rank")
    plt.ylabel("occurencies")
    plt.plot(ranks[:100], values[:100])
    plt.savefig(os.path.join(OUT_PATH, "zipf_100.jpg"))

    plt.figure()
    plt.xlabel("rank")
    plt.ylabel("rank*occurencies")
    plt.plot(ranks[:100], np.multiply(values[:100], ranks[:100]))
    plt.savefig(os.path.join(OUT_PATH, "zipf_coef_100.jpg"))


def main():
    lines = requests.get(
        "https://www.ic.unicamp.br/~stolfi/voynich/mirror/reeds/docs/FSG.txt").content.decode().split("\n")
    reader = TextReader(lines)
    words = reader.split_words()
    words = reader.remove_uncertain_words(words)
    zipf = create_zipf_dict(words)
    with open(os.path.join(OUT_PATH, "zipf.dat"), "w") as f:
        for word, value in zipf.items():
            f.write(f"{word}: {value}\n")

    plot_zipf(zipf)


if __name__ == "__main__":
    main()
