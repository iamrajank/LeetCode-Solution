class Solution:
    def findTheDifference(self, s: str, t: str) -> str:

        # Brute force
        # for i in t:
        #     if t.count(i) > s.count(i):
        #         return i

        temp = {}
        for i in t:
            if i not in temp:
                temp[i] = 1
            else:
                temp[i] += 1
        for i in s:
            temp[i] = temp[i] - 1
        for i in temp:
            if temp[i] == 1:
                return i


      
        