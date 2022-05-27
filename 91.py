class Solution:
    """
    以範例12106由左至右看:
    1 -> 可產生 [1]
    12 -> 將2獨立看 -> 2 可以搭上任何 1 產生的組合(dp[-1])
    121 -> 將1獨立看 -> 1 可以搭上任何 12 產生的組合(dp[-1]); 將1向前與2合併看 -> 21 可搭上任何 1 產生的組合(dp[-2])
    1210 -> 將0獨立看 -> 不可獨立, 因此一定要合併看 -> 10 可搭上任何12產生的組合(dp[-2])

    歸納出幾種情形:
    新產生的數字不可獨立也不可向前合併: 0 -> 直接return 0
    新產生的數字可獨立: dp[-1] + dp[-2]
    新產生的數字可向前合併: dp[-2]
    """
    def numDecodings(self, s: str) -> int:
        if s[0] == '0':
            return 0
        valid = [str(i) for i in range(1, 27)]
        dp = [1, 1]
        for index, char in enumerate(s[1:]):
            independent = char
            dependent = f'{s[index]}{char}'
            combination = 0
            if independent not in valid and dependent not in valid:
                return 0
            if independent in valid:
                combination += dp[-1]
            if dependent in valid:
                combination += dp[-2]
            dp.append(combination)
        return dp[-1]
