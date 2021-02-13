import pygame
import sys
import os
import io
from random import randint
from datetime import datetime


pygame.init()

# CONFIG
BLACK  =   0,   0,   0
DARK   =  72,  72,  92
WHITE  = 235, 235, 235 
BLUE   =  58, 142, 213 
BLUE_  =  58, 110, 213
BLUE__ =  58, 182, 235
GRAY   = 120, 120, 120
RED    = 240,  60,   5
GREEN  =  56, 213,   8


class Game:
    def __init__(self):
        # screen
        self.screen = pygame.display.set_mode([500, 200])
        pygame.display.set_caption('Mecanografía')
        # text view
        self.textview = pygame.Surface([450, 95])
        self.tv_line1 = pygame.Surface([450, 47.5])
        self.tv_line2 = pygame.Surface([450, 47.5])
        # play screen
        self.playscreen = pygame.Surface([450, 62])
        # text intro
        self.textintro = pygame.Surface([258, 48])
        self.keys = """
        q w e r t y u i o p
         a s d f g h j k l ñ
          z x c v b n m
        """.split()
        # clock
        self.clock = pygame.Surface([68, 48])
        # restart
        self.restart = pygame.Surface([48, 48])
        #start
        self.start()

    def start(self):
        self.running = True
        self.play = False
        self.set_values()
        self.read()
        self.run()

    def set_values(self):
        self.clock_value = 60
        self.textinput = str()
        self.selected_words = list()
        self.writingposition = int()
        self.wordhistory = list()
        self.wrong_types = int()
        self.correct_types = int()
        self.wrong_pre_types = int()
        self.correct_pre_types = int()
        self.endGame = False
        self.correct_words = int()
        self.wrong_words = int()
        self.total_types = int()
        self.total_words = int()
        self.average_words = int()
        self.average_types = int()

    def read(self):

        # words
        self.text = ( open( os.path.join( os.path.dirname(__file__), 'text.txt' ) ) ).read().lower().split()
        self.words = list()
        for word in self.text:
            word = str().join([w for w in list(filter(lambda w: w in self.keys, word))])
            if word: self.words.append(word)

    def define_words(self, mode=0):
        words = list()

        if mode == 1:
            for word in self.selected_words:
                if word['line'] is self.tv_line2:
                    words.append(word['word'])

            self.selected_words = list()

        line = self.tv_line1
        limit = 22
        i = 0

        while True:
            
            word = self.words[randint(0, len(self.words)-1)]

            if mode == 1 and i < len(words):
                word = words[i]
                i += 1
            
            rect = self.insert_text(word, 26, [limit, 23.75], line, mode=1)

            if (limit + rect.width) > line.get_rect().right:
                if line is self.tv_line1:
                    line = self.tv_line2
                    limit = 22
                elif line is self.tv_line2:
                    break
            else:
                limit += rect.width + 22
                self.selected_words.append({'word':word, 'rect':rect, 'line':line, 'state':None})


    def run(self):
        while self.running:
            self.events()
            self.draw()
            self.update()

    def events(self):
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                self.running = False

            if event.type == pygame.KEYDOWN:
                key = pygame.key.name(event.key)
 
                if not self.endGame:

                    if not self.play:
                        if key == 'space':
                            self.play = True
                            self.define_words()
                            self.time = Time()
                    else:
                        if key == 'space':
                            self.write_controller(2)
                            self.typing_control(2)

                        if key in self.keys:
                            self.textinput += key
                            self.typing_control(1)

                        if key == 'backspace':
                            self.textinput = self.textinput[0 : len(self.textinput)-1]

                else:
                    if key == 'r':
                        self.start()


        if not self.endGame:
            if self.play:
                self.write_controller(1)
                self.time.update()
                self.clock_value = self.time.counter
                if self.clock_value == 0:
                    self.endGame = True
        else:
            if self.play:
                for word in self.wordhistory:
                    if word['state'] == 'wrong':
                        self.wrong_words += 1
                    if word['state'] == 'correct':
                        self.correct_words += 1

                self.total_words = self.correct_words + self.wrong_words
                try:
                    self.average_words = self.correct_words / self.total_words * 100
                except ZeroDivisionError:
                    self.average_words = 0
                
                self.total_types = self.correct_types + self.wrong_types
                try:
                    self.average_types = self.correct_types / self.total_types  * 100
                except ZeroDivisionError:
                    self.average_words = 0

                print(f'Palabras correctas: {self.correct_words}')
                print(f'Palabras incorrectas: {self.wrong_words}')
                print(f'Palabras totales: {self.total_words}')
                print('Promedio de palabras correctas: %{0:.2f}'.format(self.average_words))

                print(f'Pulsaciones correctas: {self.correct_types}')
                print(f'Pulsaciones incorrectas: {self.wrong_types}')
                print(f'Pulsaciones totales: {self.total_types}')
                print('Promedio de pulsaaciones correctas: %{0:.2f}'.format(self.average_types))

                self.play = False
            




    def typing_control(self, mode):
        if mode == 1:
            self.write_controller(1)
            if self.selected_words[self.writingposition]['state'] == 'wrong':
                self.wrong_pre_types += 1
            else:
                self.correct_pre_types += 1

        if mode == 2:
            self.correct_types += self.correct_pre_types
            self.wrong_types += self.wrong_pre_types
            self.wrong_pre_types = 0
            self.correct_pre_types = 0
        

    def write_controller(self, controll):
        dataword = self.selected_words[self.writingposition]
        
        if controll == 1:
            dataword['state'] = 'writing'
            word = dataword.get('word')

            if len(self.textinput) > len(word):
                dataword['state'] = 'wrong'

            elif self.textinput != word[0 : len(self.textinput)]:
                dataword['state'] = 'wrong'

            elif self.textinput == word:
                dataword['state'] = 'correct'

        if controll == 2:
            if dataword['state'] != 'correct':
                dataword['state'] = 'wrong'
            
            self.wordhistory.append(dataword)
            self.writingposition += 1

            if self.selected_words[self.writingposition]['line'] is self.tv_line2:
                self.writingposition = 0
                self.define_words(1)
            
            self.textinput = str()






    def draw(self):
        # fill
        self.screen.fill(BLUE)
        self.textview.fill(WHITE)
        self.tv_line1.fill(WHITE)
        self.tv_line2.fill(WHITE)
        self.playscreen.fill(BLUE_)
        self.textintro.fill(WHITE)
        self.clock.fill(DARK)
        if self.endGame: self.restart.fill(BLUE__)
        else: self.restart.fill(GRAY)

        # write
        self.write()

        # draw
            # play screen
        self.playscreen.blit(self.textintro, [28, 7])
        self.playscreen.blit(self.clock, [300, 7])
        self.playscreen.blit(self.restart, [380, 7])
            # text view
        self.textview.blit(self.tv_line1, [0, 0])
        self.textview.blit(self.tv_line2, [0, 47.5])
            # screen
        self.screen.blit(self.textview, [25, 12.5])
        self.screen.blit(self.playscreen, [25, 126])      

    def update(self):
        pygame.display.flip()

    def write(self):
        # clock
        self.insert_text(str(self.clock_value), 40, self.clock.get_rect().center, self.clock)
        # text intro
        self.insert_text(self.textinput, 40, self.textintro.get_rect().center, self.textintro)
        # restart
        if self.endGame: self.insert_text('R', 40, self.restart.get_rect().center, self.restart)
        # words in text view
        if self.play:
            for dataword in self.selected_words:
                word = dataword.get('word')
                rect = dataword.get('rect')
                line = dataword.get('line')
                state = dataword.get('state')
                color = 0,0,0

                if dataword is self.selected_words[self.writingposition]:
                    color = GRAY
                else:
                    if state == None: color = WHITE
                    elif state == 'writing': color = GRAY
                    elif state == 'wrong': color = RED
                    elif state == 'correct': color = GREEN

                pygame.draw.rect(line, color, rect)
                self.insert_text(word, 26, rect.center, line)
        


    def insert_text(self, text, size, center, surface, mode=0):
        font = pygame.font.Font(pygame.font.match_font('Verdana'), size)
        txt = font.render(text, True, BLACK)
        rect = txt.get_rect()
        if mode == 0:
            rect.center = center
            surface.blit(txt, rect)
        elif mode == 1:
            # in mode 1, center is midleft
            rect.midleft = center
            return rect

    
class Time():
    def __init__(self):
        self.limit = 60
        self.counter = self.limit
        self.time_start = datetime.now()
        self.last_seconds = -1

    def update(self):
        count = datetime.now() - self.time_start
        if count.seconds != self.last_seconds:
            self.last_seconds = count.seconds
            self.counter = self.limit - self.last_seconds



# start
game = Game()
        



