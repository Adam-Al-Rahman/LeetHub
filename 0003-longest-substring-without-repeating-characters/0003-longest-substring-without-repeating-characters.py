from typing import List

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

      if (set(s) == len(s)):
        return len(s)
      
      ss = ""
      ss_len = 0

      for x in s:
        if x not in ss:
          ss += x 
          ss_len = max(ss_len, len(ss))
        else:
          ss = ss.split(x)[1] + x 

      return ss_len



          


      
