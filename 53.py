class Solution:
    """
    TODO
    兩種解題思路:
    1. Kadane’s Algorithm
        如: [-2, 1, -3, 4, -1, 2, 1, -5, 4]
        起始最大(current_max) = 起始總和(current_sum) = -2 (nums[0])
        1 -> sum = (-2 + 1) = -1, num > current_sum -> current_sum = num = 1
          -> current_max(-2) < num(1) -> current_max = 1
        -3 -> sum = (1 - 3) = -2, num < current_sum -> current_sum = current_sum = -2
           -> current_max(1) > num(-3) -> current_max = 1
    2. 分治法, 參考下解:
        https://leetcode.com/problems/maximum-subarray/discuss/1595195/
    """
    def maxSubArray(self, nums: List[int]) -> int:
        current_sum = nums[0]
        current_max = nums[0]

        for num in nums[1:]:
            # current_sum += num
            # if num > current_sum:
            #     current_sum = num
            # if current_sum > current_max:
            #     current_max = current_sum
            current_sum = max(num, current_sum + num)
            # 如果當前數字比當前總數大, 則當前總數直接定為當前數字
            current_max = max(current_sum, current_max)
            # 當前最大跟當前總數比
        return current_max

    # def find(self, start, end, nums):
    #     if start > end:
    #         return (-2) ** 31 - 1
    #
    #     mid = (start + end) // 2
    #     left = self.find(nums=nums, start=start, end=mid - 1)
    #     right = self.find(nums=nums, start=mid + 1, end=end)
    #
    #     left_sum = right_sum = 0
    #
    #     sum_ = 0
    #     for i in range(mid - 1, start - 1, -1):
    #         sum_ += nums[i]
    #         left_sum = max(left_sum, sum_)
    #
    #     sum_ = 0
    #     for i in range(mid + 1, end + 1):
    #         sum_ += nums[i]
    #         right_sum = max(right_sum, sum_)
    #
    #     return max(left, right, (left_sum + right_sum + nums[mid]))
    #
    # def maxSubArray(self, nums: List[int]) -> int:
    #     return self.find(start=0, end=len(nums) - 1, nums=nums)
