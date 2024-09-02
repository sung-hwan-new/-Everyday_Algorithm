class Solution:
    def checkTwoChessboards(self, coordinate1: str, coordinate2: str) -> bool:
        # 첫 번째 좌표의 열과 행
        x_1, y_1 = coordinate1
        # 두 번째 좌표의 열과 행
        x_2, y_2 = coordinate2
        
        # 문자 'a'를 기준으로 열 인덱스를 계산하고 행은 그대로 숫자로 변환
        color1 = (ord(x_1) - ord('a') + 1 + int(y_1)) % 2
        color2 = (ord(x_2) - ord('a') + 1 + int(y_2)) % 2
        
        # 두 좌표의 색상이 같은지 비교
        return color1 == color2
