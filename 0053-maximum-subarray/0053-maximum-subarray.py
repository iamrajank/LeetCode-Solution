class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Better 
        # result = nums[0]
        # for i in range(len(nums)):
        #     ans = 0
        #     for j in range(i,len(nums)):
        #         ans = ans + nums[j]
        #         result = max(result,ans)
        # return result
        
        # Optimal

        s=0
        res=nums[0]
        for i in range(len(nums)):
            s+=nums[i]
            if s>res:
                res=s
            if s<0:
                s=0
        return res

        