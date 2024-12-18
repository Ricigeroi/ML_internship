class Solution:
    def contains_duplicate(self, nums: List[int]) -> bool:
        return False if len(set(nums)) == len(nums) else True
