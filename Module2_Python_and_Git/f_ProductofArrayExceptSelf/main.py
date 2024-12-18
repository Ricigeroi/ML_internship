class Solution:
    def product_except_self(self, nums: List[int]) -> List[int]:
        n = len(nums)
        arr = [1] * n

        left, right = 1, 1

        for i in range(n):
            arr[i] = left
            left = left * nums[i]

        for i in range(n - 1, -1, -1):
            arr[i] = arr[i] * right
            right = right * nums[i]

        return arr
