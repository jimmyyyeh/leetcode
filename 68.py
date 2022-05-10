class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        results = list()

        tmp_len = 0  # 緩存當前所有可行元素的總長度
        start_index = 0
        for index, word in enumerate(words):
            word_len = len(word)
            sub_words = words[start_index: index + 1]
            tmp_len += word_len
            total_len = tmp_len + len(sub_words) - 1  # 每個字元之間至少間隔一個space

            if total_len > maxWidth:
                if len(sub_words) == 2:
                    # 針對一行只有一個元素的狀況做處理
                    results.append(sub_words[0].ljust(maxWidth, ' '))
                else:
                    sub_words = words[start_index: index]
                    space_len = maxWidth - (tmp_len - word_len)
                    reminder = space_len % (len(sub_words) - 1)  # 多餘的空白空間會由左至右依序遞減
                    is_divide = not reminder  # 看是否可以整除
                    spaces = ' ' * (space_len // (len(sub_words) - 1))
                    result = sub_words[0]
                    for sub_word in sub_words[1:]:
                        if not is_divide and reminder:
                            result += f'{spaces} {sub_word}'
                            reminder -= 1
                        else:
                            result += f'{spaces}{sub_word}'
                    results.append(result)
                tmp_len = word_len
                start_index = index

        # 處理剩餘元素
        sub_words = words[start_index:]
        result = sub_words[0]

        for sub_index, sub_word in enumerate(sub_words[1:]):
            result += f' {sub_word}'
        results.append(result.ljust(maxWidth, ' '))
        return results
