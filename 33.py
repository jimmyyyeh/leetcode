class Solution:
    """
    find the index of target in nums, but constraints on O(log n) runtime complexity
    使用二分法, 如果是偶數就對切, 奇數則切成 (x, x+1), 左邊較少, 反過來也可,
    設定起始range為 0 ~ len(nums)-1(即最小~最大index)
    接著判斷該數在左邊還是右邊,
    左邊->最大index-右邊總數(往左邊推進),
    右邊->最小index+左邊總數(往右邊推進),
    如範例 [0, 1, 2, 3, 4, 5], target 2 -> range = 0 ~ 5
    -> [0, 1, 2] [3, 4, 5] -> range -> 0 ~ (5 - 3)
    -> [0, 1] [2]-> range -> (0 + 2) ~ 2
    當範圍內的數只有一個, 即為正解, 且此時index=start=end
    """
    def search(self, nums: List[int], target: int) -> int:
        if target not in nums:
            return -1

        len_ = len(nums)
        start = 0
        end = len_ - 1

        while True:
            len_ = len(nums)
            split_ = int(len_ / 2)
            left = nums[:split_]
            right = nums[split_:]
            if target in left:
                end -= len(right)
                nums = left
            else:
                start += len(left)
                nums = right
            if start == end:
                break
        ans = start
        return ans
