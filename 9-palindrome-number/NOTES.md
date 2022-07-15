- Algorithm
- Used two variable
- one to store the x string value
- another to store the reverse x string value
- check if x string and reverse x string are equal or not
​
​
Other Solution
​
```py
class Solution:
def isPalindrome(self, x: int) -> bool:
return False if x < 0 else x == int(str(x)[::-1])
```