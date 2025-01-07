class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        temp = {}
        n = len(nums)
        for i in nums:
            if i not in temp:
                temp[i] = 1
            else:
                temp[i] += 1
        for i,j in temp.items():
            majority_ele = n // 2
            if j > majority_ele:
                return i

        