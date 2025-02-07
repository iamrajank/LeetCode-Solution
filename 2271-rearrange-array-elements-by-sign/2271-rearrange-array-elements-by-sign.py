class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:

        # Brute Force Approach
        temp_pos = []
        temp_neg = []
        for i in range(len(nums)):
            if nums[i] >= 0:
                temp_pos.append(nums[i])
            else:
                temp_neg.append(nums[i])
        for i in range(len(temp_pos)):
            nums[2 * i] = temp_pos[i]
        for i in range(len(temp_neg)):
            nums[2 * i + 1] = temp_neg[i]
        return nums

 













        