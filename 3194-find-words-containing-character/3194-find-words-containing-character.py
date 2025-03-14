class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        temp = []
        for i in range(len(words)):
            if x in words[i]:
                temp.append(i)
        return temp
        