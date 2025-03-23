class Solution:
    def search(self, num: List[int], target: int) -> int:

        # M - 1 (Linear search) 
        # M - 2 (BS)
        l = 0
        r = len(num)-1
        while l <= r:
            mid = l + (r-l)//2
            if num[mid] == target:
                return mid
    
            elif num[l] <= num[mid]:
                if num[l] <= target and target <= num[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                if num[mid] <= target and target <= num[r]:
                    l = mid + 1
                else:
                    r = mid - 1
        return -1

            
        
            
 
    
    
    
            
        