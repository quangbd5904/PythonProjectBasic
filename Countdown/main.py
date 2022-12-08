import pygame as pg 
import time
import math
def check_click(a,b,c,d):
    if (a < mouse_x < a+c) and (b < mouse_y < b+d):
        return True
    else:
        return False

pg.init()
screen = pg.display.set_mode((500,600))
pg.display.set_caption("Đồng hồ đếm ngược")

GREY = (150,150,150)
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
font = pg.font.SysFont('sans', 50)
text_1 = font.render('+', True, BLACK)
text_2 = font.render('-', True, BLACK)
text_3 = font.render('Start', True, BLACK)
text_4 = font.render('Reset', True, BLACK)

total = 0
total_secs = 0
start = False
running = True
clock = pg.time.Clock()

while running:
    screen.fill(GREY)
    clock.tick(60)
    mouse_x,mouse_y = pg.mouse.get_pos()
   
    pg.draw.rect(screen,WHITE,(100,50,50,50))
    pg.draw.rect(screen,WHITE,(100,200,50,50))
    pg.draw.rect(screen,WHITE,(200,50,50,50))
    pg.draw.rect(screen,WHITE,(200,200,50,50))
    pg.draw.rect(screen,WHITE,(300,50,150,50))
    pg.draw.rect(screen,WHITE,(300,200,150,50))

    pg.draw.rect(screen,BLACK,(50,520,400,50))
    pg.draw.rect(screen,WHITE,(60,530,380,30))

    pg.draw.circle(screen, BLACK, (250,400),100)
    pg.draw.circle(screen, WHITE, (250,400),95)

    screen.blit(text_1,(112,45))
    screen.blit(text_1,(212,45))
    screen.blit(text_2,(117,193))
    screen.blit(text_2,(217,193))
    screen.blit(text_3, (328,45))
    screen.blit(text_4, (318,195))
    for event in pg.event.get():
        if event.type == pg.MOUSEBUTTONDOWN:
            if event.button == 1:
                if check_click(100,50,50,50):
                    total_secs += 60
                    total = total_secs
                if check_click(100,200,50,50):
                    total_secs -= 60
                    total = total_secs
                if check_click(200,50,50,50):
                    total_secs +=1
                    total = total_secs
                if check_click(200,200,50,50):
                    total_secs -= 1
                    total = total_secs
                if check_click(300,200,150,50):
                    total_secs = 0
                    total = total_secs
                if check_click(300,50,150,50):
                    start = True
                    total = total_secs
        if event.type == pg.QUIT:
            running = False
    
    if start:
        total_secs -= 0.03
        time.sleep(0.03)
        if total_secs == 0:
            start = False
    if total_secs < 0:
        total_secs = 0
    
    min = int(total_secs/60)
    secs = int(total_secs - min*60)
    
    x_sec = 250 + 90 * math.sin(6 * secs * math.pi/180)
    y_sec = 400 - 90 * math.cos(6 * secs * math.pi/180)
    pg.draw.line(screen, BLACK,(250,400), (x_sec,y_sec))

    x_min = 250 + 40 * math.sin(6 * min * math.pi/180)
    y_min = 400 - 40 * math.cos(6 * min * math.pi/180)
    pg.draw.line(screen, RED,(250,400), (x_min,y_min))
    min = str(min)
    secs= str(secs)
    if len(min) == 1:
        min = "0" + min
    if len(secs) == 1:
        secs = "0" +secs
    
    time_now = min + "  :  " + secs
    text_time = font.render(time_now, True, BLACK)
    screen.blit(text_time,(100,120))
    if total != 0:
        pg.draw.rect(screen, RED, (60,530,int(380*(total_secs/ total)),30))
    pg.display.flip()

pg.quit()