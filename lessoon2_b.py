import pygame
import random

pygame.init()


WIDTH= 1000
HEIGHT = 650


screen= pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Neon Wireframe City")

clock = pygame.time.clock()

BULIDING = (18,18,30)
CYAN= (0,225,255)
PINK = (255,0,200)
BLUE = (0,170,225)
WHITE = (255,255,255)

stars = []

for _ in range(180):
    stars.append([
        random.randint(0,WIDTH),
        random.randint(0,HEIGHT // 2),
        random.randint(1,3),
        random.uniform(0.2,0.8)

    ])

background = []
foreground = []

x= 0 

while x < WIDTH:
    w = random.randint(60,110)
    h = random.randint(140,250)
    backround.append((x,w,h))
    x+= w + random.randint(5,20)


x=0 

while x < WIDTH:
    w = random.randint(70,120)
    h = random.randint(230,430)
    foreground.append((x,w,h))
    x+= w + random.randint(5,15)

window_state= []
for bx,bw,bh in foreground:
    top= HEIGHT - bh
    building= []
    wx=bx+8
    while wx < bx +b - 10:
        wy = top +10
        while wy< HEIGHT - 20:
            building.append([wx,wy,random.choice([True,False])])
            wx+= 20
        wx +=16
    window_state.append(building)

window_timer = 0
running = True 

while running:
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                 running = False

    for y in range(HEIGHT):
         pygame.draw.line(screen,(
                         (5+y // 20,0,25+y// 9),(0,y),(
    
                         )


    for s in starts:
    pygame.draw.circle(screen,WHITE , (int([0]), int(s[1])), s[2])
    s[0] += s[3]
    if s[0] > WIDTH:
         s[0] = 0
         s[1] = random.randint(0,HEIGHT // 2)

    pygame.draw.cricle(screen,(100,20,100), (800,110), 70)
    pygame.draw.cricle(screen,(170,40,170), (800,110), 60)
    pygame.draw.cricle(screen,(255,120,270), (800,110), 50)