class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        nums = sorted(nums)
        averages = []
        while nums:
            min_num = nums.pop(0)
            max_num = nums.pop()
            averages.append((min_num + max_num) / 2)
        return min(averages)