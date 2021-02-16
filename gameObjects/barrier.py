from lib.graphics import *

class Barrier:
  # ySize is 
  def __init__(self, window: GraphWin, x: int, ySize: int, isUpsideDown: bool):
    self.bottom = Image(Point(x, window.getHeight()), "./assets/barrier/bottom.png")
    # Move para cima para ficar direito na tela
    self.bottom.move(0, (self.bottom.getHeight() // 2) * -1)
    self.bottom.draw(window)

    self.middle = Image(Point(x, self.bottom.anchor.getY() - self.bottom.getHeight()), "./assets/barrier/middle.png")
    self.middle.draw(window)

    self.top = Image(Point(x, self.middle.anchor.getY() - self.middle.getHeight()), "./assets/barrier/top.png")
    self.top.draw(window)

    # for _ in range(ySize):
      # Criar meios da barreira de forma dinamica

  def move(self, dx, dy):
    self.bottom.move(dx, dy)
    self.middle.move(dx, dy)
    self.top.move(dx, dy)

  def destroy(self):
    self.bottom.undraw()
    self.middle.undraw()
    self.top.undraw()