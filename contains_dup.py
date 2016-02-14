class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) == 0:
            return False

        num_map = {}
        for num in nums:
            """ 
            Do not use 'if num in num_map.keys()', which would be extremely
            slow.
            """
            if num in num_map: 
                return True
            else:
                num_map[num] = True
        return False

if __name__ == "__main__":
    test_list_1 = []
    test_list_2 = [1,2,3,4,5,1,2,3,4,5]
    test_list_3 = [12,23,34,123,4321,1,321,432,543,12312]
    test_list_4 = [1,1,1,1,1,1]
    so = Solution()

    print so.containsDuplicate(test_list_1)
    print so.containsDuplicate(test_list_2)
    print so.containsDuplicate(test_list_3)
    print so.containsDuplicate(test_list_4)


