class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # for index_x, x in enumerate(nums):
        #     for index_y, y in enumerate(nums):
        #         if index_x != index_y and x + y == target:
        #             return [index_x, index_y]

        max_num = max(nums)

        indexes = [None] * (max_num + 1)
        # for i in range (max_num):
        #     indexes[i] = None

        for index_y, y in enumerate(nums):
            indexes[y] = index_y

        for index_x, x in enumerate(nums):
            to_find = target - x
            if indexes[to_find] is not None and index_x != indexes[to_find]:
                return [index_x, indexes[to_find]]
