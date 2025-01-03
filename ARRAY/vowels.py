class Solution:
    def reverseVowels(self, s: str) -> str:
        result = ""
        vowels = "aeiouAEIOU"
        s_vowels = []
        # Find vowels
        for char in s:
            if char in vowels:
                s_vowels.append(char)
        # Swap vowels
        for cnt, char in enumerate(s):
            if char in vowels:
                result += s_vowels[-1]
                s_vowels.pop(-1)
            else:
                result += char
        return result