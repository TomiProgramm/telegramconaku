import pygame
from .config import *

class Text():

    def writing(self, game):

        # clock
        self.write(str(game.clock.time), CLOCK_WRITING_SIZE, 'center', game.window.clock.get_rect().center, game.window.clock, 1)

        # words
        if game.play:
            for dataword in game.words.selected_words:
                word = dataword.get('word')
                rect = dataword.get('rect')

                self.write(word, WORDS_SIZE, 'topleft', rect.topleft, game.window.textview, 1)

        # input
        self.write(game.keyboard.textinput, WORDS_SIZE, 'center', game.window.textintro.get_rect().center, game.window.textintro, 1)

        # score
        if game.end:
            #words
            self.write('   [Palabras]', SCORE_SIZE_1, 'topleft', SCORE_WORD_POS, game.window.textview, 1)
            self.write(f' * Correctas   : {game.words.correct_words}', SCORE_SIZE_2, 'topleft', SCORE_CORRECT_WORD_POS, game.window.textview, 1)
            self.write(f' * Incorrectas : {game.words.wrong_words}', SCORE_SIZE_2, 'topleft', SCORE_WRONG_WORD_POS, game.window.textview, 1)
            self.write(f' * Totales       : {game.words.total_words}', SCORE_SIZE_2, 'topleft', SCORE_TOTAL_WORD_POS, game.window.textview, 1)
            self.write(f' * Promedio    : %{game.words.average_words}', SCORE_SIZE_2, 'topleft', SCORE_AVERAGE_WORD_POS, game.window.textview, 1)
            #types
            self.write('   [Pulsaciones]', SCORE_SIZE_1, 'topleft', SCORE_TYPE_POS, game.window.textview, 1)
            self.write(f' * Correctas   : {game.keyboard.correct_types}', SCORE_SIZE_2, 'topleft', SCORE_CORRECT_TYPE_POS, game.window.textview, 1)
            self.write(f' * Incorrectas : {game.keyboard.wrong_types}', SCORE_SIZE_2, 'topleft', SCORE_WRONG_TYPE_POS, game.window.textview, 1)
            self.write(f' * Totales       : {game.keyboard.total_types}', SCORE_SIZE_2, 'topleft', SCORE_TOTAL_TYPE_POS, game.window.textview, 1)
            self.write(f' * Promedio    : %{game.keyboard.average_types}', SCORE_SIZE_2, 'topleft', SCORE_AVERAGE_TYPE_POS, game.window.textview, 1)

        # restart
        if game.end:
            self.write('R', RESTART_SIZE, 'center', game.window.button_restart.get_rect().center, game.window.button_restart, 1)

    def write(self, text, size, pos_reference, pos_value, surface, mode):
        font = pygame.font.Font(pygame.font.match_font('Verdana'), size)
        txt = font.render(text, True, BLACK)
        rect = txt.get_rect()

        if pos_reference == 'center':
            rect.center = pos_value

        elif pos_reference == 'topleft':
            rect.topleft = pos_value

        if mode == 1:
            surface.blit(txt, rect)

        elif mode == 0:
            return rect
