class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        matches = {} # store the number (and its index) and always check for its complement
        for i in range(len(nums)): 
            num = nums[i]
            complement = target - num # what we are looking for
            if complement in matches:
                return [matches.get(complement), i]
            else:
                matches[num] = i
        return []
        