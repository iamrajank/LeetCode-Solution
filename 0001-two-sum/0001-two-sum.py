class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(1+i,len(nums)):
                result = nums[i] + nums[j]
                if result == target:
                    return i,j
        