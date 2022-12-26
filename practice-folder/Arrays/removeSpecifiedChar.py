def RemoveSpecifiedChar(str, remove):
  flagged_for_remove = []
  final = []

  for char in remove:
    flagged_for_remove.append(char)
    
    for i in range(len(str)):
      c = str[i]
      if ( c not in flagged_for_remove):
        final.append(c)
  
    return ''.join(final)
  return None


print(RemoveSpecifiedChar('battle', 'ae'))