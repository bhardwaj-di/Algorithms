from collections import defaultdict
def groupAnagrams(strs):
    res = defaultdict(list)
    for a in strs:
        count = [0]*26
        for c in a:
            count[ord(c) - ord('a')] += 1
        res[tuple(count)].append(a)
    return res.values()