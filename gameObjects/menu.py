from lib.graphics import *
from gameObjects.character import Character
from gameObjects.barrier import Barrier

class Menu:
  def __init__(self, win: GraphWin):
    x = win.getWidth() / 2
    self.titleText = Text(Point(x, win.getHeight() / 10), "Flappy Dragon")
    self.pressAnyText = Text(Point(x, (win.getHeight() / 2) + 280), "Pressione qualquer tecla para iniciar")

    for text in self.titleText, self.pressAnyText:
      text.setFace("helvetica")
      text.setStyle("bold italic")
      text.setTextColor(color_rgb(255, 255, 0))
      
    self.titleText.setSize(18)
    self.pressAnyText.setSize(12)

    self.player = Character(win, x - 80, win.getHeight() / 3)
    self.barrier1 = Barrier(win, x - 30, 2, False)
    self.barrier2 = Barrier(win, x + 180, 6, False)
    self.titleText.draw(win)
    self.pressAnyText.draw(win)

  def __del__(self):
    self.titleText.undraw()
    self.pressAnyText.undraw()
    del self.player