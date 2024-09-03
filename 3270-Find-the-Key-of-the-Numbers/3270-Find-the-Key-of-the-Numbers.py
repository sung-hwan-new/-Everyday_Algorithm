class Solution:
    def generateKey(self, num1: int, num2: int, num3: int) -> int:
        # num들을 모두 4자리 숫자로 변환
        str_1 = str(num1).zfill(4)
        str_2 = str(num2).zfill(4)
        str_3 = str(num3).zfill(4)
        
        # 결과를 저장할 문자열
        answer = ""
        
        # 각 자리의 숫자를 비교하여 가장 작은 숫자를 결과에 추가
        for chr_1, chr_2, chr_3 in zip(str_1, str_2, str_3):
            min_digit = min(chr_1, chr_2, chr_3)
            answer += min_digit
        
        # 문자열을 정수로 변환하여 반환 (앞의 0 제거)
        return int(answer)