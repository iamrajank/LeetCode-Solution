class Solution:
    def isPalindrome(self, x: int) -> bool:
        reverse_digit = 0
        x_copy = x
        while x > 0:
            digit = x % 10
            reverse_digit = reverse_digit * 10 + digit
            x = x // 10
        
        if x_copy == reverse_digit:
            return True
        return False
        