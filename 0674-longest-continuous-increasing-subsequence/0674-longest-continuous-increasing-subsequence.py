class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        count = 0
        max_count = 0
        i = 0
        j = 1
        for i in range(len(nums)-1):
            if nums[i] < nums[j]:
                count = count + 1
                max_count = max(max_count,count)
                i = i +1
                j = j + 1
            else:
                count = 0
                i = i + 1
                j = j + 1
        return max_count+1


        