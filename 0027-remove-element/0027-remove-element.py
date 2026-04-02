class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """

        for i, num in enumerate(nums):
            if num==val:
                nums[i]="_"
        k = sum(1 for elem in nums if isinstance(elem,int))
        nums.sort()
        # k = len(nums)
        print(nums)
        print(k)
        return k
        