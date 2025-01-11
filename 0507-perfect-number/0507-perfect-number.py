class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        ans = 0
        if num == 1:
            return False
        for i in range(1,int(num**0.5)+1):
            if num % i == 0:
                a = int(num/i)
                if num != a:
                    ans = ans + a + i
                else:
                    ans = ans + i
        if ans == num:
            return True
        return False
          