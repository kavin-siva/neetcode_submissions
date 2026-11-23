from functools import cache

class Solution:
    def maxCoins(self, nums: list[int]) -> int:
        balloons = [1] + nums + [1]

        @cache
        def dp(left: int, right: int) -> int:
            if left + 1 >= right:
                return 0

            best = 0
            for k in range(left + 1, right):
                coins = balloons[left] * balloons[k] * balloons[right]
                best = max(best, dp(left, k) + coins + dp(k, right))
            return best

        return dp(0, len(balloons) - 1)


        