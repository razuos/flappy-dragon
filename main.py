from lib.graphics import *

win = GraphWin("Flappy Bird", 400, 800)
pt = Point(200, 400)
pt2 = Point(200, 300)
pt3 = Point(200, 200)
pt4 = Point(200, 600)


win.setBackground(color_rgb(110, 175, 250))

bottom = Image(pt, "./assets/barrier/bottom.png")
middle = Image(pt2, "./assets/barrier/middle.png")
top = Image(pt3, "./assets/barrier/top.png")
character = Image(pt4, "./assets/character/character.png")

top.draw(win)
middle.draw(win)
bottom.draw(win)
character.draw(win)
win.getMouse()
win.close()
