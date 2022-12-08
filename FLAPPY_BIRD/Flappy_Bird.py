import pygame as pg
from random import randint

def draw_floor():
    screen.blit(floor,(floor_x,530))
    screen.blit(floor,(floor_x + WIDTH,530))
def rotate_bird(bird1):
    new_bird = pg.transform.rotozoom(bird1, -bird_drop_velocity*3, 1)
    return new_bird
def score_display(game_stay):
    if game_stay == 'main game':
        score_surface = font.render('Score: ' + str(score) ,True,WHITE)
        score_rect = score_surface.get_rect(center = (WIDTH/2,50))
        screen.blit(score_surface, score_rect)
    if game_stay == 'game over':
        score_surface = font.render('Score: ' + str(score) ,True,WHITE)
        score_rect = score_surface.get_rect(center = (WIDTH/2,50))
        screen.blit(score_surface, score_rect)

        high_score_surface = font.render('High Score: ' + str(high_score) ,True,WHITE)
        high_score_rect = high_score_surface.get_rect(center = (WIDTH/2,200))
        screen.blit(high_score_surface, high_score_rect)
pg.mixer.pre_init()
pg.init()

WIDTH = 400
HEIGHT = 600
running = False
screen = pg.display.set_mode((WIDTH,HEIGHT))
pg.display.set_caption("Flappy Bird")

GREEN = (0,200,0)
BLUE = (0,0,255)
XANH_TIM = (155,161,243)
RED = (255,0,0)
BLACK = (0,0,0)
WHITE = (255,255,255)

clock = pg.time.Clock()

TUBE_WIDTH = 50
tube1_x = 400
tube2_x = 600
tube3_x = 800

tube1_height = randint(100,300)
tube2_height = randint(100,300)
tube3_height = randint(100,300)

#BIRD
BIRD_X = 50
bird_y = 250
BIRD_WIDTH = 30
BIRD_HEIGHT = 30

TUBE_VELOCITY = 3 # van toc ong
TUBE_GAP = 150 # Khoang cach 2 ong doi dien
bird_drop_velocity = 0
GRAVITY = 0.4
score = 0
high_score = 0
with open('assets/high_score.txt') as f:
    high_score = f.read()
    high_score = int(high_score)

font = pg.font.Font('assets/04B_19.ttf', 30)
font1 = pg.font.Font('assets/04B_19.ttf', 20)

tube1_pass = False
tube2_pass = False
tube3_pass = False
pausing = False

background_image = pg.image.load('assets/background-night.png').convert()
background_image = pg.transform.scale(background_image,(400,600))
# Bird
bird_image = pg.image.load('assets/bird.png').convert_alpha()
bird_image = pg.transform.scale(bird_image,(30,25))

# Create Timer for bird
birdflap = pg.USEREVENT 
pg.time.set_timer(birdflap, 200)
# Tupe
tupe_image = pg.image.load('assets/pipe-green.png').convert()
tupe_image_under = pg.image.load('assets/pipe-green00.png').convert()

# Floor 
floor = pg.image.load('assets/floor.png').convert()
floor = pg.transform.scale(floor, (400,100))
floor_x = 0
floor_v = 1  

# Music
flap_sound = pg.mixer.Sound('assets/sound/sfx_wing.wav')
point_sound = pg.mixer.Sound('assets/sound/sfx_point.wav')
hit_sound = pg.mixer.Sound('assets/sound/sfx_hit.wav')
die_sound = pg.mixer.Sound('assets/sound/sfx_die.wav')
swooshing_sound = pg.mixer.Sound('assets/sound/sfx_swooshing.wav')
played = False

# Message
message_image = pg.image.load('assets/message.png').convert_alpha()
message_image = pg.transform.scale2x(message_image)
message_image_rect = message_image.get_rect(center = (WIDTH/2, HEIGHT/2) )

a = True
while a:
    screen.blit(background_image, (0, 0))
    screen.blit(message_image,message_image_rect)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            a = False
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE:
                running = True
                a = False
                swooshing_sound.play()
    
    pg.display.flip()
