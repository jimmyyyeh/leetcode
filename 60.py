class Solution:
    def dfs(self, nums, n, k, ans_dict):
        for index, num in enumerate(nums):
            if ans_dict['count'] == k:
                return
            ans_dict['tmp'] = f'{ans_dict["tmp"]}{num}'
            next_ = nums[:index] + nums[index + 1:]
            if not next_:
                ans_dict['count'] += 1
                ans_dict['ans'] = ans_dict['tmp']
                ans_dict['tmp'] = ans_dict['tmp'][:-1]
                return
            self.dfs(nums=next_, n=n, k=k, ans_dict=ans_dict)
            ans_dict['tmp'] = ans_dict['tmp'][:-1]

    def getPermutation(self, n: int, k: int) -> str:
        nums = list(range(1, n + 1))

        factorial = 1
        for i in range(1, n + 1):
            factorial *= i
        half = factorial / 2
        if k > half:
            k = factorial - k + 1
            nums.reverse()
        # 當結果超過階層總數的1/2, 逆著做
        ans_dict = {
            'count': 0,
            'ans': '',
            'tmp': ''
        }

        self.dfs(nums=nums, n=n, k=k, ans_dict=ans_dict)
        return ans_dict['ans']
