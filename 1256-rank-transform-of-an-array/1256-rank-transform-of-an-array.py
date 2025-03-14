class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        temp_rank = {}
        rank = 1
        arr_copy = arr.copy()
        arr.sort()
        result = []
        for i in arr:
            if i not in temp_rank:
                temp_rank[i] = rank
                rank = rank + 1
        for i in arr_copy:
            result.append(temp_rank[i])
        return result
        

        