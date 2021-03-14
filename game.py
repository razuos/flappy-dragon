from lib.graphics import GraphWin, color_rgb
from gameObjects.character import Character
from gameObjects.barrier import Barrier
from gameObjects.score import Score
from gameObjects.lost import Lost
from gameObjects.menu import Menu
from collision import isColliding
from random import randint
from time import sleep

title = "Flappy Dragon"
backgroundColor = color_rgb(110, 175, 250)

class Game:
  def __init__(self, winWidth, winHeight):
    self.win = GraphWin(title, winWidth, winHeight, autoflush=False)
    self.win.setBackground(backgroundColor)
    self.alive = False
    self.timeInterval = .005
    self.barrierSizeBudget = 4
    self.player = None
    self.score = None
    self.bottomBarrier = None
    self.topBarrier = None
    self.menu = None

  def switchState(self, state):
    if state == "MENU":
      self.menu = Menu(self.win)
      self.win.getKey()
      self.switchState("MAIN")

    if state == "MAIN":
      if self.menu:
        self.menu = None
      self.alive = True
      self.player = Character(self.win, self.win.getWidth() / 2, self.win.getHeight() / 2)
      self.bottomBarrier = Barrier(self.win, self.win.getWidth() + 100, 1, False)
      self.topBarrier = Barrier(self.win, self.win.getWidth() + 100, 1, True)
      self.score = Score(self.win)
      self.barrierWidth = self.bottomBarrier.objects[0].getWidth()

      while self.alive:
        self.mainLoop()
      
      self.switchState("LOST")

    if state == "LOST":
      finalScore = self.score.score

      if self.bottomBarrier:
        del self.bottomBarrier 
      if self.topBarrier:
        del self.topBarrier
      if self.player:
        del self.player
      if self.score:
        del self.score
      
      lost = Lost(self.win, finalScore)
      self.win.getKey()
      del lost
      self.switchState("MAIN")

  def getBarrierSizes(self):
    x = randint(1, self.barrierSizeBudget - 1)
    if (self.barrierSizeBudget - x) == 1:
      y = 1
    else:
      y = randint(1, self.barrierSizeBudget - x)
    return x, y

  def mainLoop(self):
    while self.alive:
      k = self.win.checkKey()

      dy = 0
      dx = 0

      if k == "space":
        dy -= 60
      else:
        dy += 1

      sleep(self.timeInterval)
      self.score.addPoints(self.timeInterval)
      self.player.move(dx, dy)

      for barrier in self.bottomBarrier, self.topBarrier:
        barrier.move(-1, 0)
        if isColliding(barrier.collisionBox, self.player.collisionBox):
          self.alive = False
        if barrier.collisionBox.getP2().getX() < 0:
          del self.bottomBarrier
          del self.topBarrier

          x = self.win.getWidth() + self.barrierWidth
          bottomSize, topSize = self.getBarrierSizes()

          self.bottomBarrier = Barrier(self.win, x, bottomSize, False)
          self.topBarrier = Barrier(self.win, x, topSize, True)
