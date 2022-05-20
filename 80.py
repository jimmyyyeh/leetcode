class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        num_list = list()
        count_list = list()
        for num in nums:
            if num not in num_list:
                num_list.append(num)
                count_list.append(1)
            elif count_list[-1] < 2:
                count_list[-1] += 1

        count = 0
        for index in range(len(nums)):
            if num_list:
                count += 1
                nums[index] = num_list[0]
                count_list[0] -= 1
                if count_list[0] == 0:
                    num_list = num_list[1:]
                    count_list = count_list[1:]
            else:
                nums[index] = '_'
        return count
