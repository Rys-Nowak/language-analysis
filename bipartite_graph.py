from typing import Tuple
import pandas as pd
from zipf_law import read_czech_words, read_voynich_words


def create_bipartite_graph(text) -> Tuple[dict, dict]:
    counter = {}
    graph = {}

    for i in range(0, len(text) - 1):
        curr_word = text[i]
        next_word = text[i + 1]
        if curr_word not in counter:
            counter[curr_word] = {}
            graph[curr_word] = 0

        if next_word not in counter[curr_word]:
            counter[curr_word][next_word] = 1
            graph[curr_word] += 1
        else:
            counter[curr_word][next_word] += 1

    return counter, graph


if __name__ == "__main__":
    czech_graph, czech_count = create_bipartite_graph(read_czech_words())

    df_czech = pd.DataFrame(czech_graph).fillna(0).astype(int)
    count_czech = pd.DataFrame.from_dict(czech_count, orient='index',
                                         columns=['count']).sort_values(by=['count'], ascending=False)

    print(df_czech)
    print(count_czech.head(10))

    voynich_graph, voynich_count = create_bipartite_graph(read_voynich_words())

    df_voynich = pd.DataFrame(voynich_graph).fillna(0).astype(int)
    count_voynich = pd.DataFrame.from_dict(voynich_count, orient='index',
                                         columns=['count']).sort_values(by=['count'], ascending=False)

    print(df_voynich)
    print(count_voynich.head(10))
