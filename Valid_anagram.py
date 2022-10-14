def isAnagram(s, t):
    if len(s) != len(t):
        return False
    countS, countT = {}, {}
    for i in range(len(s)):
        countS[s[i]] = 1 + countS.get(s[i],0)
        countT[t[i]] = 1 + countT.get(t[i],0)
    for a in s:
        if countS[a] != countT.get(a,0):
            return False
    return True