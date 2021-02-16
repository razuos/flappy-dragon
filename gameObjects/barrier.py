from lib.graphics import *
from collision import normalizeCollisionBox

class Barrier:
  # ySize is 
  def __init__(self, window: GraphWin, x: int, ySize: int, isUpsideDown: bool):
    self.window = window

    self.bottom = Image(Point(x, window.getHeight()), "./assets/barrier/bottom.png")
    # Move para cima para ficar direito na tela
    self.bottom.move(0, (self.bottom.getHeight() // 2) * -1)
    self.bottom.draw(window)

    self.middle = Image(Point(x, self.bottom.anchor.getY() - self.bottom.getHeight()), "./assets/barrier/middle.png")
    self.middle.draw(window)

    self.top = Image(Point(x, self.middle.anchor.getY() - self.middle.getHeight()), "./assets/barrier/top.png")
    self.top.draw(window)

    self._makeCollisionBox()
    # for _ in range(ySize):
      # Criar meios da barreira de forma dinamica

  def _makeCollisionBox(self):
    # Uses the top because it's the widest
    P1X = self.top.getAnchor().getX() - (self.top.getWidth() / 2)
    P1Y = self.bottom.getAnchor().getY() + (self.bottom.getHeight() / 2)
    P1 = Point(P1X, P1Y)

    P2X = self.top.getAnchor().getX() + (self.top.getWidth() / 2)
    P2Y = self.top.getAnchor().getY() - (self.top.getHeight() / 2)
    P2 = Point(P2X, P2Y)

    collisionBox = normalizeCollisionBox(Rectangle(P1, P2))
    collisionBox.setFill("black")
    collisionBox.draw(self.window)

    self.collisionBox = collisionBox

  def move(self, dx, dy):
    self.bottom.move(dx, dy)
    self.middle.move(dx, dy)
    self.top.move(dx, dy)
    self.collisionBox.move(dx, dy)
    
  def __del__(self):
    self.bottom.undraw()
    self.middle.undraw()
    self.top.undraw()
    self.collisionBox.undraw()