INT_MAX = 2**31 - 1
INT_MIN = 2**31
class Solution:
    def reverse(self, x: int) -> int:
        neg = x < 0
        bound = INT_MAX if not neg else INT_MIN
        x = abs(x)
        ret = 0
        while x > 0:
            digit = x % 10
            x //= 10
            if (bound - digit) // 10 < ret:
                return 0
            ret = 10 * ret + digit
        return -ret if neg else ret