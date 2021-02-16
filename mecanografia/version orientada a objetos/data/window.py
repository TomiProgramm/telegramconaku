import pygame
import sys
from .config import *

class Window():

    def __init__(self):

        # screen
        self.screen = pygame.display.set_mode([SCREEN_W, SCREEN_H])

        # text view
        self.textview = pygame.Surface([TEXT_VIEW_W, TEXT_VIEW_H])

        # play bar
        self.playbar = pygame.Surface([PLAY_BAR_W, PLAY_BAR_H])

        # text intro
        self.textintro = pygame.Surface([TEXT_INTRO_W, TEXT_INTRO_H])

        # clock
        self.clock = pygame.Surface([CLOCK_W, CLOCK_H])

        # button restart
        self.button_restart = pygame.Surface([BUTTON_RESTART_W, BUTTON_RESTART_H])
        self.button_restart_rect = pygame.Rect(BUTTON_RESTART_RECT)


    def fill(self, end, collide):
        self.screen.fill(BLUE)
        self.textview.fill(WHITE)
        self.playbar.fill(B_GRAY)
        self.textintro.fill(WHITE)
        self.clock.fill(BLUE)

        if end:
            if collide:
                self.button_restart.fill(L_BLUE)
            else:
                self.button_restart.fill(D_L_BLUE)
        else:
            self.button_restart.fill(DARK)


    def structure(self):

        #play bar
        self.playbar.blit(self.textintro, TEXT_INTRO_POS)
        self.playbar.blit(self.clock, CLOCK_POS)
        self.playbar.blit(self.button_restart, BUTTON_RESTART_POS)

        # screen
        self.screen.blit(self.textview, TEXT_VIEW_POS)
        self.screen.blit(self.playbar, PLAY_BAR_POS)



