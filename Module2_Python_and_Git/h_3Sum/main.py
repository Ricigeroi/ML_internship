class Solution:
    def three_sum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        triplets = set()

        n = len(nums)
        for j in range(n):
            if j > 0 and nums[j] == nums[j - 1]:
                continue

            target = -nums[j]
            seen = set()
            for i in range(j + 1, n):
                number = target - nums[i]
                if number in seen:
                    triplets.add((nums[j], number, nums[i]))
                seen.add(nums[i])

        return [list(triplet) for triplet in triplets]
