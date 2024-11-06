class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        
        count_positive = 0
        count_negative = 0
        
        for num in nums:
            if num > 0:
                count_positive += 1
            elif num < 0:
                count_negative += 1
        
        return max(count_positive, count_negative)