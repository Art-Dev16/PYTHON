import pygame
import time
import random
import ctypes
 
usr32 = ctypes.windll.user32
width_screen =  usr32.GetSystemMetrics(0)
height_screen = usr32.GetSystemMetrics(1)


pygame.init()
 
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)
 
dis_width = width_screen
dis_height = height_screen
 
dis = pygame.display.set_mode((100,100),pygame.FULLSCREEN)
pygame.display.set_caption('Snake')
 
clock = pygame.time.Clock()
 
snake_block = 20


img_titre = pygame.image.load("img_title.jpg")
img_press_space = pygame.image.load("img_pressSpace.png")


 
font_style = pygame.font.SysFont("bahnschrift", 40)
def our_snake(snake_block, snake_list):
    for x in snake_list:
        #pygame.draw.rect(dis, green, [x[0], x[1], snake_block, snake_block])
        pygame.draw.circle(dis,green, (x[0] + 10, x[1] + 10), snake_block/2) 
       
        

 
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 5, dis_height / 3])


continu = True

 
def gameLoop():
    
    global continu
    
    game_over = False
    game_close = False

    texte_court = False
    
    score_snake = 0
    texte = "Score : " + str(score_snake)

    fps = 17

    temps = int(time.time())
 
    x1 = 300
    y1 = 300
 
    x1_change = 0
    y1_change = 0
 
    snake_List = []
    Length_of_snake = 1

    grandeur_score = 35
 
    foodx = round(random.randrange(0, dis_width - snake_block) / 20) * 20
    foody = round(random.randrange(0, dis_height - snake_block) / 20) * 20

    


    
    while continu:
        dis.fill(black)
        dis.blit(img_titre,(dis_width/2 - int(563/2), dis_height /6))
        dis.blit(img_press_space,(dis_width/2 - 348/2 + 10, dis_height /2))
    

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    continu = False

        pygame.display.update()
        

    
 
    while not game_over:
 
        while game_close == True:

            
            
            
            dis.fill(black)
            message("You Lost ! Press C-Play Again or Q-Quit", red)
            
            pygame.display.update()
 
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()
 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    game_over = True
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0
 
        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        dis.fill(black)
        pygame.draw.rect(dis, red, [foodx, foody, snake_block, snake_block])
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]
 
        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        score_font = pygame.font.SysFont("Comic Sans MS", grandeur_score)
 
        our_snake(snake_block, snake_List)

        new_temps = int(time.time())

        if new_temps == temps + 8:
            texte_court = True
            grandeur_score = 45

        
        
        if texte_court == False:
            texte = "Score : " + str(score_snake)
        if texte_court == True:
            texte = str(score_snake)
        
        aff_score = score_font.render(texte, True, blue)
        dis.blit(aff_score,(40,30))

        
 
        pygame.display.update()
 
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, dis_width - snake_block) / 20) * 20
            foody = round(random.randrange(0, dis_height - snake_block) / 20) * 20
            Length_of_snake += 1
            score_snake +=1
            
        
 
        clock.tick(fps)
 
    pygame.quit()
    quit()
 
 
gameLoop()
