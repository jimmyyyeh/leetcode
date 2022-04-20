class Solution:
    """
    dfs
    """
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates = set(candidates)
        level = int(target / min(candidates))
        tmp_list = [[candidate] for candidate in candidates]
        ans = list()
        if target in candidates:
            ans.append([target])
        for _ in range(level - 1):
            tmp_list = [sorted(tmp + [candidate]) for tmp in tmp_list for candidate in candidates if
                        sum(tmp + [candidate]) <= target]
            ans.extend([list(tmp) for tmp in set(tuple(tmp) for tmp in tmp_list) if sum(tmp) == target])
        return ans
