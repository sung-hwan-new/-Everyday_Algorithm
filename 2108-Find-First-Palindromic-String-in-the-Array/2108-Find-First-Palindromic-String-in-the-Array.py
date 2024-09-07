class Solution:
    def firstPalindrome(self, words: List[str]) -> str:

        answer = ""
        for word in words:
            if word == word[::-1]:
                answer = word
                break

        return answer