class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        temp = []
        # temp.append(nums[0])
        for i in range(len(nums)):
            count = 0
            for j in range(i+1):
                count = count + nums[j]
            temp.append(count)
        return temp


        