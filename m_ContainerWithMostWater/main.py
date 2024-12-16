class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_volume = 0
        left = 0
        right = len(height) - 1

        while left < right:
            max_volume = max(
                max_volume,
                (right - left) * min(height[left], height[right])
            )
            print(f'r={right}, l={left}')
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_volume