class Solution:
    def isPalindrome(self, x: int) -> bool:
        str_ = f'{x}'
        return str_ == str_[::-1]
