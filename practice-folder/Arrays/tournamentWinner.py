HOME_TEAM_WON = 1

def tournamentWinnerOne(competitions, results):
  currentBest = ""
  scores = {currentBest: 0}

  for i, competition in enumerate(competitions):
    result = results[i]
    home, away = competition

    winnningTeam = home if result == HOME_TEAM_WON else away

    updateHelper(home, 3, scores)

    if scores(winnningTeam) > scores[currentBest]:
      currentBest = winnningTeam
  return currentBest


def updateHelper(team, points, scores):
  if team not in scores:
    scores[team] = 0

  scores[team] += points

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