class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        temp = {}
        for i in nums:
            if i not in temp:
                temp[i] = 1
            else:
                temp[i] += 1
        a = []
        for i,j in temp.items():
            if j == 1:
                a.append(i)
        return a

      
        