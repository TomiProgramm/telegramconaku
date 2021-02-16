from .config import *
from random import randint
import pygame
import os


class Words():

    def __init__(self):
        self.words = ( open( os.path.join( os.path.dirname(__file__), 'text.txt' ) ) ).read().lower().split()
        self.wordhistory = list()
        self.correct_words = int()
        self.wrong_words = int()
        self.total_words = int()
        self.average_words = float()

    def select_words(self, game):
        self.selected_words = list()
        self.writingposition = int()

        limit = 22
        top = 11

        while True:
            word = self.words[randint(0, len(self.words)-1)]
            rect = game.text.write(word, WORDS_SIZE, 'topleft', [limit, top], game.window.textview, 0)
            limit += rect.width + 22

            if limit >= TEXT_VIEW_W:

                if top == 11:
                    top *= 5
                    limit = 22
                    continue

                else:
                    break

            else:
                self.selected_words.append({'word':word, 'rect':rect, 'state':None, 'color':WHITE})

    def count(self):
        for word in self.wordhistory:
            if word.get('state') == 'wrong': self.wrong_words += 1
            elif word.get('state') == 'correct': self.correct_words += 1

        self.total_words = self.wrong_words + self.correct_words

        try: self.average_words = float(str('{0:.2f}'.format(self.correct_words / self.total_words * 100)))
        except: pass


    def fill(self, textview):
        self.selected_words[self.writingposition]['color'] = B_GRAY

        for dataword in self.selected_words:
            rect = dataword.get('rect')
            color = dataword.get('color')

            pygame.draw.rect(textview, color, rect)




