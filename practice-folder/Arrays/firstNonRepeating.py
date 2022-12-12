
def FirstNonRepeating(str):
    char_order = [] ## List of characters. Reduce going through duplicates
    count = {}

    for char in str:
      if char in count:
        count[char] += 1
      else:
        count[char] = 1
        char_order.append(char)
    for char in char_order:
        if count[char] == 1:
          return char
    return None

print("First Non-Repeating Character = ",FirstNonRepeating('thisisit'))