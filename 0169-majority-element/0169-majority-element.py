class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        temp = {}
        for i in nums:
            if i not in temp:
                temp[i] = 1
            else:
                temp[i] += 1
        n = len(nums)
        m_ele = n//2
        for i in temp:
            if temp[i] > m_ele:
                return i

        
        