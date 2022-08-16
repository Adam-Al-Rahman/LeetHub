class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        char_frequency = {}
        
        for i in s:
            if i in char_frequency:
                char_frequency[i] += 1
            else:
                char_frequency[i] = 1
                
        print(char_frequency)
        
        for i in range(len(s)):
            if char_frequency[s[i]] == 1:
                return i
        return -1
                