class Solution:
    """
    針對特殊符號的限制式做處理:
        e -> 只能出現一次, 且檢查前後是否為數字
        - + -> 只能出現起始位置 or e的後面
        . -> 只能出現一次, 不能出現在e的後面
    """
    def isNumber(self, s: str) -> bool:
        s = s.strip().lower()
        # 去除空白, 將強制轉字母為小寫
        is_num = has_e = has_dot = False
        for index, char in enumerate(s):
            if char.isdigit():
                is_num = True
            elif char == 'e':
                if not is_num or has_e:
                    return False
                has_e = True
                is_num = False
            elif char in {'-', '+'}:
                if index != 0 and s[index - 1] != 'e':
                    return False
            elif char == '.':
                if has_e or has_dot:
                    return False
                has_dot = True
            else:
                return False
        return is_num
