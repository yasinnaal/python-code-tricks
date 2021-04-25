class Match:

  def __init__(self,points=0):
    self.points = points

  def ScorePoints(self):
    self.points += 1

newMatch = Match(1)
newMatch.ScorePoints()
newMatch.ScorePoints()
print(newMatch.points)