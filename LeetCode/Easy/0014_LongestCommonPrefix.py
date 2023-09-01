#runtime: 15ms-->beats 90.42%
#memory:13.39mb-->breats 87.99%
def longestCommonPrefix(strs):
    if len(strs)==0: return ""
    prefix=""
    loopSize=min(len(str) for str in strs)
    for i in range(loopSize):
        letter=strs[0][i]
        for word in strs:
            if word[i]!=letter:
                return prefix
        prefix+=letter
    return prefix
