class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
      # //Brute force approach 

        # for i in range(len(arr)):
        #     j = 1
        #     var = -99999
        #     for j in range(i+1,len(arr)):           
        #         if arr[j] > var:
        #             var = arr[j]
        #     arr[i] = var
        # arr[len(arr)-1] = -1
        # return arr
  # Optimal Solution

        m = -1
        for i in range(len(arr)-1,-1,-1):
            temp = m
            if arr[i] > m:
                temp = arr[i]
            arr[i] = m
            m = temp
        return arr

        