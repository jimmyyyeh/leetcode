class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        # return target in nums
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return True
            if nums[left] == nums[right] == nums[mid]:
                left += 1
                right -= 1
            elif nums[left] <= nums[mid]:
                # 表示此段仍在遞增中
                if nums[left] <= target < nums[mid]:
                    # target在遞增範圍內, 直接從mid往左切
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                # 表示此段正在遞減中
                if nums[right] >= target > nums[mid]:
                    # target在遞增範圍內, 直接從mid往右切
                    left = mid + 1
                else:
                    right = mid - 1
        return False
