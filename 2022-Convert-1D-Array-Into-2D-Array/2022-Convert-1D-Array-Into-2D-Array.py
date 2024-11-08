class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:

        answer = []
        if len(original) != m * n:
            return []

        for i in range(0, len(original), n):
            answer.append(original[i:i+n])

        return answer