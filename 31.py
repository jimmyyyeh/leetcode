class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        先從最小兩位數開始做交換,若降冪 -> 下一位
        遇到要交換的位數, 跟其右邊最小且大於自己的做交換, 接著其右邊的數做降冪

        從最右邊的位數開始, 依序往左檢查, 可交換的位數一定是在右邊(往左換會把數字變小),
        令當前迭代的數字為num, 依序迭代至右邊出現比其大的數字:
        [ 5 1 3 8 7 6 ]
        step 1. 將當前的位數與其右數字作比較, 與比其大且最小的數字做交換
        5 -> [] x
        1 -> [6] x
        8 -> [7, 6] x
        3 -> [8, 7, 6] 符合條件, 且6為當中最小之符合數
        更換完畢後為
        [ 5 1 6 8 7 3 ]
        step 2. 其右邊數再進行一次升冪排序(即6以右[3 7 8])
        [ 5 1 6 8 7 3 ] -> [5 1 6 3 7 8]
        """
        # check if the nums is in descending order
        sorted_nums = sorted(nums, reverse=True)
        if sorted_nums == nums:
            sorted_nums = sorted(sorted_nums)
            for index, num in enumerate(sorted_nums):
                nums[index] = num
            return nums

        len_ = len(nums)
        left = list()
        switch_index = 0
        for index, num in enumerate(nums[::-1]):
            switch_index = len_ - index - 1
            right = nums[switch_index + 1:]
            if not right or num >= max(right):
                continue
            # 找出右邊陣列內第一個符合條件的數及其index, 以便做交換
            right_index, right_num = next((right.index(right_num) + switch_index + 1, right_num)
                                          for index, right_num in enumerate(sorted(right)) if right_num > num)
            nums[switch_index] = right_num
            nums[right_index] = num
            # left為剩餘需要升冪排序的數
            left = nums[switch_index + 1:]
            break

        # 對剩餘的數進行升冪排序
        sorted_left = sorted(left)
        for index, num in enumerate(sorted_left):
            nums[switch_index + index + 1] = num
        return nums
