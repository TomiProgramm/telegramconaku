import pygame

pygame.init()

class Mouse:
    def __init__(self):
        self.x, self.y = pygame.mouse.get_pos()
        self.pos = pygame.Rect(self.x, self.y, 1, 1)
    
    def update(self):
        self.x, self.y = pygame.mouse.get_pos()
        self.pos = pygame.Rect(self.x, self.y, 1, 1)

    def click(self, button):
        if button.colliderect(self.pos):
            return True