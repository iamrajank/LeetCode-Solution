class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        temp = set()
        nums.sort()
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                left = j + 1
                right = len(nums) - 1
                while left < right:
                    result = nums[i]+nums[j]+nums[left]+nums[right]
                    if result == target:
                        temp.add((nums[i],nums[j],nums[left],nums[right]))
                        left = left + 1
                    elif result > target:
                        right = right - 1
                    else:
                        left = left + 1
        return list(temp)



        