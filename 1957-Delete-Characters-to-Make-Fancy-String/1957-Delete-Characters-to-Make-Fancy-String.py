class Solution:
    def makeFancyString(self, s: str) -> str:
        answer = []
        
        for i in range(len(s)):
            if i > 1 and s[i] == s[i - 1] == s[i - 2]:
                continue
            answer.append(s[i])
        return ''.join(answer)