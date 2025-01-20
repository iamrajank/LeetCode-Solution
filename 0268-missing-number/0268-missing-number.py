class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        ans = (n * (n+1))// 2
        result = ans - sum(nums)
        return result
        