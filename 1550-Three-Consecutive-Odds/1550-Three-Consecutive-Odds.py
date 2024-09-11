class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        answer = False
        cnt = 0
        for num in arr:
            if num % 2 == 0:
                cnt = 0
            else:
                cnt += 1
            if cnt >= 3:
                answer = True
                break
        return answer