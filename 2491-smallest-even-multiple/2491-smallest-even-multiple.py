class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        #if n is even :-The smallest positive integer that is a multiple of both 2 and n is n    itself. This is because n is already divisible by 2.


#         If n is odd:
# The smallest positive integer that is a multiple of both 2 and n is 2 * n. Since n is odd, it is not divisible by 2. Multiplying n by 2 ensures that the result is even and also a multiple of n.

        if n % 2 == 0:  
            return n
        else:
            return 2 * n

        