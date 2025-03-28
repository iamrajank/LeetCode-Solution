class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0
        elif n == 2 and nums[1] >= nums[0]:
            return 1
        elif nums[n-1] >= nums[n-2]:
            return n-1
        else:
            for i in range(len(nums)-1):
                if nums[i] > nums[i-1] and nums[i] > nums[i+1]:
                    return i
        