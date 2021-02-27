from lib.graphics import Rectangle, Point

# "Normalizar" signica deixar o ponto1 no canto inferior esquerdo e o ponto2 no canto superior direito
# Isso falicita o cálculo de colisão
def normalizeCollisionBox(collisionBox: Rectangle):
  oldP1 = collisionBox.getP1()
  oldP2 = collisionBox.getP2()

  maxX = max(oldP1.x, oldP2.x)
  maxY = max(oldP1.y, oldP2.y)
  
  minX = min(oldP1.x, oldP2.x)
  minY = min(oldP1.y, oldP2.y)

  P1 = Point(minX, minY)
  P2 = Point(maxX, maxY)

  return Rectangle(P1, P2)

def isColliding(box1: Rectangle, box2: Rectangle):
  if (box1.p1.x <= box2.p2.x):
    if (box1.p2.x >= box2.p1.x):
      if (box1.p1.y <= box2.p2.y):
        if (box1.p2.y >= box2.p1.y):
          return True

  return False
