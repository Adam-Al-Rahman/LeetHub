class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if s == "":
            return True
        
        if t == "":
            return False
        
        if (len(s) == 1 and len(t) == 1):
            return s[0] == t[0]
        
        x=0
        for i in range(len(t)):
            if (x>=len(s)):
                return True
            if (s[x] == t[i]):
                x += 1
                
        if x == len(s):
            return True
        else:
            return False
        
    