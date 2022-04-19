class Solution:
    """
    數獨規則: 橫的不能重複, 直的不能重複, 九宮格內不可重複
    橫的驗一次, 直的驗一次, 九宮格各驗一次即可(當x位於每個九宮格的左上角時), 不需每一個位數都驗
    """
    @staticmethod
    def valid(nums):
        return len(nums) - nums.count('.') == len(set(nums)) - 1

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for x in range(9):
            # 驗橫排
            if not self.valid(nums=board[x]):
                return False
            # 驗直排
            column = [board[i][x] for i in range(9)]
            if not self.valid(nums=column):
                return False
            # 驗九宮格
            if x in [0, 3, 6]:
                for y in [0, 3, 6]:
                    sub_boxes = [board[i + x][j + y] for i in range(x % 3, 3) for j in range(y % 3, 3)]
                    if not self.valid(nums=sub_boxes):
                        return False
        return True
