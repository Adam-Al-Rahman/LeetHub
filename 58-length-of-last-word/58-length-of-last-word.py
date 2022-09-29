class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if (len(s.split())> 1):
            first, *mid, last = s.split()
            return len(last)
        else:
            return len(s.strip()) 
        