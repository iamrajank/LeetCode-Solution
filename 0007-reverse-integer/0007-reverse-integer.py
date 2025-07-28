class Solution:
    def reverse(self, x: int) -> int:
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        result = 0
        x_isnegative = x < 0
        if x_isnegative:
            x = -x
        while x > 0:
            digit = x % 10
            result = result * 10 + digit
            x = x // 10
            if result > INT_MAX or result < INT_MIN:
                return 0
        if x_isnegative:
            result = -result
        return result
            
        
        