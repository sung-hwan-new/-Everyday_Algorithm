class Solution:
    def addDigits(self, num: int) -> int:
        
        while num >= 10:
            digit_sum = 0
            while num > 0:
                digit_sum += num % 10  # num의 마지막 자릿수를 temp에 더함
                num //= 10        # num을 10으로 나누어 자릿수를 줄임
            num = digit_sum            # 자릿수의 합을 num에 할당
        return num


        # answer = []
        # for i in str(num):
        #     answer += i
        # print(answer)

# - num의 자릿수 쪼개기
# - while문으로 쪼갠 자릿수 숫자 더하기
# - if문으로 더이상 자릿수 쪼갤 수 없으면 break
# - 쪼개서 더한 횟수를 answer로 출력

        # while num >= 10:
        #     digit_sum = 0
        #     for c in str(num):
        #         print(c)
        #     break
        # return num

        
        # while num >= 10:
        #     answer = 0
        #     for i in str(num):
