from lib.graphics import *
from gameObjects.barrier import Barrier
from gameObjects.character import Character
from collision import isColliding

win = GraphWin("Flappy Bird", 400, 600)
win.setBackground(color_rgb(110, 175, 250))

myBarrier = Barrier(win, 300, 1, False)
myCharacter = Character(win, 100, 500)

win.getMouse()
myBarrier.move(-30, 0)
# Na verdade é preciso checar se colide com o resto da barreira também
print("is colliding: ", isColliding(myCharacter.character, myBarrier.top))

win.getMouse()
myBarrier.move(-30, 0)
print("is colliding: ", isColliding(myCharacter.character, myBarrier.top))

win.getMouse()
myBarrier.destroy()

win.getMouse()
win.close()
