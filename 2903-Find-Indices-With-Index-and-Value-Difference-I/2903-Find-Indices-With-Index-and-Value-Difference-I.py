class Solution:
    def findIndices(self, nums: List[int], indexDifference: int, valueDifference: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(len(nums)):
                # abs(i - j) >= indexDifference
                # abs(nums[i] - nums[j]) >= valueDifference
                # 두 가지 조건을 만족시키면 answer에 i, j append, break
                if abs(i - j) >= indexDifference and abs(nums[i] - nums[j]) >= valueDifference:
                    return [i, j]
        return [-1, -1]