class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        from collections import Counter

        nums_counter = Counter(nums)
        answer = 0
        m = max(nums_counter.values())
        for k, v in nums_counter.items():
            if v == m:
                answer += v
        return answer  