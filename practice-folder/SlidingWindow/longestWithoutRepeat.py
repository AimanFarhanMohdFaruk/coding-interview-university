def longestSubstring(s):
    charSet = set()
    l = 0
    res = 0

    for r in range(len(s)):
        while s[r] in charSet:
          charSet.remove(s[l])
          l += 1
        charSet.add(s[r])
        res = max(res, r - l + 1)
        print(charSet)
    return res
            
print(longestSubstring('abcabcbbabcd'))

# the sliding window, your subarray, just ensure that is does not have any duplicates.