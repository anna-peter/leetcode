class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        result = []
        for i in range(0,len(s), k):
            # print(i)
            # print(i+k)
            # print(s[i:i+k])
            result.append(s[i:i+k])
        rem = len(s) % k
        print(rem)
        if rem !=0:
            # we have to use fill
            result[-1]+= fill*(k-rem)

        return result