while running:
    clock.tick(60)
    screen.fill(GREEN)
    screen.blit(background_image, (0, 0))

    # tube 1
    tupe1_image = pg.transform.scale(tupe_image,(TUBE_WIDTH, tube1_height)) 
    tube1_rect = screen.blit(tupe1_image, (tube1_x, 0) )

    tube01_y = tube1_height + TUBE_GAP

    tupe01_image = pg.transform.scale(tupe_image_under, (TUBE_WIDTH, HEIGHT - tube01_y))
    tube01_rect = screen.blit(tupe01_image, (tube1_x, tube01_y))
    # tube 2 

    tupe2_image = pg.transform.scale(tupe_image,(TUBE_WIDTH, tube2_height)) 
    tube2_rect = screen.blit(tupe2_image, (tube2_x, 0) )

    tube02_y = tube2_height + TUBE_GAP
    
    tupe02_image = pg.transform.scale(tupe_image_under, (TUBE_WIDTH, HEIGHT - tube02_y))
    tube02_rect = screen.blit(tupe02_image, (tube2_x, tube02_y))

    # tube 3
    tupe3_image = pg.transform.scale(tupe_image,(TUBE_WIDTH, tube3_height)) 
    tube3_rect = screen.blit(tupe3_image, (tube3_x, 0) )

    tube03_y = tube3_height + TUBE_GAP
   
    tupe03_image = pg.transform.scale(tupe_image_under, (TUBE_WIDTH, HEIGHT - tube03_y))
    tube03_rect = screen.blit(tupe03_image, (tube3_x, tube03_y))

    tube1_x = tube1_x - TUBE_VELOCITY
    tube2_x = tube2_x - TUBE_VELOCITY
    tube3_x = tube3_x - TUBE_VELOCITY

    if pausing == False:
        rotated_bird = rotate_bird(bird_image)
    # Draw BIRD
    #bird_rect = pg.draw.rect(screen, RED, (BIRD_X, bird_y,BIRD_WIDTH , BIRD_HEIGHT))
    bird_rect = screen.blit(rotated_bird, (BIRD_X,bird_y))

    # bird falls
    bird_y += bird_drop_velocity
    bird_drop_velocity += GRAVITY


    if tube1_x < -TUBE_WIDTH :
        tube1_x = WIDTH + 150
        tube1_height = randint(100, 300)
        tube1_pass = False

    if tube2_x < -TUBE_WIDTH:
        tube2_x = WIDTH + 150
        tube2_height = randint(100, 300)
        tube2_pass = False

    if tube3_x < -TUBE_WIDTH:
        tube3_x = WIDTH + 150
        tube3_height = randint(100, 300)
        tube3_pass = False

    score_display('main game')

    if tube1_x + TUBE_WIDTH <= BIRD_X and tube1_pass == False:
        score += 1
        tube1_pass = True
        point_sound.play()
    if tube2_x + TUBE_WIDTH <= BIRD_X and tube2_pass == False:
        score += 1
        tube2_pass = True
        point_sound.play()
    if tube3_x + TUBE_WIDTH <= BIRD_X and tube3_pass == False:
        score += 1
        tube3_pass = True
        point_sound.play()

    # check collision
    for tube in [tube1_rect, tube2_rect, tube3_rect, tube01_rect, tube02_rect, tube03_rect]:
        if bird_rect.colliderect(tube) :
            TUBE_VELOCITY = 0
            bird_drop_velocity = 0
            if score > high_score:
                high_score = score
            if played == False:
                hit_sound.play()
                played = True
            game_over = pg.image.load('assets/gameover.png').convert_alpha()
            game_over = pg.transform.scale(game_over,(200,50))
            game_over_rect = game_over.get_rect(center = (WIDTH/2,300)) 
            screen.blit(game_over, game_over_rect)
            press_space_txt = font1.render("Press BackSpace to Restart", True, BLACK)
            press_space_txt_rect = press_space_txt.get_rect(center = (WIDTH/2,400))
            screen.blit(press_space_txt, press_space_txt_rect)
            floor_v = 0
            pausing = True
            score_display('game over')
        if bird_y >= 530:
            TUBE_VELOCITY = 0
            bird_drop_velocity = 0
            if score > high_score:
                high_score = score
            if played == False:
                die_sound.play()
                played = True
            game_over = pg.image.load('assets/gameover.png').convert_alpha()
            game_over = pg.transform.scale(game_over,(200,50))
            game_over_rect = game_over.get_rect(center = (WIDTH/2,300)) 
            screen.blit(game_over, game_over_rect)
            press_space_txt = font1.render("Press BackSpace to Restart", True, BLACK)
            press_space_txt_rect = press_space_txt.get_rect(center = (WIDTH/2,400))
            screen.blit(press_space_txt, press_space_txt_rect)
            floor_v = 0
            pausing = True
            score_display('game over')
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        if event.type == pg.KEYDOWN and pausing == False:
            if event.key == pg.K_SPACE:
                flap_sound.play()
                bird_drop_velocity = 0
                bird_drop_velocity -= 7
        if event.type == pg.KEYDOWN:
            if pausing and event.key == pg.K_BACKSPACE:
                # reset
                bird_y = 250
                tube1_x = 400
                tube2_x = 600
                tube3_x = 800 
                TUBE_VELOCITY = 3
                score = 0
                pausing = False
                floor_v = 1
                played = False
    draw_floor()
    floor_x -= floor_v

    if floor_x == -WIDTH:
        floor_x = 0
    pg.display.flip()

with open('high_score.txt','r+') as f:
    f.write(str(high_score))
pg.quit()








