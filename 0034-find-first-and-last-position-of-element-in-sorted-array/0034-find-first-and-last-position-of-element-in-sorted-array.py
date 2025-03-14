class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        # Brute Force
        temp = []
        for i in range(len(nums)):
            if nums[i] == target:
                temp.append(i)
                break
        for i in range(len(nums) -1,-1,-1):
            if nums[i] == target:
                temp.append(i)
                break
        if len(temp) == 0:
            return [-1,-1]
        return temp
        