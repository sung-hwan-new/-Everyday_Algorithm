class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        answer = 0
        for i in sentences:
            word_count = len(i.split())
            if word_count > answer:
                answer = word_count
        return answer