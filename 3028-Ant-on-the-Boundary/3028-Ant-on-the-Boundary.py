class Solution:
    def returnToBoundaryCount(self, nums: List[int]) -> int:
        
        answer = 0
        location = 0

        for num in nums:
            location += num
            if location == 0:
                answer += 1
        return answer