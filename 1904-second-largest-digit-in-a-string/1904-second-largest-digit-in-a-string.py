class Solution:
    def secondHighest(self, s: str) -> int:
        temp = []
        for i in s:
            if i.isdigit():
                temp.append(i)
        if not temp:
            return -1
            
        f_large = temp[0]
        s_large = str(-1)
        for i in range(1,len(temp)):
            if temp[i] > f_large:
                s_large = f_large
                f_large = temp[i]
            elif temp[i] < f_large and temp[i] > s_large:
                s_large = temp[i]
        return int(s_large)

        