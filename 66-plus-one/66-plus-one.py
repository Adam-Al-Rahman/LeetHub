class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s = int()
        length = len(digits)
        for i in range(length):
            s += (digits[i] * pow(10, (length-(i + 1))))
        return [int(i) for i in str(s+1)]