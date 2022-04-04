class Solution:
    """
    假設排序後的值為: [-14, -3, 0, 1, 2, 5, 8, 19]
    從左至右固定一個值 ex: -14
    起始指標為index, index+1, last_index(即-14, -3, 19)
    相對位置假設:
    sum_3 target -> 需使sum_3++ 才能更靠近target (移動左指標, 總和增加)
    target sum_3 -> 需使sum_3-- 才能更靠近target (移動右指標, 總和減少)
    """
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums = sorted(nums)
        ans = None
        for index_1, num_1 in enumerate(nums[:-2]):
            left = index_1 + 1
            right = len(nums) - 1
            while left < right:
                tmp = nums[left] + nums[right] + num_1
                if ans is None:
                    ans = tmp
                else:
                    ans = tmp if abs(tmp - target) < abs(ans - target) else ans
                if tmp < target:
                    left += 1
                elif tmp > target:
                    right -= 1
                else:
                    return target
        return ans
