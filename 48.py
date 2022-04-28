class Solution:
    """
     寫出index位置, 即可推出:
     00 01 02      20 10 00
     10 11 12  ->  21 11 01  -> 每一個row為 x, y 位置交換, 再將row反轉
     20 21 22      22 12 02
     推敲出位置, 再透過邏輯去轉換元素即可

     參考discuss解法, 走斜角方式做更換, 只需要做一次即可
     """
    def rotate(self, matrix: List[List[int]]) -> None:
        len_ = len(matrix)
        position_dict = dict()
        for i in range(len_):
            for j in range(len_):
                position_dict[(i, j)] = matrix[i][j]

        for i in range(len_):
            for j in range(len_):
                matrix[i][j] = position_dict[(j, i)]

            matrix[i] = matrix[i][::-1]
        return matrix

        # len_ = len(matrix)
        # for i in range(len_):
        #     for j in range(i, len_):
        #         matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        #     matrix[i] = matrix[i][::-1]
        # return matrix
