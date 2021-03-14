from lib.graphics import *

class Lost:
  def __init__(self, win: GraphWin, score: float):
    x = win.getWidth() / 2
    self.youLostText = Text(Point(x, (win.getHeight() / 2) - 30), "Você perdeu, sua pontução foi:")
    self.scoreText = Text(Point(x, (win.getHeight() / 2) + 30), "{:.0f}".format(score))
    self.pressAnyText = Text(Point(x, (win.getHeight() / 2) + 280), "Pressione qualquer tecla para reiniciar")

    for text in self.scoreText, self.youLostText, self.pressAnyText:
      text.setFace("helvetica")
      text.setStyle("bold italic")
      text.setTextColor(color_rgb(255, 255, 0))
      text.draw(win)
      
    self.youLostText.setSize(18)
    self.scoreText.setSize(36)
    self.pressAnyText.setSize(12)

  def __del__(self):
    self.youLostText.undraw()
    self.scoreText.undraw()
    self.pressAnyText.undraw()
