class Solution:
    def romanToInt(self, s: str) -> int:
        m = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        result = 0
        ans = 0
        for i in range(len(s)):
            # if m[s[i]] == 1:
            #     ans = ans + 1
            if i < len(s) - 1 and m[s[i]] < m[s[i+1]]:
                ans = ans - m[s[i]]
            else:
                ans = ans + m[s[i]]
        return ans


        