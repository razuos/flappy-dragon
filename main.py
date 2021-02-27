from lib.graphics import *
from gameObjects.character import Character
from gameObjects.barrier import Barrier
from collision import isColliding

win = GraphWin("Flappy Bird", 400, 600, autoflush=False)
win.setBackground(color_rgb(110, 175, 250))
 
myPlayer = Character(win, win.getWidth() / 2, win.getHeight() / 2)
myBarrier = Barrier(win, win.getWidth() / 2, 1, True)

collided = False

while collided == False:
    k = win.checkKey()

    dy = 0
    dx = 0

    if k == "space":
      dy -= 30
    else:
      dy += .5

    time.sleep(.005)
    myPlayer.move(dx, dy)

    
    if (isColliding(myPlayer.collisionBox, myBarrier.collisionBox)):
      print("COLIDINDO")
    else:
      print("Não está colidindo")



win.close()

win.close()
