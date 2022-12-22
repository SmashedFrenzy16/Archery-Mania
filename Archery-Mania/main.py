import math
import random
import pygame
from pygame import mixer
import sys

pygame.init()

WIDTH = 800
HEIGHT = 600
BLACK = (255, 255, 255)

screen = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("Archery by @SmashedFrenzy16")

# <a href="https://www.flaticon.com/free-icons/target" title="target icons">Target icons created by Vectors Market - Flaticon</a>

gicon = pygame.image.load("target.png")
pygame.display.set_icon(gicon)

background = pygame.image.load("hilly_back.png")

# <a href="https://www.flaticon.com/free-icons/bow" title="bow icons">Bow icons created by Freepik - Flaticon</a>

player_img = pygame.image.load("bow.png")
player_x = 1
player_y = 580
player_y_change = 0

# All Target icons credited to Flaticon

# t5p is the target that gets you 5 points

t5p_img = []
t5p_x = []
t5p_y = []
t5p_x_change = []
t5p_num = 10

for i in range(t5p_num):

    t5p_img.append(pygame.image.load("t5p.png"))
    t5p_x.append(random.randint(801, 900))
    t5p_y.append(random.randint(0, 598))
    t5p_x_change.append(0.6)

# tgover is the target that results in game over

tgover_img = []
tgover_x = []
tgover_y = []
tgover_x_change = []
tgover_num = 5

for i in range(tgover_num):

    tgover_img.append(pygame.image.load("tgover.png"))
    tgover_x.append(random.randint(801, 900))
    tgover_y.append(random.randint(0, 598))
    tgover_x_change.append(0.6)

# Arrow image from Flaticon

arrow_img = pygame.image.load("arrow.png")
arrow_x = 0
arrow_y = 480
arrow_x_change = 1.5
arrow_y_change = 0
arrow_state = "Ready"


def player(x, y):

    screen.blit(player_img, (x, y))

def t5p(x, y, i):

    screen.blit(t5p_img[i], (x, y))

def tgover(x, y, i):

    screen.blit(tgover_img[i], (x, y))

def fire_arrow(x, y):

    global arrow_state

    arrow_state = "Fire"

    screen.blit(arrow_img, (x + 16, y + 10))

def is_colliding_t5p(t5p_x, t5p_y, arrow_x, arrow_y):
    distance = math.sqrt(math.pow(t5p_x - arrow_x, 2) +
                         (math.pow(t5p_y - arrow_y, 2)))
    if distance < 27:
        return True
    else:
        return False

def is_colliding_tgover(tgover_x, tgover_y, arrow_x, arrow_y):
    distance = math.sqrt(math.pow(tgover_x - arrow_x, 2) +
                         (math.pow(tgover_y - arrow_y, 2)))
    if distance < 27:
        return True
    else:
        return False

score_val = 0

sfont = pygame.font.Font("freesansbold.ttf", 50)

text_x = 10
text_y = 0

goverfont = pygame.font.Font("freesansbold.ttf", 70)

def show_score(x, y):

    score  = sfont.render("Score: " + str(score_val), True, (0, 225, 0))
    screen.blit(score, (x, y))

def game_over_txt():

    govertxt = goverfont.render("GAME OVER!", True, (0, 225, 0))
    screen.blit(govertxt, (200, 250))

running = True

while running:

    screen.fill(BLACK)

    screen.blit(background, (0, 0))

    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            running = False
        
        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_DOWN:

                player_y_change = 0.6
            
            if event.key == pygame.K_UP:

                player_y_change = -0.6
        
        if event.type == pygame.KEYUP:

            if event.key == pygame.K_DOWN or event.key == pygame.K_UP:

                player_y_change = 0

            if event.key == pygame.K_SPACE:

                if arrow_state is "Ready":

                    arrow_y = player_y

                    fire_arrow(arrow_x, arrow_y)
    
    player_y += player_y_change

    if player_y <= 0:

        player_y = 0

    elif player_y >= 598:

        player_y = 598

    for i in range(t5p_num):

        t5p_x[i] += t5p_x_change[i]

        if t5p_x[i] <= 0:

            t5p_x_change[i] = 0.6

        elif t5p_x[i] >= 736:

            t5p_x_change[i] = -0.6

        collide_t5p = is_colliding_t5p(t5p_x[i], t5p_y[i], arrow_x, arrow_y)

        if collide_t5p:

            arrow_x = 1

            arrow_state = "Ready"

            t5p_x[i] = random.randint(801, 900)
            t5p_y[i] = random.randint(0, 598)

            score_val += 5

        t5p(t5p_x[i], t5p_y[i], i)

    
    for i in range(tgover_num):

        tgover_x[i] += tgover_x_change[i]

        if tgover_x[i] <= 0:

            tgover_x_change[i] = 0.6

        elif tgover_x[i] >= 736:

            tgover_x_change[i] = -0.6

        collide_tgover = is_colliding_tgover(tgover_x[i], tgover_y[i], arrow_x, arrow_y)

        if collide_tgover:

            arrow_x = 1

            arrow_state = "Ready"

            tgover_x[i] = random.randint(801, 900)
            tgover_y[i] = random.randint(0, 598)

            game_over_txt()

            sys.exit()

        tgover(tgover_x[i], tgover_y[i], i)

    
    if arrow_x >= 800:

        arrow_x = 1

        arrow_state = "Ready"

    if arrow_state is "Fire":

        fire_arrow(arrow_x, arrow_y)

        arrow_x += arrow_x_change

    player(player_x, player_y)

    show_score(text_x, text_y)

    pygame.display.update()



        

