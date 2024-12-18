class Solution:
    def max_sub_array(self, nums: List[int]) -> int:
        max_sum = nums[0]
        current_sum = max_sum

        for item in nums[1:]:
            current_sum = max(item, current_sum + item)
            max_sum = max(current_sum, max_sum)

        return max_sum
