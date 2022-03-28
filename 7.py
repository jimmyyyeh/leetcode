class Solution:
    def reverse(self, x: int) -> int:
        max_ = 2 ** 31 - 1
        min_ = -2 ** 31
        multiplier = -1 if x < 0 else 1
        value_str = f'{abs(x)}'
        reversed_value = int(value_str[::-1]) * multiplier
        reversed_value = 0 if (reversed_value > max_ or reversed_value < min_) else reversed_value
        return reversed_value
