class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged_array = sorted(nums1 + nums2)
        index_ = int(len(merged_array) / 2)
        if not len(merged_array) % 2:
            mid = (merged_array[index_] + merged_array[index_ - 1]) / 2
        else:
            mid = (merged_array[index_])
        return mid
