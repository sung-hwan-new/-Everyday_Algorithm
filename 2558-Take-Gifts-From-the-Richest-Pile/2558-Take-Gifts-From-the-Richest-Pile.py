class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        for i in range(k):
            gifts = sorted(gifts)
            max_gifts = gifts.pop()
            gifts.append(int(math.sqrt(max_gifts)))
        return sum(gifts)