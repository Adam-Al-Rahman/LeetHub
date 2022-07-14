class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if (len(s) == len(t)) and (len(set(s)) == len(set(t))):
            dt = {}
            st = {}
            for i in range(len(s)):
                if (s[i] not in dt) and (t[i] not in st):
                    dt[s[i]] = t[i]
                    st[i] = t[i]
                elif (s[i] not in dt) and (t[i] in st):
                    return False
                elif dt[s[i]] != t[i]:
                    return False
            return True
        else:
            return False