class Solution:
    def reverse(self, x: int) -> int:
      min_x = -(2 ** 31)
      max_x = (2 ** 31) - 1

      sign = -1 if x < 0 else 1
      x = abs(x)

      x = int(str(x)[::-1])
      x = x * sign
      if min_x <= x <= max_x:
        return x

      return 0
