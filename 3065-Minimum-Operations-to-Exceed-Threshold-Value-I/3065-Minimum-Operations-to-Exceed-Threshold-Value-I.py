class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        # sorted
        answer = 0
        nums = sorted(nums)
        for i in range(len(nums)):
            if nums[i] >= k:
                answer = i
                break
        return answer