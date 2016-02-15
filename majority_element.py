class Solution(object):
    def majorityElement(self, nums): # 72ms
        """
        :type nums: List[int]
        :rtype: int
        """
        num_map = {}
        curr = 0
        for item in nums:
            curr = item
            if item in num_map:
                num_map[item] += 1
                if num_map[item] > len(nums)/2:
                    break
            else:
                num_map[item] = 1
        return curr

    def majorityElement2(self, nums): # 64ms
        # implement the Moore's voting algorithm: find a pair different element and delete it
        count = 0
        for i in range(0, len(nums)):
            if count == 0:
                key = nums[i]
                count = 1
            else:
                if key == nums[i]:
                    count += 1
                else:
                    count -= 1
        return key
