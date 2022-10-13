import pygame
from sys import exit
from math import sin,cos,pi
from collections import deque
from decimal import Decimal,localcontext

pygame.init()
clock = pygame.time.Clock()
height , width = 800,800
screen = pygame.display.set_mode((width,height))
trace = pygame.USEREVENT + 1
pygame.time.set_timer(trace,10)
x = 10

g = 1

m1,m2 = 10,10

r1 , r2 = 160+m1,160+2*m2

fix_x , fix_y = width/2,250

angle1 , angle2 = pi/2 ,pi/4

angular_v1 , angular_v2 = 0 , 0


positions = deque()

while True:
    denom1 = r1*(2*m1+m2-m2*cos(2*angle1-2*angle2))

    _1 = -g * (2 * m1 + m2) * sin(angle1)
    _2 = -m2 * g * sin(angle1-2*angle2)
    _3 = -2*sin(angle1 - angle2)*m2
    _4 = (angular_v2**2)*r2+(angular_v1**2)*r1*cos(angle1-angle2)

    angular_acc1 = (_1+_2+_3*_4)/denom1

    _1_ = 2*sin(angle1-angle2)
    _2_ = (angular_v1**2)*r1*(m1+m2)
    _3_ = g*(m1+m2)*cos(angle1)
    _4_ = (angular_v2**2)*r2*m2*cos(angle1-angle2)
    denom2 = r2*(2*m1+m2-m2*cos(2*angle1-2*angle2))

    angular_acc2 =  _1_*(_2_ + _3_ + _4_)/denom2

    x1, y1 = r1 * sin(angle1) + fix_x, r1 * cos(angle1) + fix_y
    x2, y2 = (r2 * sin(angle2) + x1), (r2 * cos(angle2) + y1)

    screen.fill("black")
    pygame.draw.line(screen,"white",(fix_x,fix_y),(x1,y1))
    pygame.draw.circle(screen, "white", (x1,y1), m1)
    pygame.draw.line(screen,"white",(x1,y1),(x2,y2))
    cir = pygame.draw.circle(screen, "white", (x2,y2), m2)
    positions.append((cir.x,cir.y))


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    for i in positions:
        pygame.draw.circle(screen,"white",(i[0]+m2,i[1]+m2),1)
    # print(cir.x)

    # pygame.draw.circle(screen,"white",pygame.mouse.get_pos(),1)
    # x+=2
    # clock.tick(200)
    if len(positions)>100:
        positions.popleft()

    angular_v1 += angular_acc1
    angular_v2 += angular_acc2

    angle1 += angular_v1
    angle2 += angular_v2

    angular_v1*=0.9999
    angular_v2*=0.9999
    clock.tick(60)
    pygame.display.flip()
