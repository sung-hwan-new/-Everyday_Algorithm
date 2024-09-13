class Solution:
    def repeatedCharacter(self, s: str) -> str:
        answer = set()
        for char in s:
            if char in answer:
                return char
            answer.add(char)