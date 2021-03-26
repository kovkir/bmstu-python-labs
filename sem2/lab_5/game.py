import pygame as pg
from random import randint

window_width = 1275
window_height = 690

pg.init()
win = pg.display.set_mode((window_width, window_height))

pg.display.set_caption("Kovalets Kirill IU7-23B")

mario = pg.image.load('mario.png')
mario2 = pg.image.load('mario2.png')
background = pg.image.load('background.jpg')
game_over = pg.image.load('game_over.jpg')
rock = pg.image.load('rock.png')
coin = pg.image.load('coin.png')

width = 90
height = 135
x = 5
y = window_height - height - 5
speed = 5
FPS = 120

right = True
isJump = False

jump_count = 10

clock = pg.time.Clock()

run = True
rocks = []
coins = []

class rockfall():
    def __init__(self, x, y):

        self.x = x
        self.y = y
        self.vel = 8

    def draw_rock(self, win):
        win.blit(rock, (self.x, self.y))

class mario_coins():
    def __init__(self, x, y):

        self.x = x
        self.y = y

    def draw_coin(self, win):
        win.blit(coin, (self.x, self.y))
        
def draw():
    win.blit(background, (0, 0))
    
    if right:
        win.blit(mario, (x, y))
    else:
        win.blit(mario2, (x, y))

    for i in rocks:
        i.draw_rock(win)
        
    for i in coins:
        i.draw_coin(win)
        
    pg.display.update()

rocks.append(rockfall(randint(5, window_width - 85), 5))
coins.append(mario_coins(randint(width + 10, window_width - 85),
        window_height - 2 * height + randint(1, 2 * height - 55)))

while run:
    clock.tick(FPS)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False

    for i in rocks:
        if (i.y < window_height) and (i.y > 0):
            
            if ((y + 15 < i.y + 60 < y + height) and (10 < x + width - i.x < width)) or\
               ((y + 30 < i.y + 60 < y + height) and (10 < i.x + 60 - x < width)):

                pg.time.wait(3000)
                win.blit(game_over, (0, 0))
                pg.display.update()
                pg.time.wait(3000)
                run = False

            else:
                i.y += i.vel
        else:
            rocks.pop(rocks.index(i))
            
    for i in coins:
        if (y < i.y + 50 < y + height) and\
           ((10 < x + width - i.x < width) or (10 < i.x + 50 - x < width)):
            coins.pop(coins.index(i))
            
    keys = pg.key.get_pressed()

    if len(coins) < 3:
        coins.append(mario_coins(randint(width + 10, window_width - 85),
        window_height - 2 * height + randint(1, 2 * height - 55)))
        
    if len(rocks) < 5:
        if rocks[-1].y > 120:
            rocks.append(rockfall(randint(5, window_width - 85), 5))
            
    if keys[pg.K_LEFT] and (x > speed):
        x -= speed
        right = False
        
    if keys[pg.K_RIGHT] and (x < window_width - width - speed):
        x += speed
        right = True

    if not(isJump):
        if keys[pg.K_SPACE]:
            isJump = True
    else:
        if jump_count >= -10:

            if jump_count < 0:
                y += int((jump_count ** 2) / 5 * 2)
            else:
                y -= int((jump_count ** 2) / 5 * 2) 

            jump_count -= 1
        else:
            isJump = False
            jump_count = 10

    draw()
    
pg.quit()
