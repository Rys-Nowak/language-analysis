from typing import List


class TextReader:
    text: str

    def __init__(self, lines: List[str]) -> None:
        self.text = self._filter_comments(lines)

    def _filter_comments(self, lines: List[str]) -> str:
        return ''.join([line for line in lines if len(line) and line[0].isalnum()])

    def split_words(self) -> List[str]:
        return self.text.replace("=", ",").replace("-", ",").split(",")
    
    def remove_uncertain_words(self, words: List[str]) -> List[str]:
        return [word for word in words if word.isalnum()]
