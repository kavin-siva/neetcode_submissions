class Solution:

    def longestPalindrome(self, s: str) -> str:
        res_start, res_len = 0, 0

        def expand(l: int, r: int) -> None:
            nonlocal res_start, res_len
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > res_len:
                    res_start = l
                    res_len = r - l + 1
                l -= 1
                r += 1

        for i in range(len(s)):
            expand(i, i)  # Odd length
            expand(i, i + 1)  # Even length

        return s[res_start : res_start + res_len]

        