class Solution:
    """
    TODO
    固定兩數, 只需要判斷第三數是不是能在扣除兩數後的list內找到即可
    """
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []
        nums = sorted(nums)
        ans = set()
        for index_1, num_1 in enumerate(nums[:-2]):
            if index_1 != 0 and num_1 == nums[index_1 - 1]:
                continue
            need = dict()  # 用dict效能會比set好
            for index_2, num_2 in enumerate(nums[index_1 + 1:]):
                num_3 = -(num_1 + num_2)
                if num_3 not in need:  # 透過need來判斷第三數是不是能在接下來的陣列內找到, 若可以即可推出正確答案
                    need[num_2] = 1
                else:
                    ans.add((num_1, num_2, num_3))  # 直接add進去set不需要再判斷是否存在
        ans = list(ans)
        return ans
