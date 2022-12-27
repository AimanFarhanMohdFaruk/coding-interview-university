def ReverseWord(str):
  words = str.split(' ')
  string = []
  for word in words:
    string.insert(0, word) ## insert each word in the beginning.
  return (" ".join(string))

print(ReverseWord("Jordi Alba"))
