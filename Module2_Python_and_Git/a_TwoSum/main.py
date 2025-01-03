from typing import List


class Solution:
    def two_sum(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        n = len(nums)

        for i in range(n):
            number = target - nums[i]
            if number in dict.keys():
                return dict[number], i
            else:
                dict[nums[i]] = i
