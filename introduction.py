import pygame
pygame.init()

clock = pygame.time.Clock()
running = True
while running:
    
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
       
    # Draw the background image
   

    
    # Draw the left hand
  
    clock.tick(60)

# Clean up the game and quit Pygame
pygame.quit()