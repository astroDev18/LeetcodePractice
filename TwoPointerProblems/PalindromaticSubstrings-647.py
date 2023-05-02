class Solution:
    def countSubstrings(self, s: str):
        res = 0
        for i in range(len(s)):
            l = r = i
            # even values
            while l >= 0 and r < len(s) and s[l] == s[r]:
                res += 1
                l -= 1
                r += 1
            # increment pointers
            l = i
            r = i + 1
            # odd values
            while l >= 0 and r < len(s) and s[l] == s[r]:
                res += 1
                l -= 1
                r += 1

        return res
print(Solution.countSubstrings(0, "aaa"))

