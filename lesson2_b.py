import pgzrun
from random import randint

TITLE= " Multiple Flappy Ball"
WIDTH= 800
HEIGHT = 600



class Ball:
    def __init__(self):
      self.x = randint (50, WIDTH - 50)
      self.y = randint (50, HEIGHT - 50)
      self.vx = randint(-300,300)
      self.vy = randint(-300,300)
      self.radius= 25
      self.color= (
         randint(0,255),
         randint(0,255),
         randint(0,255)
      )

    def draw(self):
     pos = (self.x,self.y)
     screen.draw.filled_circle(pos,self.radius, self.color)




    def move(self,dt):
       self.x+= self.vx* dt
       self.y += self.vy *dt
       if self.x <self.radius:
        self.x = self.radius
        self.vx= -self.vx

       if self.x >WIDTH - self.radius:
         self.x = WIDTH- self.radius
         self.vx = -self.vx

       if self.y <self.radius:
        self.y = self.radius
        self.vy= -self.vy

       if self.y >HEIGHT - self.radius:
         self.y = HEIGHT - self.radius
         self.vy= -self.vy

balls = []

for i in range(5):
    ball = Ball()
    balls.append(ball)

def draw():
   screen.clear()
   for ball in balls:
      ball.draw()

def update(dt):
      for ball in balls:
        ball.move(dt)

pgzrun.go()
