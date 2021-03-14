from lib.graphics import GraphicsError
from game import Game

myGame = Game(400, 700)

try:
  myGame.switchState('MENU')
except GraphicsError as e:
  if str(e) == "getKey in closed window":
    quit(0)
  else:
    print(e)
