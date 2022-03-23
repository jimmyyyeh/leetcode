class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans = list()
        for index, num in enumerate(nums):
            num_1 = target - num
            if num_1 in nums:
                num_1_index = nums.index(num_1)
                if index != num_1_index:
                    ans = [index, nums.index(num_1)]
                    break
        return ans
