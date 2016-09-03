"""
Handles the operation of the main menu.

@author: RichardFlanagan - A00193644
@version: 15 April 2014
"""

import pygame
import sys



class MainMenu():

    def __init__(self, params, debugParam):
        """
        Initialize variables.

        @param params: The list of parameter objects.
        """
        (self.screen, self.FPS, self.clock, self.music, self.sfx) = params
        self.DEBUG = debugParam




    def run(self):
        """
        Runs the main menu.

        @return: Exit status. Signals what screen comes next.
        """
        if not self.music.currentSongName == self.music.menu:
            self.music.fadeout(1000)
            self.music.load(self.music.menu)
            self.music.play(-1)

        pygame.mouse.set_visible(True)

        background = pygame.image.load("../res/images/StartScreen.png").convert()
        self.screen.blit(background, (0, 0))


        playButton = pygame.image.load("../res/images/b_play.png")
        quitButton = pygame.image.load("../res/images/b_quit.png")
        optionsButton = pygame.image.load("../res/images/b_options.png")
        scoresButton = pygame.image.load("../res/images/b_scores.png")

        while True:
            self.clock.tick(self.FPS)

            for event in pygame.event.get():
                # Close the window.
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit(0)

                # Click on screen.
                if event.type == pygame.MOUSEBUTTONDOWN:

                    # Play
                    if (self.testMouse(self.screen.get_width()/2 - 150, 400, 300, 100)):
                        self.sfx.play(self.sfx.button)
                        return 5

                    # Options
                    elif (self.testMouse(self.screen.get_width()/2 - 100, 550, 200, 50)):
                        self.sfx.play(self.sfx.button)
                        return 3

                    # High Scores
                    elif (self.testMouse(self.screen.get_width()/2 - 100, 650, 200, 50)):
                        self.sfx.play(self.sfx.button)
                        return 4

                    # Quit
                    elif (self.testMouse(self.screen.get_width()-250, 650, 200, 50)):
                        pygame.quit()
                        sys.exit(0)

                # Keyboard input.
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit(0)



            self.screen.blit(playButton, (self.screen.get_width()/2 - 150, 400))
            self.screen.blit(optionsButton,(self.screen.get_width()/2 - 100, 550))
            self.screen.blit(scoresButton,(self.screen.get_width()/2 - 100, 650))
            self.screen.blit(quitButton, (self.screen.get_width()-250, 650))

            self.printText()

            pygame.display.flip()

        return 1




    def testMouse(self, x, y, width, height):
        """
        Tests to see if the mouse is within the defined box.

        @param x: The x position of the top left point of the box.
        @param y: The y position of the top left point of the box.
        @param width: The width of the box.
        @param height: The height of the box.
        @return: True if mouse is in box, false if not.
        """
        if (pygame.mouse.get_pos()[0] > x
            and pygame.mouse.get_pos()[0] < x+width
            and pygame.mouse.get_pos()[1] > y
            and pygame.mouse.get_pos()[1] < y+height):
                return True
        else:
            return False


    def printText(self):
        """
        Print the text to the screen.
        """
        font = pygame.font.SysFont("COURIER", 16)

        t = ("\xa9 Richard Flanagan - A00193644 :: All sound resources to their respective owners.")

        self.screen.blit(font.render(t, 0, (0, 255, 0)),
                        (20, self.screen.get_height()-30))




