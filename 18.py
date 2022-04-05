class Solution:
    """
    固定一個值 x, target_new = target - x
    再延伸3sum的解法
    """
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums = sorted(nums)
        ans = set()
        for index_1, num_1 in enumerate(nums):
            # 固定 num_1, target_new = target - num_1
            target_new = target - num_1
            for index_2, num_2 in enumerate(nums[index_1 + 1:]):
                tmp = dict()
                for index_3, num_3 in enumerate(nums[index_1 + index_2 + 2:]):
                    left = target_new - num_2 - num_3
                    if left not in tmp:
                        tmp[num_3] = 1
                    else:
                        ans.add((num_1, num_2, num_3, left))
        return list(ans)
