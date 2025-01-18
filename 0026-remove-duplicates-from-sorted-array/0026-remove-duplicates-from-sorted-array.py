class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        #First Approach (Brute force approach)
        temp = []
        for i in range(len(nums)):
            if nums[i] not in temp:
                temp.append(nums[i])
        nums.clear()
        for i in temp:
            nums.append(i)
        return len(nums)


   