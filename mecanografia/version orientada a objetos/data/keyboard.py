import pygame
from .config import *

pygame.init()

class Keyboard():

    def __init__(self):
        self.pre_correct_types = int()
        self.pre_wrong_types = int()

        self.correct_types = int()
        self.wrong_types = int()

        self.total_types = int()
        self.average_types = float()

        self.textinput = str()
    

    def keydown(self, game):

        if not game.play:

            if game.key == 'space':
                game.play = True
                game.clock.start_count()
                game.words.select_words(game)
        
        else:

            dataword = game.words.selected_words[game.words.writingposition]
            word = dataword.get('word')

            if game.key in KEYS:
                self.textinput += game.key
                
                if self.textinput == word[0 : len(self.textinput)]: self.pre_correct_types += 1
                elif self.textinput != word[0 : len(self.textinput)]: self.pre_wrong_types += 1

            if game.key == 'backspace':
                self.textinput = self.textinput[0 : len(self.textinput)-1]

            if game.key == 'space':

                if self.textinput == word:
                    dataword['color'] = GREEN
                    dataword['state'] = 'correct'

                elif self.textinput != word:
                    dataword['color'] = RED
                    dataword['state'] = 'wrong'

                game.words.wordhistory.append(dataword)
                game.words.writingposition += 1
                self.textinput = str()

                if game.words.writingposition == len(game.words.selected_words): game.words.select_words(game)

                self.correct_types += self.pre_correct_types
                self.wrong_types += self.pre_wrong_types

                self.pre_correct_types = 0
                self.pre_wrong_types = 0


    def count(self):
        self.wrong_types += self.pre_wrong_types
        self.correct_types += self.pre_wrong_types
        self.total_types = self.wrong_types + self.correct_types
        try: self.average_types = float(str('{0:.2f}'.format(self.correct_types / self.total_types * 100)))
        except: pass
        





            