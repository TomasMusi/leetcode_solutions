class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0

        for i, value in enumerate(nums):
            if value != val:
                nums[k] = nums[i]
                k+=1
        return k