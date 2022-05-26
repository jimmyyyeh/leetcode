class Solution:
    def dfs(self, nums, result, results):
        for index, num in enumerate(nums):
            origin = result.copy()
            result.append(num)
            if result not in results:
                results.append(result.copy())
            if nums[index + 1:]:
                self.dfs(nums=nums[index + 1:], result=result, results=results)
            result = origin

    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        results = [[]]
        nums = sorted(nums)
        self.dfs(nums=nums, results=results, result=list())
        return results
