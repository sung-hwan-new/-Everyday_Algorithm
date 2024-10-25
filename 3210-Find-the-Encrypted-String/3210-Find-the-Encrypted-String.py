class Solution:
    def getEncryptedString(self, s: str, k: int) -> str:
        answer = ""
        for i in range(len(s)):
            new_index = (i + k) % len(s)
            answer += s[new_index]           
        return answer