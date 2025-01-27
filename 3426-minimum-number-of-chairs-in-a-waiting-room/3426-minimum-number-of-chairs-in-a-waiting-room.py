class Solution:
    def minimumChairs(self, s: str) -> int:
        count = 0
        max_count = 0
        for i in range(len(s)):
            if s[i] == "E":
                count += 1
                max_count = max(count,max_count)
            else:
                count -= 1
        return max_count


        