class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        countS, countT = {}, {}
        print(s)

        for i in range(len(s)):

            countS[s[i]] = 1 + countS.get(s[i], 0) #second value of get if the value that retunr if three is not that key
            countT[t[i]] = 1 + countT.get(t[i], 0)
            print(type(countS.get("a")))
        return countS == countT
