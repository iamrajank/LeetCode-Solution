class Solution:
    def search(self, nums: List[int], k: int) -> int:
        n = len(nums)
        l = 0
        r = n - 1
        # result = -1
        while l <= r:
            mid = l + (r-l)//2
            if nums[mid] == k:
                return mid
                # result = mid
                # r = mid - 1
            elif nums[mid] > k:
                r = mid - 1
            else:
                l = mid + 1
        return -1

      
        