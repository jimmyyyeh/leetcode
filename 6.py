class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        reverse = True
        position = [[0, 0, s[0]]]
        for index, char_ in enumerate(s[1:]):
            if index % (numRows - 1) == 0:
                reverse = not reverse
            last = position[-1]
            last_x, last_y = last[0], last[1]
            if not reverse:
                new_x = last_x
                new_y = last_y + 1
            else:
                new_x = last_x + 1
                new_y = last_y - 1
            position.append([new_x, new_y, char_])
        ans = ''.join([element[-1] for element in sorted(position, key=lambda x: x[1])])
        return ans
