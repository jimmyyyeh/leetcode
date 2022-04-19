class Solution:
    """
    延續Search in Rotated Sorted Array, 先判斷target是否在左邊, 最終取得最左邊target的index, 反之取得最右邊
    """
    @staticmethod
    def from_right(target, start, end, left, right):
        if target in right:
            start += len(left)
            nums = right
        else:
            end -= len(right)
            nums = left
        return start, end, nums

    @staticmethod
    def from_left(target, start, end, left, right):
        if target in left:
            end -= len(right)
            nums = left
        else:
            start += len(left)
            nums = right
        return start, end, nums

    def get_index(self, target, nums, func):
        len_ = len(nums)
        start = 0
        end = len_ - 1

        while True:
            len_ = len(nums)
            split_ = int(len_ / 2)
            left = nums[:split_]
            right = nums[split_:]
            start, end, nums = func(target=target, start=start, end=end, left=left, right=right)
            if start == end:
                break
        ans = start
        return ans

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if target not in nums:
            return [-1, -1]
        left = self.get_index(target=target, nums=nums, func=self.from_left)
        right = self.get_index(target=target, nums=nums, func=self.from_right)
        return [left, right]
