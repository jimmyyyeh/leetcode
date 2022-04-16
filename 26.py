class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        duplicate_set = set()
        del_count = 0
        for index, num in enumerate(nums.copy()):
            if num not in duplicate_set:
                duplicate_set.add(num)
            else:
                del nums[index - del_count]
                del_count += 1
        return len(nums)
