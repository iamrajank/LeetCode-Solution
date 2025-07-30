class Solution:
    def addDigits(self, num: int) -> int:
        while num >= 10:
            result = 0
            while num > 0:
                digit = num % 10
                result = result + digit
                num = num // 10
            num = result
        return num
        