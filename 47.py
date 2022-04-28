class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        results = list()
        count_dict = dict()

        for num in set(nums):
            results.append([num])
            count_dict[num] = nums.count(num)

        for _ in range(len(nums) - 1):
            tmp_list = list()
            for result in results:
                for num in nums:
                    tmp = result + [num]
                    if tmp.count(num) <= count_dict[num] and tmp not in tmp_list:
                        tmp_list.append(tmp)
            results = tmp_list
        return results
