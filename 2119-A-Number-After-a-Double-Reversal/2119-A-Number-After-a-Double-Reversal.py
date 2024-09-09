class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        return num == 0 or num % 10 != 0

# 조건식은 그 자체로 True나 False값을 반환할 수 있다.
# 조건식을 하나의 질문이라고 생각하면 된다.