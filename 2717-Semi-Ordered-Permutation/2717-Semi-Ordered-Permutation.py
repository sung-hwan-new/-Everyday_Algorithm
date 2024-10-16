class Solution:
    def semiOrderedPermutation(self, nums: List[int]) -> int:
        # 1. 1과 n의 위치 구하기
        # 2. 1이 n보다 앞에 있을 경우, 필요한 이동 수 구하기
        # 3. 1이 n보다 뒤에 있을 경우, 필요한 이동 수 구하기
        first_index = nums.index(1)
        last_index = nums.index(len(nums))
        if first_index < last_index:
            answer = first_index + (len(nums) - 1 - last_index)
        else:
            answer = first_index + (len(nums) - 1 - last_index) - 1
        return answer