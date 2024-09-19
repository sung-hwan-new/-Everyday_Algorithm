class Solution:
    def checkString(self, s: str) -> bool:
        found_b = False
        for c in s:
            if c == 'b':
                found_b = True
            elif c == 'a' and found_b:
                return False
        return True