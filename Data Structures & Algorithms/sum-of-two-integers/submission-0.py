class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF
        max_int = 0x7FFFFFFF

        while (b & mask) > 0:
            carry = (a & b) << 1
            a = a ^ b
            b = carry

        return (a & mask) if b > 0 else a

        