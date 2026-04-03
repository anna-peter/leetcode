class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        # hashmap that maps for each value, the count
        unique_keys = {}

        for num in nums: 
            if num in unique_keys: 
                unique_keys[num] += 1
                if unique_keys[num] > len(nums)/2:
                    return num
            else: 
                unique_keys[num] = 1
        
        return max(unique_keys, key=unique_keys.get)
            
