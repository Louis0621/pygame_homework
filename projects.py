import pygame
import pygame.mixer as mixer
import mobManager as manager
import variable as va
import character as ch
pygame.init()
mixer.init()
SOUND_EFFECT  = ["sound_effect_shotGun.mp3", "pistol.mp3", "fireShot.mp3", "laser.mp3"]
WINDOW_SIZE = (1200, 700)

BACKGROUND_IMAGE = "background.png"

game_window = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("The shooting game")

# Load the background image and scale it to fit the window
background_image = pygame.image.load(BACKGROUND_IMAGE)
background_image = pygame.transform.scale(background_image, WINDOW_SIZE)

# Set up the game clock
clock = pygame.time.Clock()

# The protagonist
character = ch.Character()
hand = ch.Hand()

# Start the game loop
animation_timer = 0
animation_delay = 10
monster_timer = 0
monster_delay = 80
 

# Upgrade timer
upgrade = 0
upgrade_level = 1

trigger_timer = 0
# GunFire movement
trigger_delay = 10
running = True

index = 0
# Hand movements
index2 = 0
rotate_hand = False
click_time = 0

# Mob
manager= manager.MobManager(game_window)


# Gun
gun = ch.Gun()

# Gun swtich
gun_idx = 0
# Gun delay
gun_delay = [300, 250, 500, 400]

# Variable
var = va.Variable()

# intro
duration = 15000
init_time = pygame.time.get_ticks()
idx = 0
general_dur = 3000

# gun_cold
flag = True
gun_delay_cold = 0
cold_time = 0


mixer.Sound('intro.mp3').play()

GameOver = False
while running:
     
    
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if GameOver == False and event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and flag:  # Check for left click
            rotate_hand = True
            click_time = pygame.time.get_ticks()  # Record the time of the left click
            index2 = 1  # Switch to the second hand picture
            sound_effect = mixer.Sound(SOUND_EFFECT[gun_idx])
            sound_effect.play()
            flag = False
            manager.attack(gun_idx)
            cold_time = gun_delay[gun_idx]
            gun_delay_cold = pygame.time.get_ticks()
        if  GameOver == False and  event.type == pygame.KEYDOWN:
          if event.key == pygame.K_q:
              gun_idx += 1 
              gun_idx = gun_idx % len(gun.files)
              gun.get_img(gun_idx)         
              
    curr = pygame.time.get_ticks()
    
    
    
    if flag == False and (curr - gun_delay_cold) >= cold_time:
        flag = True
                
    # Draw the background image
    game_window.blit(background_image, (0, 0))
        
    # Sprawn
    
    demage = manager.update()
    if demage != 0:
        var.health -= demage
        var.health = max(var.health, 0)
        if var.health == 0:
            GameOver = True
            init_time = pygame.time.get_ticks()
            idx = 0
        
    # Introduction
    offset = curr - init_time
    if GameOver == False and offset < duration:
        font = pygame.font.Font(None, 36)
        tmp = font.render(var.text[idx], True, (255, 255, 255))
        game_window.blit(tmp, (500, 70))
        temp = general_dur
        if idx == 2:
            temp = 500 + general_dur
        else:
            temp = general_dur
            
        if offset > (idx + 1) * temp:
            idx += 1
            idx %= len(var.text)
            font = None
    #GameOver
    if GameOver == True and offset < 6000:
        
        font = pygame.font.Font(None, 36)
        tmp = font.render(var.loseTheGame[idx], True, (255, 255, 255))
        game_window.blit(tmp, (500, 70))
        
        if offset > (idx + 1) * (general_dur + 1):
            idx += 1
            idx %= len(var.loseTheGame)
            font = None
    
    
    # Draw the left hand
    if rotate_hand:
        if pygame.time.get_ticks() - click_time >= gun_delay[gun_idx]:  # Check if 2 seconds have passed
            rotate_hand = False  # Reset rotate_hand
            index2 = 0  # Switch back to the first hand picture
    hand.update(game_window, index2, 85, 600, 3.5)
    gun.update(game_window, index2, 105, 599)
    
    # Draw other game elements here
    
    character.update(game_window, index, 40, 575, 3.5)  # Adjust the position and scale as needed
    
    # Display the variables
    var.update(game_window, gun_idx)
    
    # Update the display
    pygame.display.update()
    animation_timer += 1
    if animation_timer >= animation_delay:
        index = (index + 1) % len(character.files)
        animation_timer = 0
        
    # Monster's timer
    monster_timer += 1
    if monster_timer >= monster_delay:
        manager.spawn(var.level)
        monster_timer = 0
        
    upgrade += 1
    if GameOver == False and var.level < 5 and upgrade == (1500 * upgrade_level):
        mixer.Sound('upgrade.mp3').play()
        var.level += 1
        upgrade_level += 1
        var.health = 100 + (50 * (var.level - 1))
        monster_delay -= 10
        
    elif GameOver == False and var.level >= 5 and upgrade == (1500 * upgrade_level):
        if var.level % 5 == 0:
            manager.spawn_boss(var.level)
        mixer.Sound('upgrade.mp3').play()
        var.level += 1
        upgrade_level += 1
        var.health = 300
        monster_delay *= 0.9
    
    # Tick the clock to enforce a maximum frame rate
    clock.tick(60)

# Clean up the game and quit Pygame
pygame.quit()