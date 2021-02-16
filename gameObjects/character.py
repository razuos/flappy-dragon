from lib.graphics import *

class Character:
  def __init__(self, window: GraphWin, x: int, y: int):
    self.character = Image(Point(x, y), "./assets/character/character.png")
    self.character.draw(window)

  def move(self, dx, dy):
    self.character.move(dx, dy)

  def destroy(self):
    self.character.undraw()
