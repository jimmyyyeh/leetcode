class Solution:
    def mySqrt(self, x: int) -> int:
        previous = 0
        for i in range(0, 46341 + 1):
            if x == i * i:
                return i
            elif previous * previous < x < i * i:
                return previous
            else:
                previous = i

