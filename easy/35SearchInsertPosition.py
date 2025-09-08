class Solution(object):
    # Using Binary Search we always need to have sorted array!
    def binarySearch(self ,nums, target):
        # We have to choose, two pointers, first at the start and second at the end.
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid
            
            elif nums[mid] < target:
                left = mid + 1

            else:
                right = mid - 1

        return left
    
    def searchInsert(self, nums, target):
        return self.binarySearch(nums,target)


nums = [2, 4, 7, 10, 13, 18]
target = 5

s = Solution()
print(s.searchInsert(nums, target))