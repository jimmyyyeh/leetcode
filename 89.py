class Solution:
    """
    原先使用back tracking做到16會ETL,
    根據gray code定義做bitwise operation, 參考下解:
    https://desolve.medium.com/%E5%BE%9Eleetcode%E5%AD%B8%E6%BC%94%E7%AE%97%E6%B3%95-11-bitwise-operation-1-3117c4ce925d

    """
    # def helper(self, sequence, result, len_):
    #     if len(result) == len_:
    #         return
    #     previous = result[-1]
    #     for index, char in enumerate(previous):
    #         replacement = '0' if char == '1' else '1'
    #         next_ = previous[:index] + replacement + previous[index + 1:]
    #
    #         if next_ in sequence:
    #             result.append(next_)
    #             sequence_copy = sequence.copy()
    #             sequence_copy.remove(next_)
    #             self.helper(sequence=sequence_copy, result=result, len_=len_)
    #             if len(result) == len_:
    #                 return
    #
    #     if len(result) != len_:
    #         result.pop()
    #     return
    #
    # def grayCode(self, n: int) -> List[int]:
    #     sequence = [f'{i:0{n}b}' for i in range(2 ** n)]
    #     result = [sequence[0]]
    #     self.helper(sequence=sequence[1:], result=result, len_=len(sequence))
    #     result = [int(num, 2) for num in result]
    #     return result

    def grayCode(self, n: int) -> List[int]:
        return [num ^ (num >> 1) for num in range(2 ** n)]
