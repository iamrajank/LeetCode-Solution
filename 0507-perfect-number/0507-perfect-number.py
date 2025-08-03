class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        result = 0
        if num == 1:
            return False

        for i in range(1, int(num ** 0.5)+1):
            if num % i == 0:
                a = int(num/i)
                if num != a:
                    result = result + a + i
                else:
                    result = result + i
        if result == num:
            return True
        return False
        