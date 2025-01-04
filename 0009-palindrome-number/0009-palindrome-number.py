class Solution:
    def isPalindrome(self, x: int) -> bool:
        pal_num = 0
        pal_copy = x
        while x > 0:
            digit = x % 10
            pal_num = pal_num * 10 + digit
            x = x // 10
        if pal_copy == pal_num:
            return True
        return False
        
        
        