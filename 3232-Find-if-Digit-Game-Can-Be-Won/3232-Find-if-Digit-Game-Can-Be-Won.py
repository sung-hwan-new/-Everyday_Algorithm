class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        single_digit_sum = 0
        double_digit_sum = 0

        for num in nums:
            if 1 <= num <= 9:
                single_digit_sum += num
            elif 10 <= num <= 99:
                double_digit_sum += num

        total_sum = sum(nums)
        bob_sum_with_single_digits = total_sum - single_digit_sum
        bob_sum_with_double_digits = total_sum - double_digit_sum

        return single_digit_sum > bob_sum_with_single_digits or double_digit_sum > bob_sum_with_double_digits