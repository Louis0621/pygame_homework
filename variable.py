import pygame

class Variable:
 
    def __init__(self, health = 100, level = 1):
        self.font = pygame.font.Font(None, 36)
        self.health = health
        self.level = level
        self.weapon_type = ['Shotgun', 'Pistol', 'Flame projector', 'Laser']
        self.attribute = ["metal", "wind", "fire", "light"]
        self.text = ["You are the hero to save the planet",
                     "People are suffering from the monsters",
                     "So we must use different weapons to give them a shot",
                     "You can left click to shoot"
                     ,"Press Q to switch the weapon"]
        self.loseTheGame = ["Game Over", "Now you are the same of the world"]
    def update(self, game_window, index = 0):
        health_text = self.font.render("Health: " + str(self.health), True, (0, 0, 0))
        weapon_text = self.font.render("Weapon: " + str(self.weapon_type[index]), True, (0, 0, 0))
        level_text = self.font.render("Level: " + str(self.level), True, (0, 0, 0))
        game_window.blit(health_text, (10, 10))
        game_window.blit(weapon_text, (10, 40))
        game_window.blit(level_text, (10, 70))