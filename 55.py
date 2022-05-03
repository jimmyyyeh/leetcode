class Solution:
    """
    每一個點能走到的最遠距離為 index + num, 當前的點若不包含於先前最遠距離,代表這個點走不到, 即可直接中斷,
    走完所有的點之後只要判斷最後一次走是不是剛好走在最後一個點即可
    """
    def canJump(self, nums: List[int]) -> bool:
        distance = len(nums) - 1
        max_ = 0
        for index, num in enumerate(nums[:-1]):
            if index > max_:
                return False
            current_max = index + num
            if current_max < max_:
                continue
            max_ = min(distance, current_max)
        return distance == max_
