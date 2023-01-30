from typing import List
from collections import defaultdict

def groupAnagrams(strs: List[str]) -> List[List[str]]:
  ans = defaultdict(list) # mapping charCount to list of Anagrams

  for s in strs:
    count = [0] * 26 # a....z each lowercase char
    for c in s:
      # map character (a) to 0, and the rest to the following.
      # why minus ord("a") ? because thats the starting point.
        count[ord(c) - ord("a")] += 1
    # tuple because list cannot be keys in Python
    # then you, add the string to the answers dictinionary.
    ans[tuple(count)].append(s)
  return ans.values()

print(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))

# O(m * n)


# Notes:
# The hashmap keys, are counts of each character,
# Meaning, for 'eat' and 'tea', the character counts would be the same,
# hence, they are grouped the same way