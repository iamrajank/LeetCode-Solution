class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # result = nums[0]
        # for i in range(len(nums)):
        #     ans = 1
        #     for j in range(i,len(nums)):
        #         ans = ans * nums[j]
        #         result = max(result,ans)
        # return result

        n = len(nums) # size of array.

        pre, suff = 1, 1
        ans = float('-inf')
        for i in range(n):
            if pre == 0:
                pre = 1
            if suff == 0:
                suff = 1
            pre *= nums[i]
            suff *= nums[n - i - 1]
            ans = max(ans, max(pre, suff))
        return ans
        