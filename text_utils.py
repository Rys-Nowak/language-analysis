from typing import List
import re


def filter_comments(lines: List[str]) -> str:
    return ''.join([line for line in lines if len(line) and line[0].isalnum()])


def filter_punctuation_czech(lines: List[str]) -> str:
    return ''.join([re.sub('[^ěščřžýáíéóúůďťňa-z]+', ' ', line.lower()) for line in lines])


def split_words_natural(text: str) -> List[str]:
    return ' '.join(text.split(" ")).split()


def split_words_voynich(text: str) -> List[str]:
    return text.replace("=", ",").replace("-", ",").split(",")


def remove_uncertain_words(words: List[str]) -> List[str]:
    return [word for word in words if word.isalnum()]
