class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        # split, enumerate, startswith
        answer = -1
        word_list = sentence.split(" ")
        for i, word in enumerate(word_list):
            if word.startswith(searchWord):
                return i + 1
                break
        return -1