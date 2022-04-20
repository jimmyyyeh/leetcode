class Solution:
    """
    TODO
    用回溯法, 先依序隨機填數字, 當遇到不可填寫的狀況時, 則往回一步換數字填
    """

    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        nums = {str(i) for i in range(1, 10)}
        positions = [[x, y] for x in range(9) for y in range(9) if board[x][y] == '.']  # 先過濾出空白的位置
        index = 0

        used_dict = dict()  # 存放導致後面無法繼續的數字
        while index < len(positions):
            x, y = positions[index]
            position_key = f'{x},{y}'
            current = board[x][y]
            if current != '.':
                used_dict[position_key].add(current)
                # 如果該位置有數字, 代表這個位置被回溯, 因此把他去除掉
            else:
                used_dict[position_key] = set()
            row = board[x]  # 橫
            column = [board[i][y] for i in range(9)]  # 直
            starter_x = int(x / 3) * 3
            starter_y = int(y / 3) * 3
            sub_boxes = [board[i + starter_x][j + starter_y] for i in range(starter_x % 3, 3) for j in
                         range(starter_y % 3, 3)]  # 小九宮格
            nums_set = set(row).union(set(column)).union(set(sub_boxes)).union(used_dict[position_key])
            allow_set = nums - nums_set
            if allow_set:
                # 隨機抽一個數字出來填
                board[x][y] = allow_set.pop()
                index += 1
            else:
                # 要清空當前位置以及緩存的數字, 因為當重填後的數字, 其後的位置都應該重新來過
                used_dict[position_key] = set()
                board[x][y] = '.'
                index -= 1
        return board
