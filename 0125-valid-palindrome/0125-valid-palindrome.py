class Solution:
    def isPalindrome(self, s: str) -> bool:
        temp = ""
        a = s.lower()
        for i in a:
            if i.isalnum():
                temp = temp + i
        left = 0
        right = len(temp)-1
        while left < right:
            if temp[left] != temp[right]:
                return False
            else:
                left += 1
                right -= 1
        return True

        
     
 

        