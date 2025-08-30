permutation = [3,2,1]

class Solution:
    def nextPermutation(self, nums: list[int]) -> None: 

        # finding a Pivot
        i = len(nums) - 2
        while i >= 0 and nums[i] >= nums[i+1]:
            i -= 1

        # if its the last number, we must reverse it and return it.
        if i < 0:
            nums.reverse() 
            return 
        
        j = len(nums) - 1
        while nums[j] <= nums[i]:
            j -= 1
        nums[i], nums[j] = nums[j], nums[i]

        nums[i+1:] = reversed(nums[i+1:])

 
s = Solution()
print(s.nextPermutation(permutation))


