class player:
  def __init__(self,playful=True):
    self.playful = playful

  def wantsToPlay(self):
    if self.playful == True:
      print("The player wants to play")
    else:
      print("The player doesn't want to play")

newPlayer = player(False)
newPlayer.wantsToPlay()