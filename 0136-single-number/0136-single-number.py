class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        temp = {}
        for i in nums:
            if i not in temp:
                temp[i] = 1
            else:
                temp[i] += 1
        for i,j in temp.items():
            if j == 1:
                return i

        