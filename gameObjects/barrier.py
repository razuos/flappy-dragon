from lib.graphics import *
from collision import normalizeCollisionBox

class Barrier:
  def __init__(self, window: GraphWin, x: int, ySize: int, isUpsideDown: bool):
    self.window = window
    self.objects = []
    self.x = x
    self.ySize = ySize
    self.isUpsideDown = isUpsideDown
    self._makeBottom()
    self._makeMiddle()
    self._makeTop()
    self._makeCollisionBox()

  def _makeBottom(self):
    if (self.isUpsideDown):
      bottom = Image(Point(self.x, 0), "./assets/barrier/bottom-inverted.png")
      bottom.move(0, (bottom.getHeight() // 2))
    else:
      bottom = Image(Point(self.x, self.window.getHeight()), "./assets/barrier/bottom.png")
      bottom.move(0, (bottom.getHeight() // 2) * -1)

    bottom.draw(self.window)
    self.objects.append(bottom)

  def _makeMiddle(self):
    for _ in range(self.ySize):
      reference = self.objects[-1]
      if (self.isUpsideDown):
        middle = Image(Point(self.x, reference.anchor.getY() + reference.getHeight()), "./assets/barrier/middle-inverted.png")
      else:
        middle = Image(Point(self.x, reference.anchor.getY() - reference.getHeight()), "./assets/barrier/middle.png")
      
      middle.draw(self.window)
      self.objects.append(middle)
  
  def _makeTop(self):
    reference = self.objects[-1]
    if (self.isUpsideDown):
      top = Image(Point(self.x, reference.anchor.getY() + reference.getHeight()), "./assets/barrier/top-inverted.png")
    else:
      top = Image(Point(self.x, reference.anchor.getY() - reference.getHeight()), "./assets/barrier/top-inverted.png")

    top.draw(self.window)
    self.objects.append(top)

  def _makeCollisionBox(self):
    top = self.objects[-1]
    bottom = self.objects[0]

    P1X = top.getAnchor().getX() - (top.getWidth() / 2)
    P2X = top.getAnchor().getX() + (top.getWidth() / 2)

    if (self.isUpsideDown):
      P1Y = bottom.getAnchor().getY() - (bottom.getHeight() / 2)
      P2Y = top.getAnchor().getY() + (top.getHeight() / 2)
    else:
      P1Y = bottom.getAnchor().getY() + (bottom.getHeight() / 2)
      P2Y = top.getAnchor().getY() - (top.getHeight() / 2)

    P1 = Point(P1X, P1Y)
    P2 = Point(P2X, P2Y)

    collisionBox = normalizeCollisionBox(Rectangle(P1, P2))
    # collisionBox.setFill("black")
    # collisionBox.draw(self.window)

    self.collisionBox = collisionBox

  def move(self, dx, dy):
    for obj in self.objects:
      obj.move(dx, dy)
    self.collisionBox.move(dx, dy)
    
  def __del__(self):
    for obj in self.objects:
      obj.undraw()
    self.collisionBox.undraw()