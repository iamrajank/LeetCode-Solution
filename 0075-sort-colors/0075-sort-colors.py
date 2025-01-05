class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
   

        temp_zero = []
        temp_one = []
        temp_two = []
        for i in range(len(nums)):
            if nums[i] == 0:
                temp_zero.append(nums[i])
            elif nums[i] == 1:
                temp_one.append(nums[i])
            else:
                temp_two.append(nums[i])
        nums.clear()
        for i in temp_zero:
            nums.append(i)
        for i in temp_one:
            nums.append(i)
        for i in temp_two:
            nums.append(i)
        return nums
        