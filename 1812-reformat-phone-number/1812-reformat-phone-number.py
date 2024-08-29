class Solution:
    def reformatNumber(self, number: str) -> str:
        reformat_number = number.replace(' ', '').replace('-', '')
        answer = []

        while len(reformat_number) > 4:
            answer.append(reformat_number[:3])
            reformat_number = reformat_number[3:]
        
        if len(reformat_number) == 4:
            answer.append(reformat_number[:2])
            answer.append(reformat_number[2:])
        else:
            answer.append(reformat_number)
        
        return '-'.join(answer)