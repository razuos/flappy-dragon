from lib.graphics import *

class Score:
  def __init__(self, win: GraphWin):
    self.win = win
    self.score = 0
    self.text = Text(Point(self.win.getWidth() / 2, self.win.getHeight() / 10), self.score)

    self.text.setFace("helvetica")
    self.text.setStyle("bold italic")
    self.text.setSize(24)
    self.text.setTextColor(color_rgb(255, 255, 0))

    self.text.draw(win)

  def addPoints(self, points):
    self.score += points
    self.text.setText("{:.0f}".format(self.score))
    # Pra ficar no topo
    self.win.tag_raise(self.text.id)

  def __del__(self):
    self.text.undraw()
