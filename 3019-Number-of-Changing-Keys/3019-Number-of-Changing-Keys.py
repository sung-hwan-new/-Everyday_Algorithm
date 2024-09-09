class Solution:
    def countKeyChanges(self, s: str) -> int:
        answer = 0
        # 문자열을 소문자로 변환
        s = s.lower()
        
        # for문을 사용하여 앞의 문자와 뒤의 문자를 비교
        for i in range(len(s) - 1):
            # 앞의 문자와 뒤의 문자가 다르면 키 변경 횟수 증가
            if s[i] != s[i + 1]:
                answer += 1
        
        return answer