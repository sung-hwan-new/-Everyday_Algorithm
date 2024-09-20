class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        digit = set()
        answer = []
        for num in nums:
            if num in digit:
                answer.append(num)
            else:
                digit.add(num)
        return answer