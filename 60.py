import math


class Solution:
    """
    兩種解題思路:
    1. dfs, 搜尋到題目給的k為止return, 基本上會ETL, 修正後還是只有5% faster
    2. 每一個根節點下, 都會有(n-1)!的子節點數, 因此可以透過餘數, 商數的方式快速裁切樹枝, 依序求出解, 參考下解:
        https://medium.com/@ryanyang1221/leetcode-challenge-permutation-sequence-6-20-5b08b3f13683
    """

    # def dfs(self, nums, n, k, ans_dict):
    #     for index, num in enumerate(nums):
    #         if ans_dict['count'] == k:
    #             return
    #         ans_dict['tmp'] = f'{ans_dict["tmp"]}{num}'
    #         next_ = nums[:index] + nums[index + 1:]
    #         if not next_:
    #             ans_dict['count'] += 1
    #             ans_dict['ans'] = ans_dict['tmp']
    #             ans_dict['tmp'] = ans_dict['tmp'][:-1]
    #             return
    #         self.dfs(nums=next_, n=n, k=k, ans_dict=ans_dict)
    #         ans_dict['tmp'] = ans_dict['tmp'][:-1]
    #
    # def getPermutation(self, n: int, k: int) -> str:
    #     nums = list(range(1, n + 1))
    #
    #     factorial = 1
    #     for i in range(1, n + 1):
    #         factorial *= i
    #     half = factorial / 2
    #     if k > half:
    #         k = factorial - k + 1
    #         nums.reverse()
    #     # 當結果超過階層總數的1/2, 逆著做
    #     ans_dict = {
    #         'count': 0,
    #         'ans': '',
    #         'tmp': ''
    #     }
    #
    #     self.dfs(nums=nums, n=n, k=k, ans_dict=ans_dict)
    #     return ans_dict['ans']

    def getPermutation(self, n: int, k: int) -> str:
        nums = list(range(1, n + 1))
        ans = ''
        while nums:
            n -= 1
            factorial_ = math.factorial(n)
            index = math.ceil(k / factorial_) - 1
            num = nums[index]
            nums = nums[:index] + nums[index + 1:]
            k -= index * factorial_
            ans = f'{ans}{num}'
        return ans
