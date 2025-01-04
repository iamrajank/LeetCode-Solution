class Solution:
    def reverse(self, x: int) -> int:
        reverse_digit = 0
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31  
        is_negative = x < 0
        if is_negative:
            x = -x  
        while x > 0:
            digit = x % 10
            reverse_digit = reverse_digit * 10 + digit
            x = x // 10
            if reverse_digit > INT_MAX or reverse_digit < INT_MIN:
                return 0
        if is_negative:
            reverse_digit = -reverse_digit
     
        return reverse_digit
        
    
        
        