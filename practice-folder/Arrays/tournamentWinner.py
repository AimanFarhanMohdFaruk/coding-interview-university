def tournamentWinner(competitions, results):
  scores = {}
  for idx in range(len(competitions)):
    [homeTeam, awayTeam] = competitions[idx]
    if homeTeam not in scores:
      scores[homeTeam] = 0

    if awayTeam not in scores:
      scores[awayTeam] = 0
    
    if results[idx] == 1:
      scores[homeTeam] += 3
    else:
      scores[awayTeam] += 3
  
  return max(scores, key=scores.get)

print(tournamentWinner([
  ["HTML", "C#"],
  ["C#", "Python"],
  ["Python", "HTML"]
],[0,0,1]))