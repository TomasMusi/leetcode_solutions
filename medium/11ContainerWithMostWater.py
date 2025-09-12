class Solution(object):
    def maxArea(self, height: list[int]) -> int:
        left = 0
        right = len(height) - 1
        max_area = 0

        # Loop runs till the pointers meet each other.
        while left < right:
            # the width
            width = right - left

            # we use here the min, otherwise the water would fall.
            curr_height = min(height[left], height[right])

            # Calculating curr_height, with the width.
            max_area = max(max_area, curr_height * width)

            # Always moving the smaller one.
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area




height: list[int] = [1,2,1]
s = Solution()
print(s.maxArea(height))