class Solution:
    """
    TODO
    DFS, 每一層都與前面的組合再配對一次
    """
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) < 1:
            return []
        alphabet_dict = {
            2: 'abc',
            3: 'def',
            4: 'ghi',
            5: 'jkl',
            6: 'mno',
            7: 'pqrs',
            8: 'tuv',
            9: 'wxyz'
        }
        ans = ['']
        for digit in digits:
            alphabet = alphabet_dict[int(digit)]
            ans = [ans_ + alphabet_ for alphabet_ in alphabet for ans_ in ans]
        return ans
