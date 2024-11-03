class Solution:
    def minOperations(self, nums: List[int]) -> int:
        prev = nums[0]
        answer = 0
        for i in range(1, len(nums)):
            if nums[i] <= prev:
                increment = prev - nums[i] + 1
                answer += increment
                prev = nums[i] + increment
            else:
                prev = nums[i]
        return answer