class Solution:
    def hammingWeight(self, n: int) -> int: 
        binary_str = bin(n)[2:] 
        ones_count = binary_str.count("1")
        return int(ones_count)

s = Solution()
number = 128

print(s.hammingWeight(number))