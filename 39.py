class Solution:
    """
    dfs
    """
    # def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
    #     candidates = set(candidates)
    #     level = int(target / min(candidates))
    #     tmp_list = [[candidate] for candidate in candidates]
    #     ans = list()
    #     if target in candidates:
    #         ans.append([target])
    #     for _ in range(level - 1):
    #         tmp_list = [sorted(tmp + [candidate]) for tmp in tmp_list for candidate in candidates if
    #                     sum(tmp + [candidate]) <= target]
    #         ans.extend([list(tmp) for tmp in set(tuple(tmp) for tmp in tmp_list) if sum(tmp) == target])
    #     return ans

    def dfs(self, tmp, ans, target, candidates):
        if target == 0:
            ans.append(tmp.copy())
        elif target < 0:
            return
        else:
            for index, candidate in enumerate(candidates):
                tmp.append(candidate)
                self.dfs(tmp=tmp, ans=ans, target=target - candidate, candidates=candidates[index:])
                # candidates[index:] -> 該index前的數字不考慮
                tmp.pop()
                # tmp >= 題目設定target則回溯

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates = sorted(list(set(candidates)))
        tmp = list()
        ans = list()
        self.dfs(tmp=tmp, ans=ans, target=target, candidates=candidates)
        return ans
