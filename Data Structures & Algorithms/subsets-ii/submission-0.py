class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        res = []
        subset = []

        def backtrack(start: int):
            res.append(subset.copy())

            for i in range(start, len(nums)):
                # Skip duplicate elements at the same recursion level
                if i > start and nums[i] == nums[i - 1]:
                    continue

                subset.append(nums[i])
                backtrack(i + 1)
                subset.pop()

        backtrack(0)
        return res

        