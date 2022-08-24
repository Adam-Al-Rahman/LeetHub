class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        def check(reduced_n):
            if reduced_n == 1:
                return True
            elif reduced_n%3 != 0 or reduced_n == 0:
                return False
            return check(reduced_n/3)
        
        return check(n)
            