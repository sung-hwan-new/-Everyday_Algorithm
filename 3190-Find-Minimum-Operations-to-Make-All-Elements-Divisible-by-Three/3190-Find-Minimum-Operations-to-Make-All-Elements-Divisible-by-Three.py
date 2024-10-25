class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        answer = 0
        for num in nums:
            remainder = num % 3
            if remainder == 1 or remainder == 2:
                answer += 1
        return answer