class Solution:
    # def dfs(self, nums, result, results):
    #     for index, num in enumerate(nums):
    #         result.append(num)
    #         results.append(result.copy())
    #         if not nums[index + 1:]:
    #             result.pop()
    #         else:
    #             self.dfs(nums=nums[index + 1:], result=result, results=results)
    #     if result:
    #         result.pop()
    #
    # def subsets(self, nums: List[int]) -> List[List[int]]:
    #     results = [[]]
    #     self.dfs(nums=nums, result=list(), results=results)
    #     return results

    def subsets(self, nums: List[int]) -> List[List[int]]:
        results = [[]]
        for num in nums:
            results += [result + [num] for result in results]
        return results
