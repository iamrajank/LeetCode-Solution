class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        i = 0
        k = k % n
        j = n-k-1
        while i < j:
            nums[i],nums[j] = nums[j],nums[i]
            i = i + 1
            j = j - 1
        i = n-k
        j = n - 1
        while i < j:
            nums[i],nums[j] = nums[j],nums[i]
            i = i + 1
            j = j - 1
        i = 0
        j = n - 1
        while i < j:
            nums[i],nums[j] = nums[j],nums[i]
            i = i + 1
            j = j - 1
        return nums

        