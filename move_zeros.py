class Solution(object):
    def moveZeroes(self, nums): # 1044ms
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        i = 0
        none_zero_count = 0
        length = len(nums)
        while i < (length - none_zero_count):
            if nums[i] == 0:
                none_zero_count += 1
                for j in range(i, length - 1):
                    nums[j], nums[j+1] = nums[j+1], nums[j]
                i -= 1
            i += 1
    
    def moveZeros2(self, nums): # 72ms
        if len(nums) == 0:
            return
        position = 0
        for i in range(0, len(nums)):
            if nums[i] != 0:
                nums[position] = nums[i]
                position += 1
        for i in range(position, len(nums)):
            nums[i] = 0    
