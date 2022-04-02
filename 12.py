class Solution:
    def intToRoman(self, num: int) -> str:
        roman_list = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
        thousands = int(num / 1000)
        num = num % 1000
        ans = []
        for index, n in enumerate(str(num)[::-1]):
            n_num = int(n)
            quotient_char = roman_list[index * 2 + 1]
            reminder_char = roman_list[index * 2]
            next_quotient_char = roman_list[index * 2 + 2]
            if n_num == 4:
                ans.append(f'{quotient_char}{reminder_char}')
            elif n_num == 9:
                ans.append(f'{next_quotient_char}{reminder_char}')
            else:
                quotient = int(n_num / 5)
                reminder = int(n_num % 5)
                ans.extend(reminder * [reminder_char] + quotient * [quotient_char])
        ans = ''.join(ans)[::-1]
        ans = thousands * roman_list[-1] + ans
        return ans
