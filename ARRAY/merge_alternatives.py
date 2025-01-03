class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = ""
        length_1 = len(word1)
        length_2 = len(word2)        
        length = max([length_1, length_2])
        for i in range(length):
            if i < length_1:
                result += word1[i]
            if i < length_2:
                result += word2[i]

        return result