class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        temp = set()
        for i in range(len(nums)):
            left = i + 1
            right = len(nums)-1
            target = 0
            while left < right:      
                result = nums[i]+nums[left]+nums[right]   
                if result == target:
                    temp.add((nums[i],nums[left],nums[right]))
                    left = left + 1
                elif result < target:
                    left = left + 1
                else:
                    right = right - 1
                    
        return list(temp)

       