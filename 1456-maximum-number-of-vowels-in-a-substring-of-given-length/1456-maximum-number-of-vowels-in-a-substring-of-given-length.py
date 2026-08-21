class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        # define vowels
        vowels = {'a', 'e','i','o','u'}

        max_len = curr_count = 0
        # brute force: loop through each starting idx i and take the max number of vowels
        # worst case o(n^2) if k=n
        # for i in range(len(s)):
        #     curr_count = 0
        #     for v in range(k):
        #         if i+v >= len(s):
        #             continue
        #         if s[i+v] in vowels:
        #             curr_count+=1
        #     max_len = max(curr_count, max_len)

        # count vowels in s[:k] - initialize
        for v in range(k):
            if s[v] in vowels:
                curr_count +=1
        max_len = curr_count
        # only values that change are the leftmost (dropped) and rightmost (added)
        for i in range(len(s)-k):
            # count - vowel if s[i] is a vowel
            # count + vowel if s[i+k] is a vowel 
            if s[i] in vowels:
                curr_count -=1
            if s[i+k] in vowels:
                curr_count +=1
            max_len = max(curr_count, max_len)


        return max_len