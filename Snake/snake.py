# Snake Game by Arthur
# github : art_dev16.github.io
# Open Source
# arthur.riviere16@gmail.com
# réalisé à partir du code sur : https://ichi.pro/fr
#
# 17/12/2021


from os import write
import pygame
import time
import random
import ctypes
 
usr32 = ctypes.windll.user32
width_screen =  usr32.GetSystemMetrics(0)       
height_screen = usr32.GetSystemMetrics(1)         # récupération des dimensions de l'écran


pygame.init()
 
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)            # Couleurs
green = (0, 255, 0)
blue = (50, 153, 213)
 
dis_width = width_screen
dis_height = height_screen         # défintion des diemsions de la fenêtre en fonction des dimensions de l'écran ( voir L8 )
 
dis = pygame.display.set_mode((100,100),pygame.FULLSCREEN)
pygame.display.set_caption('Snake')                            # initialisation de la fenêtre du jeu
 
clock = pygame.time.Clock()  # gestion du temps
 
snake_block = 20   # taille d'un bloc du serpent


img_titre = pygame.image.load("img_title.jpg")
img_press_space = pygame.image.load("img_pressSpace.png")
img_apple = pygame.image.load("apple.png").convert_alpha()          # chargement des images du jeu
img_trophée  = pygame.image.load("trophy.png").convert_alpha()


################### Fonctions du jeu ###########################

def checkIfRecord():
    global score_snake
    fichier = open("records.txt","r") 
    contenu_du_fichier = fichier.readlines()
    fichier.close()                                                   
    longueur = len(contenu_du_fichier)    
    record_inscrit = int(contenu_du_fichier[longueur - 1])
    record_inscrit = int(record_inscrit /16000000)
    
    
    

font_style = pygame.font.SysFont("bahnschrift", 40)
font_record = pygame.font.SysFont("Comic Sans MS", 140)           # définition des surfaces de texte

def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.circle(dis,green, (x[0] + 10, x[1] + 10), snake_block/2)      # gestion du dessinage des blocs du serpent
       
        
score_écrit = False

 
def message(msg, color, score_serpent, record_inscrit):
    global score_écrit

    mesg = font_style.render(msg, True, color)                # affichage "Perdu" quand partie terminée
    dis.blit(mesg, [dis_width / 5, dis_height / 3])

    ##

    if score_écrit == False:
        print("Le record précédent est ", record_inscrit)              
        if score_serpent > int(record_inscrit):
            fichier = open("records.txt","a")
            fichier.write("\n")                                  # sauvegarde du score si celui-ci est supérieur au record
            encrypté = score_serpent * 16000000                  # la sauvegarde se fait dans records.txt
            fichier.write(str(encrypté))                         # les records sont cryptés par le programme avant d'être écrit dans le txt
            print(score_serpent," écrit")
        score_écrit = True


continu = True

 
def gameLoop(): # boucle générale du jeu
    
    global continu
    
    game_over = False
    game_close = False    # game_close est True quand la partie se termine et que le message "perdu" est affiché

    texte_court = False
    
    score_snake = 0         # score
    texte = "Score : " + str(score_snake)

    fps = 17    # vitesse du mouvement du serpent

    temps = int(time.time())    # récupération du temps au moment où une partie commence
 
    x1 = 300      
    y1 = 300     # position x et y du serpent au démarrage de la partie
 
    x1_change = 0
    y1_change = 0   # gestion des directions du serpent
 
    snake_List = []    # gestion des blocs du serpent
    Length_of_snake = 1    # longueur du serpent

    score_écrit = False

    record_verif = False

    grandeur_score = 35
 
    foodx = round(random.randrange(0, dis_width - snake_block) / 20) * 20
    foody = round(random.randrange(0, dis_height - snake_block) / 20) * 20      # définition d'une position aléatoire du bloc nourriture    

    
    
    while continu:             # boucle gérant la fenêtre d'accueil du jeu
        dis.fill(black)
        dis.blit(img_titre,(dis_width/2 - int(563/2), dis_height /6))
        dis.blit(img_press_space,(dis_width/2 - 348/2 + 10, dis_height /2)) 
        dis.blit(img_trophée,(dis_width - 250,dis_height - dis_height/6))    # affichages des composants  
                                                                             #          de la page d'accueil

        if record_verif == False:
            fichier = open("records.txt","r") 
            contenu_du_fichier = fichier.readlines()
            fichier.close()                                     # récupération du record dans le txt
            longueur = len(contenu_du_fichier)                    
            record_inscrit = int(contenu_du_fichier[longueur - 1])
            record_inscrit = int(record_inscrit /16000000)
            record_verif = True

        aff_record = font_record.render(str(record_inscrit), True, (0,0,255))
        dis.blit(aff_record, (dis_width - 120, dis_height - dis_height/4.5)) # affichage du record sur la page
                                                                                    # d'accueil
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    continu = False

        pygame.display.update()
        

    
 
    while not game_over:
 
        while game_close == True:

            
            
            
            dis.fill(black)
            score_serpent = score_snake

            if record_verif == False:
                fichier = open("records.txt","r") 
                contenu_du_fichier = fichier.readlines()
                fichier.close()
                longueur = len(contenu_du_fichier)    
                record_inscrit = int(contenu_du_fichier[longueur - 1])
                record_inscrit = int(record_inscrit / 16000000)
                record_verif = True

            message("You Lost ! Press C-Play Again or Q-Quit", red, score_serpent, record_inscrit)
            
            
            
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
                    if x1_change != snake_block:
                        x1_change = -snake_block
                        y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    if x1_change != -snake_block:
                        x1_change = snake_block
                        y1_change = 0
                elif event.key == pygame.K_UP:
                    if y1_change != snake_block:
                        y1_change = -snake_block
                        x1_change = 0
                elif event.key == pygame.K_DOWN:
                    if y1_change != -snake_block:
                        y1_change = snake_block
                        x1_change = 0
 
        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        dis.fill(black)
        #pygame.draw.rect(dis, red, [foodx, foody, snake_block, snake_block])
        dis.blit(img_apple, (foodx,foody))
        snake_Head = []
        snake_Head.append(x1)                       # gestion du serpent
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]
 
        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True


        score_font = pygame.font.SysFont("Comic Sans MS", grandeur_score) #affichage du score durant la partie
 
        our_snake(snake_block, snake_List)

        new_temps = int(time.time()) # calcul du temps

        if new_temps == temps + 8:
            texte_court = True
            grandeur_score = 45
                                                                     
                                                                     
                                                      # pas important
        
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
            print("Mon score est maintenant à ", score_snake)
            
        
 
        clock.tick(fps)
 
    pygame.quit()
    quit()
 
 
gameLoop()



# Snake Game by Arthur
# github : art_dev16.github.io
# Open Source
# arthur.riviere16@gmail.com
# réalisé à partir du code sur : https://ichi.pro/fr
#
# 17/12/2021