from lib.graphics import *
from collision import normalizeCollisionBox
class Character:
  def __init__(self, window: GraphWin, x: int, y: int):
    self.window = window
    self.character = Image(Point(x, y), "./assets/character/character.png")
    self.character.draw(window)
    self._makeCollisionBox()

  def _makeCollisionBox(self):
    P1X = self.character.getAnchor().getX() - self.character.getWidth() / 2
    P1Y = self.character.getAnchor().getY() + self.character.getHeight() / 2
    P1 = Point(P1X, P1Y)

    P2X = self.character.getAnchor().getX() + self.character.getWidth() / 2
    P2Y = self.character.getAnchor().getY() - self.character.getHeight() / 2
    P2 = Point(P2X, P2Y)

    collisionBox = normalizeCollisionBox(Rectangle(P1, P2))
    # collisionBox.setFill("green")
    # collisionBox.draw(self.window)

    self.collisionBox = collisionBox

  def move(self, dx, dy):
    self.character.move(dx, dy)
    self.collisionBox.move(dx, dy)

  def __del__(self):
    self.character.undraw()
    self.collisionBox.undraw()
