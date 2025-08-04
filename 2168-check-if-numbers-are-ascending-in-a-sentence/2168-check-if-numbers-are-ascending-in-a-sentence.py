class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        word = s.split()
        prev = -1
        for i in word:
            if i.isdigit():
                temp = int(i)
                if temp <= prev:
                    return False
                prev = temp
        return True
        
        