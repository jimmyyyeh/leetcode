class Solution:
    """
    兩種解題思路:
    1. inplace的排序法, 時間複雜度可參考下文: https://hackmd.io/@Aquamay/BylVMPFkiu
    2. 由左至右的指針, 根據數量將0加在左邊, 2放在右邊, 最後將left與right之間的全部更新成1
    """
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # insert sort
        # for index in range(1, len(nums)):
        #     num = nums[index]
        #     sorted_nums = nums[:index]
        #     for index_ in range(len(sorted_nums)):
        #         num_ = nums[index_]
        #         if num_ > num:
        #             nums[index], nums[index_] = nums[index_], nums[index]
        # return nums

        # select sort
        # len_ = len(nums)
        # for index in range(len_):
        #     for index_ in range(index, len_ - 1):
        #         num = nums[index]
        #         num_ = nums[index_ + 1]
        #         if num > num_:
        #             nums[index], nums[index_ + 1] = nums[index_ + 1], nums[index]

        # bubble sort
        # len_ = len(nums)
        # for index in range(len_ - 1, -1, -1):
        #     for index_ in range(index):
        #         num = nums[index_]
        #         num_ = nums[index_ + 1]
        #         if num > num_:
        #             nums[index_], nums[index_ + 1] = nums[index_ + 1], nums[index_]
        # return nums

        # quick sort
        # def partition(self, nums, start, end):
        #     pivot = nums[start]
        #     left = start + 1
        #     right = end
        #     while True:
        #         while left <= right and nums[left] <= pivot:
        #             left += 1
        #         while left <= right and nums[right] >= pivot:
        #             right -= 1
        #         if left > right:
        #             break
        #         else:
        #             nums[left], nums[right] = nums[right], nums[left]
        #     nums[start], nums[right] = nums[right], nums[start]
        #     return right
        #
        # def quick_sort(self, nums, start, end):
        #     if start < end:
        #         pivot = self.partition(nums=nums, start=start, end=end)
        #         self.quick_sort(nums, start, pivot - 1)
        #         self.quick_sort(nums, pivot + 1, end)
        #
        # def sortColors(self, nums: List[int]) -> None:
        #     """
        #     Do not return anything, modify nums in-place instead.
        #     """
        #     self.quick_sort(nums=nums, start=0, end=len(nums) - 1)
        #     return nums

        left = 0
        right = len(nums) - 1
        for num in nums.copy():
            if num == 0:
                nums[left] = 0
                left += 1
            elif num == 2:
                nums[right] = 2
                right -= 1

        for index in range(left, right + 1):
            nums[index] = 1

        return nums
