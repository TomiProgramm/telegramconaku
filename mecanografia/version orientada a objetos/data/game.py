from .window import Window
from .clock import Clock
from .keyboard import Keyboard
from .text import Text
from .words import Words
from .mouse import Mouse
import pygame
import sys

class Game():

    def __init__(self):
        self.window = Window()
        self.clock = Clock()
        self.keyboard = Keyboard()
        self.text = Text()
        self.words = Words()
        self.mouse = Mouse()
        self.collide = bool()
        self.running = True
        self.play = False
        self.end = False


    def start(self):
        while self.running:
            self.events()
            self.updates()
            self.draw()
            pygame.display.flip()


    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if not self.end:
                if event.type == pygame.KEYDOWN:
                    self.key = pygame.key.name(event.key)
                    self.keyboard.keydown(self)
            
            else:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if self.collide:
                            self.__init__()

        if self.clock.time == 0:
            self.end = True

        if self.end:
            if self.play:
                self.words.count()
                self.keyboard.count()
                self.play = False
            


    def updates(self):
        if self.play and not self.end: self.clock.update()
        if self.end:
            self.mouse.update()
            self.collide = self.window.button_restart_rect.colliderect(self.mouse.pos)

    
    def draw(self):
        self.window.fill(self.end, self.collide)
        if self.play: self.words.fill(self.window.textview)
        self.text.writing(self)
        self.window.structure()






