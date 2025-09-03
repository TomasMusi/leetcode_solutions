class Solution(object):
    def singleNumber(self, nums: list[int]):

        counts = {}

        for x in nums:
            if x not in counts:
                counts[x] = 1
            else:
                counts[x] = counts[x] + 1

        for num, count in counts.items():
            if count == 1:
                return num