class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # temp = []
        # n = len(nums)
        # k = k % n
        # for i in range(len(nums)-1,-1,-1):
        #     temp.append(nums[i])
        # r_temp = []
        # for i in range(k-1,-1,-1):
        #     r_temp.append(temp[i])
        # for i in range(len(nums)-1,k-1,-1):
        #     r_temp.append(temp[i])
        
        # nums.clear()
        # for i in r_temp:
        #     nums.append(i)
        # return nums

        # Two pointer 

        n = len(nums)
        k = k % n
        i = 0
        j = n-k-1
        while i < j:
            nums[i],nums[j] = nums[j],nums[i]
            i = i + 1
            j = j - 1

        i = n-k
        j = len(nums)-1
        while i < j:
            nums[i],nums[j] = nums[j],nums[i]
            i = i + 1
            j = j - 1
        nums.reverse()
        return nums






        