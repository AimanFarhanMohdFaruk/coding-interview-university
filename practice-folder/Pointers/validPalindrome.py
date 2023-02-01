# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters

def validPalindrome(string):
  newString = ""

  for c in string:
    if c.isalnum():
      newString += c.lower()
  return newString == newString[::-1]

print(validPalindrome("A man, a plan, a canal: Panama"))

def isPalindrome(string: str) -> bool:
  l, r = 0, len(string) - 1
  while l < r:
    while l < r and not alphanum(string[l]):
      # ignore non-alphanum characters
      l += 1
    while l < r and not alphanum(string[r]):
      r -= 1
    if string[l].lower() != string[r].lower():
      return False
    l += 1
    r -= 1
  return True

# function to check whether it is a alphanumeric number
def alphanum(c):
    return (
        ord("A") <= ord(c) <= ord("Z")
        or ord("a") <= ord(c) <= ord("z")
        or ord("0") <= ord(c) <= ord("9")
    )

print(isPalindrome("A man, a plan, a canal: Panamw"))