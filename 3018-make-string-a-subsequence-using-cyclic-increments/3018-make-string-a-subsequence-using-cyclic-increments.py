class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
      s = collections.deque(str2)

      for c in str1:
        nc = chr((ord(c) - ord('a') + 1) % 26 + ord('a'))

        if ((len(s) > 0) and (c == s[0] or nc == s[0])):
          s.popleft()
    
      return len(s) == 0
        