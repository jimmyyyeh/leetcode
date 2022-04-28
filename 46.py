class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        results = [[num] for num in nums]

        for _ in range(len(nums) - 1):
            results = [result + [num] for result in results for num in nums if num not in result]
        return results
