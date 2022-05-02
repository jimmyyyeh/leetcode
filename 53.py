class Solution:
    """
    TODO
    如: [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    起始最大(current_max) = 起始總和(current_sum) = -2 (nums[0])
    1 -> sum = (-2 + 1) = -1, num > current_sum -> current_sum = num = 1
      -> current_max(-2) < num(1) -> current_max = 1
    -3 -> sum = (1 - 3) = -2, num < current_sum -> current_sum = current_sum = -2
       -> current_max(1) > num(-3) -> current_max = 1
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
