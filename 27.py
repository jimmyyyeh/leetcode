class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        del_count = 0
        for index, num in enumerate(nums.copy()):
            if num == val:
                del nums[index - del_count]
                del_count += 1
        return len(nums)
