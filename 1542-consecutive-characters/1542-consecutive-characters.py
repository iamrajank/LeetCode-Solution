class Solution:
    def maxPower(self, s: str) -> int:
        count = 0
        m = 0
        i = 0
        j = 1
        for i in range(len(s)-1):
            if s[i] == s[j]:
                count = count + 1
                m = max(count,m)
                i = i + 1
                j = j + 1
            else:
                count = 0
                i = i + 1
                j = j + 1
        return m+1

        