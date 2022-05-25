class Solution:
    """
    follow up提到可以嘗試用m+n, 因此採取空間換取時間的做法
    """
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        index_1, index_2 = 0, 0
        tmp = list()
        while index_1 < m and index_2 < n:
            if nums1[index_1] <= nums2[index_2]:
                tmp.append(nums1[index_1])
                index_1 += 1
            else:
                tmp.append(nums2[index_2])
                index_2 += 1

        while index_1 < m:
            tmp.append(nums1[index_1])
            index_1 += 1

        while index_2 < n:
            tmp.append(nums2[index_2])
            index_2 += 1

        for index, num in enumerate(tmp):
            nums1[index] = num
        return nums1
