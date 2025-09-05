class Solution(object):
    def plusOne(self, digits: list[int]) -> list[int]:
        number: int = 0
        digit: list[str] = [] 
        for x in digits:
            number = number * 10 + x

        number += 1

        for ch in str(number):
            digit.append(int(ch))

        return digit


s = Solution()
nums = [9]

print(s.plusOne(nums))