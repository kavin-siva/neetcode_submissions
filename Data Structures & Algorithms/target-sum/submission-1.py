class Solution:
    def findTargetSumWays(self, nums: list[int], target: int) -> int:
        total = sum(nums)
        if abs(target) > total or (target + total) % 2 != 0:
            return 0

        subset_target = (target + total) // 2
        dp = [0] * (subset_target + 1)
        dp[0] = 1

        for num in nums:
            for s in range(subset_target, num - 1, -1):
                dp[s] += dp[s - num]

        return dp[subset_target]


        