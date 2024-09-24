class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        evens = [num for num in nums if num % 2 == 0]
        if not evens:
            return -1
        count = Counter(evens)
        return min(count, key=lambda x: (-count[x], x))