class Solution:
    def alternateDigitSum(self, n: int) -> int:
        n = str(n)
        answer = 0
        for i in range(len(n)):
            digit = int(n[i])
            if i % 2 == 0:
                answer += digit
            else:
                answer -= digit
        return answer