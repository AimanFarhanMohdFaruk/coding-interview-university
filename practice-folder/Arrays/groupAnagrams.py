from typing import List
from collections import defaultdict

def groupAnagrams(strs: List[str]) -> List[List[str]]:
  ans = defaultdict(list) # mapping charCount to list of Anagrams

  for s in strs:
    count = [0] * 26 # a....z each lowercase char
    for c in s:
      # map character (a) to 0, and the rest to the following.
        count[ord(c) - ord("a")] += 1
    ans[tuple(count)].append(s)
  return ans.values()

print(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))

# O(m * n)