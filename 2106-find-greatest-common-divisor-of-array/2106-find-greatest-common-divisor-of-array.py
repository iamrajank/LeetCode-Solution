class Solution:
    def findGCD(self, nums: List[int]) -> int:
        a = max(nums)
        b = min(nums)

        if b == 0:
            return a
        else:
            return math.gcd(b,a%b)
        