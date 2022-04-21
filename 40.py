class Solution:
    """
    兩種解題思路:
    1. 先將題目轉成set, 接著去做combination sum, 增加一個dfs return的條件: 當前的數字counter不符合題目時即return
    2. 先排序後, 依序往下走, 當candidate與前一個candidate相同時即跳過(回溯時不再重複)
    """
    # def dfs(self, tmp, ans, target, candidate, candidates, counter):
    #     if tmp and counter[candidate] < tmp.count(candidate):
    #         return
    #     elif sum(tmp) == target:
    #         ans.append(tmp.copy())
    #     elif sum(tmp) > target:
    #         return
    #     else:
    #         for index, candidate in enumerate(candidates):
    #             tmp.append(candidate)
    #             self.dfs(tmp=tmp, ans=ans, target=target, candidate=candidate, candidates=candidates[index:],
    #                      counter=counter)
    #             tmp.pop()
    #
    # @staticmethod
    # def init_candidates(candidates):
    #     candidates_unique = list()
    #     counter = dict()
    #     for candidate in sorted(candidates):
    #         if candidate not in candidates_unique:
    #             candidates_unique.append(candidate)
    #             counter[candidate] = 0
    #         counter[candidate] += 1
    #     return candidates_unique, counter
    #
    # def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
    #     if sum(candidates) < target:
    #         return []
    #     if sum(candidates) == target:
    #         return [candidates]
    #
    #     candidates, counter = self.init_candidates(candidates=candidates)
    #
    #     tmp = list()
    #     ans = list()
    #     self.dfs(tmp=tmp, ans=ans, target=target, candidate=-1, candidates=candidates, counter=counter)
    #     return ans

    def dfs(self, candidates, target, index, ans, tmp):
        if target == 0:
            ans.append(tmp.copy())
        elif target < 0:
            return
        else:
            for i, candidate in enumerate(candidates[index:]):
                index_ = index + i
                if i > 0 and candidate == candidates[index_ - 1]:
                    continue
                tmp.append(candidate)
                self.dfs(candidates=candidates, target=target - candidate, index=index_ + 1, ans=ans, tmp=tmp)
                tmp.pop()

    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        if sum(candidates) < target:
            return []
        if sum(candidates) == target:
            return [candidates]

        candidates = sorted(candidates)
        tmp = list()
        ans = list()
        self.dfs(candidates=candidates, target=target, index=0, ans=ans, tmp=tmp)
        return ans
