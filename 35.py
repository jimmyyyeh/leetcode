class Solution:
    """
    延續Search in Rotated Sorted Array, 最後會留下一個最接近的數, 去比較該數與target的大小做增減即可
    """
    @staticmethod
    def find_index(target, nums):
        len_ = len(nums)
        start = 0
        end = len_ - 1
        while True:
            len_ = len(nums)
            split_ = int(len_ / 2)
            left = nums[:split_]
            right = nums[split_:]
            if target < right[0]:
                end -= len(right)
                nums = left
            else:
                start += len(left)
                nums = right
            if start == end:
                break
        return start, nums

    def searchInsert(self, nums: List[int], target: int) -> int:
        if not nums:
            return 0
        if len(nums) != 1:
            start, nums = self.find_index(nums=nums, target=target)
        else:
            start = 0
        current_num = nums[0]
        if current_num == target:
            ans = start
        elif target > current_num:
            ans = start + 1
        else:
            ans = start - 1
        ans = 0 if ans < 0 else ans
        return ans