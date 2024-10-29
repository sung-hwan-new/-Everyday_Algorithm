class Solution:
    def numberOfAlternatingGroups(self, colors: List[int]) -> int:
        answer = 0
        n = len(colors)
        for i in range(n):
            if colors[i] != colors[(i + 1) % n] and colors[(i + 1) % n] != colors[(i + 2) % n]:
                answer += 1
        return answer