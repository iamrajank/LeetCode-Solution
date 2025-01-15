class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        temp_non_zero = []
        temp_zero = []
        for i in range(len(nums)):
            if nums[i] != 0:
                temp_non_zero.append(nums[i])
            else:
                temp_zero.append(nums[i])
        temp_non_zero.extend(temp_zero)
        nums.clear()
        for i in temp_non_zero:
            nums.append(i)
        return nums
        