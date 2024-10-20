class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums = sorted(nums, reverse=True)
        answer = -1
        for i in range(len(nums)):
            x = i + 1
            if i == len(nums) - 1:
                if nums[i] >= x:
                    answer = x
            elif nums[i] >= x and nums[i+1] < x:
                answer = x
                break
        return answer