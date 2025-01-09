class Solution:
    def fib(self, n: int) -> int:
        # if n == 0:
        #     return 0
        # elif n == 1:
        #     return 1
        # elif n > 1:
        #     a = 0
        #     b = 1
        #     c = a + b
        #     a = b
        #     b = c
        # return c

        if n <= 1:
            return n
        else:
            return self.fib(n-1) + self.fib(n-2)

        