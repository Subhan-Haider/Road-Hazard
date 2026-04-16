'''
Name: Subhan Haider
Period: 5
Date: 4/2/2026
Teacher: Mr. Philips
'''
import pygame   #Pygame libery
import random   #Random Libery
import math     #Math Libery

pygame.init()   #Initialize pygame

#variable
SIZE = (800, 450)           #Screen size variable
WHITE = (255, 255, 255)     #Color white
BLACK = (0, 0, 0)           #Color black
RED = (255, 0, 0)           #Color red
GREEN = (0, 255, 0)         #Color green
BLUE = (0, 0, 255)          #Color blue

counter = 0                 #Frame counter for spawning
cars = []                   #List to hold car data
car_images = []             #List to hold car images
x_location = 10             #Player grid X
y_location = 14             #Player grid Y
score = 0                   #Points variable
lives = 3                   #Player lives
game_state = "MENU"         #Current screen (MENU, PLAY, OVER)
invincible_timer = 0        #Timer for hit recovery

#Set up display
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption("Road Hazard")
clock = pygame.time.Clock() #Game clock for FPS

#Text Fonts
font_big = pygame.font.SysFont('freesansbold.ttf', 50, True)     #Big font for menu
font_small = pygame.font.SysFont('freesansbold.ttf', 25, True)   #Small font for UI

#Load Character image
charater_image = pygame.image.load("Characters/man.png").convert_alpha()
charater_image = pygame.transform.scale(charater_image, [25, 30])
death_image = pygame.image.load("Characters/death.png").convert_alpha()

#Load all 48 car images
for i in range(48):
    car_instance = pygame.image.load(f"Cars/{i}.png").convert_alpha()
    car_images.append(car_instance)

#Load Background tiles
bg_grass = pygame.image.load("Backgrounds/Grass1.png").convert()
bg_grass = pygame.transform.scale(bg_grass, [30, 30])
bg_road = pygame.image.load("Backgrounds/road_tile.png").convert()
bg_road = pygame.transform.scale(bg_road, [30, 30])
bg_bush = pygame.image.load("Backgrounds/bush.png").convert_alpha()
bg_bush = pygame.transform.scale(bg_bush, [30, 30])

#Load Music and Sounds
pygame.mixer.music.load("Sounds/BGMusic.ogg")
pygame.mixer.music.set_volume(0.3)
pygame.mixer.music.play(-1) #Loop forever

move_sound = pygame.mixer.Sound("Sounds/jump.wav")
hit_sound = pygame.mixer.Sound("Sounds/hit.wav")

def spawn_car(cars):
    """Function to add a new car to the list"""
    y = random.randrange(1, 14) #Random lane
    car_type = random.randrange(48) #Random car image
    speed = random.choice([3, 4, 5, 6]) #Random speed
    
    if y % 2 == 0:
        #Spawn on left moving right
        cars.append([-50, y, speed, car_type])
    else:
        #Spawn on right moving left
        cars.append([SIZE[0] + 50, y, -speed, car_type])
    return cars

done = False
while not done:
    # --- Event handling ---
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True #Close button pressed
        
        if event.type == pygame.KEYDOWN:
            if game_state == "MENU":
                if event.key == pygame.K_SPACE:
                    #Reset and start game
                    game_state = "PLAY"
                    score = 0
                    lives = 3
                    x_location = 10
                    y_location = 14
                    cars = []
            
            elif game_state == "PLAY":
                # Movement controls (Arrow keys and WASD)
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    if x_location > 0:
                        x_location -= 1
                        move_sound.play()
                elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    if x_location < 25:
                        x_location += 1
                        move_sound.play()
                elif event.key == pygame.K_UP or event.key == pygame.K_w:
                    if y_location > 0:
                        y_location -= 1
                        move_sound.play()
                        score += 10 # Points for moving up
                elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    if y_location < 14:
                        y_location += 1
                        move_sound.play()
            
            elif game_state == "OVER":
                if event.key == pygame.K_r:
                    game_state = "MENU" #Go back to menu

    # ##Logic
    if game_state == "PLAY":
        #Timer for spawning cars
        counter += 1
        spawn_rate = max(10, 30 - (score // 200)) #Faster as you get points
        if counter % spawn_rate == 0:
            cars = spawn_car(cars)

        #Check hitbox for player
        player_rect = pygame.Rect(x_location * 30 + 5, y_location * 30 + 5, 20, 25)

        #Update cars and check hits
        new_car_list = []
        for i in range(len(cars)):
            cars[i][0] += cars[i][2] #Move car
            
            #Car hitbox
            car_rect = car_images[cars[i][3]].get_rect(topleft=(cars[i][0], cars[i][1] * 30))
            
            #Collision detection
            if player_rect.colliderect(car_rect) and invincible_timer == 0:
                hit_sound.play()
                lives -= 1
                invincible_timer = 60 #1 second of safety
                x_location = 10 #Reset player
                y_location = 14
            
            #Keep cars on screen
            if -100 < cars[i][0] < SIZE[0] + 100:
                new_car_list.append(cars[i])
        
        cars = new_car_list
        
        #Decrease recovery timer
        if invincible_timer > 0:
            invincible_timer -= 1
            
        #Check if game over
        if lives <= 0:
            game_state = "OVER"
            
        #Check win (reached top)
        if y_location == 0:
            score += 500 #Big bonus
            x_location = 10
            y_location = 14

    # ##Drawing
    if game_state == "MENU":
        screen.fill(BLACK)
        txt = font_big.render("ROAD HAZARD", True, GREEN)
        screen.blit(txt, [SIZE[0]//2 - txt.get_width()//2, 150])
        txt2 = font_small.render("PRESS SPACE TO START", True, WHITE)
        screen.blit(txt2, [SIZE[0]//2 - txt2.get_width()//2, 250])
        
    elif game_state == "PLAY" or game_state == "OVER":
        #Draw the tiled background
        for r in range(15):
            for c in range(27):
                if r == 0 or r == 14:
                    screen.blit(bg_grass, [c*30, r*30])
                    if c % 5 == 0: screen.blit(bg_bush, [c*30, r*30])
                else:
                    screen.blit(bg_road, [c*30, r*30])

        #Draw all cars
        for i in range(len(cars)):
            img = car_images[cars[i][3]]
            if cars[i][2] < 0:
                img = pygame.transform.flip(img, True, False) #Flip if moving left
            screen.blit(img, [cars[i][0], cars[i][1] * 30])

        #Draw the player character (blinking if hit)
        if invincible_timer % 10 < 5:
            screen.blit(charater_image, [x_location * 30 + 2, y_location * 30])

        #Draw UI text
        score_txt = font_small.render(f"Score: {score}", True, WHITE)
        screen.blit(score_txt, [10, 10])
        lives_txt = font_small.render(f"Lives: {lives}", True, RED)
        screen.blit(lives_txt, [SIZE[0] - 100, 10])
        
        #Draw game over message
        if game_state == "OVER":
            overlay = pygame.Surface(SIZE, pygame.SRCALPHA)
            overlay.fill((0,0,0,150))
            screen.blit(overlay, [0,0])
            msg = font_big.render("GAME OVER", True, RED)
            screen.blit(msg, [SIZE[0]//2 - msg.get_width()//2, 150])
            msg2 = font_small.render("Press R to Reset", True, WHITE)
            screen.blit(msg2, [SIZE[0]//2 - msg2.get_width()//2, 250])

    pygame.display.flip() #Update screen
    clock.tick(60)        #60 FPS

pygame.quit() #Shutdown
