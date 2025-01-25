class Solution:
    def duplicateNumbersXOR(self, nums: List[int]) -> int:
        temp = {}
        for i in nums:
            if i not in temp:
                temp[i] = 1
            else:
                temp[i] += 1
        tem = []
        for i,j in temp.items():
            if j % 2 == 0:
                tem.append(i)
        count = 0
        if len(tem) > 1:
            for i in  tem:
                count = count ^ i
            return count
        elif len(tem) == 1:
            return tem[0]
        return 0
        

        