class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """

        # reverse means just to swap leftmost and rightmost that didnt get swapped until we're at the middle
        l=0
        r=len(s)-1
        while l<r:
            temp = s[l]
            s[l]=s[r]
            s[r]=temp
            l+=1
            r-=1
        