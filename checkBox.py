import pygame
class CheckBox:
    def __init__(self):
        self.font = ['Test mode', 'Easy mode', 'Intermediate mode', 'Hard mode']
        self.delay = [200, 150, 100, 40]
        self.checkbox_rect = []
    def showAll(self, game_window):
        font = pygame.font.Font(None, 32)
        for i in range(4):
            font_surface = font.render(self.font[i], True, (0, 0, 0))
            self.checkbox_rect.append(pygame.Rect(100, 100 + i * 25, 20, 20))
            game_window.blit(font_surface, (self.checkbox_rect[i].right + 10, self.checkbox_rect[i].top))
    def drawAll(self, game_window):
        for checkBox in self.checkbox_rect:
            pygame.draw.rect(game_window, (0, 0, 0), checkBox, 2)
    def updateAll(self, idx, game_window):
        self.drawAll(game_window)
        pygame.draw.line(game_window, (0, 0, 0), (self.checkbox_rect[idx].left + 3, self.checkbox_rect[idx].centery), (self.checkbox_rect[idx].right - 3, self.checkbox_rect[idx].centery), 3)
        pygame.draw.line(game_window, (0, 0, 0), (self.checkbox_rect[idx].centerx, self.checkbox_rect[idx].top + 3), (self.checkbox_rect[idx].centerx, self.checkbox_rect[idx].bottom - 3), 3)
        