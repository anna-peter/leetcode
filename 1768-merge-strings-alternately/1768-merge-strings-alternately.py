class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        at = 0
        res = ""
        max_word = word1 if len(word1)>len(word2) else word2
        # print(max_word)
        while at<min(len(word1), len(word2)):
            res +=(word1[at])
            res +=(word2[at])
            # print(f"appended {word1[at]} and {word2[at]} at idx {at}")
            at+=1
        res +=(max_word[at:])
        return res
            
                
        