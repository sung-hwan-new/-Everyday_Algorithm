class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        nums = set()
        tmp = ""
        for c in word:
            if c.isnumeric():
                tmp += c
            elif tmp:
                nums.add(int(tmp))
                tmp = ""
        if tmp:
            nums.add(int(tmp))
        return len(nums)