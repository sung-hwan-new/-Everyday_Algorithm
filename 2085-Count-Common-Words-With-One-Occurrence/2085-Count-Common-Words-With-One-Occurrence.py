class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        answer = 0
        c1 = Counter(words1)
        c2 = Counter(words2)
        keys = set(list(c1.keys()) + list(c2.keys()))
        for key in keys:
            if c1[key] == 1 and c2[key] == 1:
                answer += 1
        return answer