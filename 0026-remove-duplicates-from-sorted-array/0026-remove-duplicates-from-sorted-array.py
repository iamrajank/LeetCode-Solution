class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        #    First approach

        # temp = {}
        # for i in nums:
        #     if i not in temp:
        #         temp[i] = 1
        #     else:
        #         temp[i] += 1
        # lst = []
        # for i,j in temp.items():
        #     if j > 1:
        #         lst.append(i)
        #     elif j == 1:
        #         lst.append(i)
        # nums.clear()
        # for i in lst:
        #     nums.append(i)
        # return len(nums)

        # Second approach
        temp = []
        for i in range(len(nums)):
            if nums[i] not in temp:
                temp.append(nums[i])
        nums.clear()
        for i in temp:
            nums.append(i)
        return len(nums)
        