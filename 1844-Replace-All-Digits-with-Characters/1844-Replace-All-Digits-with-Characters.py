class Solution:
    def replaceDigits(self, s: str) -> str:
        result = []
        for i in range(len(s)):
            if s[i].isdigit():
                new_char = chr(ord(s[i - 1]) + int(s[i]))
                result.append(new_char)
            else:
                result.append(s[i])
        
        return ''.join(result)