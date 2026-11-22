import math

class Solution:
    def reverse(self, x: int) -> int:
        MIN_INT = -2147483648  # -2^31
        MAX_INT = 2147483647   #  2^31 - 1
        
        res = 0
        while x != 0:
            # Extract last digit (truncating toward zero for negative x)
            digit = int(math.fmod(x, 10))
            x = int(x / 10)
            
            # Check positive overflow before multiplying by 10
            if res > MAX_INT // 10 or (res == MAX_INT // 10 and digit > MAX_INT % 10):
                return 0
            
            # Check negative overflow before multiplying by 10
            if res < int(MIN_INT / 10) or (res == int(MIN_INT / 10) and digit < int(math.fmod(MIN_INT, 10))):
                return 0
                
            res = res * 10 + digit
            
        return res

        