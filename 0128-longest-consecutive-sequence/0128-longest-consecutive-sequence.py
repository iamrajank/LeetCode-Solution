class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 1
        count = 1
        nums.sort()
        if len(nums) == 0:
            return 0
        for i in range(1,len(nums)):
            if nums[i] != nums[i-1]:
                if nums[i] == nums[i-1] + 1:
                    count = count + 1
                    longest = max(longest,count)
                else:
                    count = 1
        return longest

        