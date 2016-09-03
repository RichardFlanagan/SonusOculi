"""
Game Development 2.2 Assignment : Main

@author: RichardFlanagan - A00193644
@version: 15 April 2014
"""

import pygame
from MainMenu import MainMenu
from Game import Game
from GameOver import GameOver
from OptionsMenu import OptionsMenu
from MusicPlayer import MusicPlayer
from SFXPlayer import SFXPlayer
from HighScores import HighScores
from InstructionsMenu import InstructionsMenu


pygame.init()
pygame.mixer.init()


# Screen Variables.
CAPTION = "Sonus Oculi"
ICON = "../res/images/icon.png"
WIDTH = 1024
HEIGHT = 768
FPS = 30





def main():
    """
    Controls the games flow.
    Loads menus and game.
    """
    # DEBUG MODE
    # -Shows intercept targets.
    # -Prints spawns to the console.
    # -No player damage
    # -Infinite smg ammunition.
    # -Scores not counted.

    DEBUG = False
    params = (setUpScreen(), FPS, pygame.time.Clock(), MusicPlayer(DEBUG), SFXPlayer())
    state = 0

    while True:
        while (state == 0): # Main menu
            state = MainMenu(params, DEBUG).run()
        while (state == 1): # Game
            state = Game(params, DEBUG).run()
        while (state == 2): # Game Over
            state = GameOver(params, DEBUG).run()
        while (state == 3): # Options
            (state, DEBUG) = OptionsMenu(params, DEBUG).run()
        while (state == 4): # Scores
            state = HighScores(params, DEBUG).run()
        while (state == 5):
            state = InstructionsMenu(params, DEBUG).run()




def setUpScreen():
    """
    Creates the display.
    """
    pygame.display.set_icon(pygame.image.load(ICON))
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption(CAPTION)
    pygame.key.set_repeat(10,10)
    return screen




if __name__=="__main__":
    main()
