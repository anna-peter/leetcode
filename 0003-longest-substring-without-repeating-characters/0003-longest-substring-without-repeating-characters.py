class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        for i in range(len(s)):
            # go through each starting letter
            # try to append until we reach a letter already seen
            seen = set()
            curr = s[i]
            length = 0
            j = i
            while j<len(s) and s[j] not in seen:
                # print('s[j] '+s[j])
                seen.add(s[j])
                length += 1
                j += 1

            max_len = max(length,max_len)
        return max_len