class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        sorted_arr = sorted(set(arr))
        rank_map = {x: i + 1 for i, x in enumerate(sorted_arr)}
        return [rank_map[x] for x in arr]