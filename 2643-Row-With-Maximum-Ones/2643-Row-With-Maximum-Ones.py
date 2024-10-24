class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        answer = [0, 0]
        prev_cnt = 0
        for i, row in enumerate(mat):
            one_cnt = row.count(1)
            if one_cnt > prev_cnt:
                answer = [i, one_cnt]
                prev_cnt = one_cnt
        return answer