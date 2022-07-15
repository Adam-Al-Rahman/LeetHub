class Solution:
    def isPalindrome(self, x: int) -> bool:
        x_str = str(x)
        x_rstr = str(x)[::-1]
        for i in range(len(x_str)):
            if x_str[i] != x_rstr[i]:
                return False
        return True
            
        