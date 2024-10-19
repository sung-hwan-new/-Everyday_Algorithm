class Solution:
    def countAsterisks(self, s: str) -> int:
        answer = 0
        word_list = s.split("|")
        for i in range(0, len(word_list), 2):
            answer += word_list[i].count('*')
        return answer