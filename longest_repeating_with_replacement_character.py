def characterReplacement(s, k) :
    l = 0
    res = 0
    alphaCount = {}
    for r in range(len(s)):
        alphaCount[s[r]] = 1 + alphaCount.get(s[r],0)
        if ((r - l + 1) - max(alphaCount.values())) > k:
            alphaCount[s[l]] -= 1
            l += 1
        res = max(res, r - l + 1)
    return res