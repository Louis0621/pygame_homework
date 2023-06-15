import pygame

class Character:
    def __init__(self):
        self.files = ['protagonist1.png', 'protagonist.png']
        self.width = 24
        self.height = 40

    def get_img(self, index):
        img = pygame.image.load(self.files[index]).convert_alpha()
        image = pygame.Surface((self.width, self.height), pygame.SRCALPHA)  # Create a surface with an alpha channel
        image.blit(img, (0, 0), (0, 0, self.width, self.height))
        return image

    def update(self, game_window, index, start_x, start_y, scale):
        character_img = self.get_img(index)
        scaled_img = pygame.transform.scale(character_img,
        (int(self.width * scale),
        int(self.height * scale)))
        game_window.blit(scaled_img, (start_x, start_y))
class Hand:
    def __init__(self):
        self.files = ['hand1.png', 'hand2.png']
        self.width = [14, 11]
        self.height = [8, 13]
    def get_img(self, index):
        img = pygame.image.load(self.files[index]).convert_alpha()
        image = pygame.Surface((self.width[index], self.height[index]), 
        pygame.SRCALPHA)  # Create a surface with an alpha channel
        image.blit(img, (0, 0), (0, 0, self.width[index], self.height[index]))
        return image
    def update(self, game_window, index, start_x, start_y, scale):
        if index == 1:
            start_y -= 10
        hand_img = self.get_img(index)
        scaled_img = pygame.transform.scale(hand_img,
         (int(self.width[index] * scale), 
        int(self.height[index] * scale)))
        game_window.blit(scaled_img, (start_x, start_y))
class Gun:
    def __init__(self):
        self.files = ["Shotgun.png", "pistol.png", "flameProjector.png", "laser gun.png"]
        self.bullet = ["shooting.png", "pistol_shooting.png", "fire.png", "laser.png"]
        self.get_img()
    def get_img(self, index = 0):
        self.index = index
        scale = 3.5
        self.image = pygame.image.load(self.files[index]).convert_alpha()
        self.bullet_image = pygame.image.load(self.bullet[index]).convert_alpha()
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.scaled_image = pygame.transform.scale(self.image,
        (int(self.width * scale), int(self.height * scale)))
        self.scaled_bullet = pygame.transform.scale(self.bullet_image,
         (int(self.bullet_image.get_width()),
         int(self.bullet_image.get_height())))
    
    def update(self, game_window, index, start_x, start_y):
        if index == 1:
            start_y -= 10
            start_x += 10
            game_window.blit(self.scaled_bullet, (start_x + 43, start_y - 5))
            rotated_img = pygame.transform.rotate(self.scaled_image, 50)  # Rotate the scaled image
            rotated_width = rotated_img.get_width()
            rotated_height = rotated_img.get_height()
            offset_x = (rotated_width - self.width) // 2
            offset_y = (rotated_height - self.height) // 2
            game_window.blit(rotated_img, (start_x - offset_x, start_y - offset_y))  # Blit the rotated image
        else:
            game_window.blit(self.scaled_image, (start_x, start_y))