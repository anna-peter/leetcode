class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # keep a left and a right pointer 
        # l tracks where the next non-zero number goes, r is the scout
        # check: if l is nonzero, we can increment l. can we increment r too?
        if len(nums)<2:
            return None
        
        l =r= 0
        while r<len(nums):
            left = nums[l]
            right = nums[r]
            if right !=0:
                # found a nonzero
                nums[l] = right
                nums[r] = left
                l+=1
            r+=1

    # [0,5,3]
    # l = 0, r=1. left=0, right=5. [5,0,3] l=1,r=2
    # left=0, right=3. [5,3,0]

    # [0,0,5,3]
    #[5,0,5,3]
