class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        memo = {}
        
        def dfs(i: int, j: int) -> bool:
            if (i, j) in memo:
                return memo[(i, j)]
            
            # Base case: reached end of pattern
            if j == len(p):
                return i == len(s)
            
            # Check if current characters match
            first_match = i < len(s) and (p[j] == s[i] or p[j] == ".")
            
            # Handle '*' wildcard at p[j + 1]
            if j + 1 < len(p) and p[j + 1] == "*":
                # Choice 1: Skip 'char*' (0 occurrences)
                # Choice 2: Match s[i] and keep 'char*' (1+ occurrences)
                ans = dfs(i, j + 2) or (first_match and dfs(i + 1, j))
            else:
                ans = first_match and dfs(i + 1, j + 1)
                
            memo[(i, j)] = ans
            return ans
            
        return dfs(0, 0)

        