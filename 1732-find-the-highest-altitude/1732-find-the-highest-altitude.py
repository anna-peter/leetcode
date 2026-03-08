class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        max = 0 # this is the highest altitude
        altitudes = [0] # these are the altitudes
        curr = 0 # this keeps track of the current height
        for x in gain:
            curr = curr + x
            altitudes.append(curr)
            if curr > max:
                max = curr

        return max