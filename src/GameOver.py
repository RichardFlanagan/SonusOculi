"""
Handles the operation of the game over screen.

@author: RichardFlanagan - A00193644
@version: 15 April 2014
"""

import pygame
import sys



class GameOver():

    def __init__(self, params, debugParam):
        """
        Initialize variables.

        @param params: The list of parameter objects.
        """
        (self.screen, self.FPS, self.clock, self.music, self.sfx) = params
        self.DEBUG = debugParam




    def run(self):
        """
        Runs the game over screen.

        @return: Exit status. Signals what screen comes next.
        """
        self.music.fadeout(1000)
        self.music.load(self.music.gameOver)
        self.music.play(-1)

        pygame.mouse.set_visible(True)

        background = pygame.Surface(self.screen.get_size())
        background.fill((0, 0, 0))
        self.screen.blit(background, (0, 0))

        keepGoing = True

        highscoresButton = pygame.image.load("../res/images/b_scores.png")
        quitButton = pygame.image.load("../res/images/b_quit.png")

        while keepGoing:
            self.clock.tick(self.FPS)

            for event in pygame.event.get():
                # Close the window.
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit(0)

                # Click on screen.
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if (self.testMouse(self.screen.get_width()/2-100, 500, 200, 50)):
                        self.sfx.play(self.sfx.button)
                        return 4
                    elif (self.testMouse(self.screen.get_width()-250, 650, 200, 50)):
                        pygame.quit()
                        sys.exit(0)
                # Keyboard input.
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit(0)

            self.printText()

            self.screen.blit(highscoresButton, (self.screen.get_width()/2-100,500))
            self.screen.blit(quitButton, (self.screen.get_width()-250, 650))
            pygame.display.flip()

        return 0




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
        Print text to the screen.
        """
        font1 = pygame.font.SysFont("COURIER", 32)
        t = ("Game Over")
        self.screen.blit(font1.render(t, 0, (0, 255, 0)), (self.screen.get_width()/2-font1.size(t)[0]/2, 50))

        font2 = pygame.font.SysFont("COURIER", 16)
        ins = ("You have fallen to the creatures of the cave. ",
                "It was only a matter of time, even the best warriors ",
                "will be overwhelmed by those sheer numbers.",
                "Remember, pinging your enemy is crucial to your survival. ",
                "Stealth is their friend.",
                " ",
                "Try again?")

        counter = 0
        for i in ins:
            counter+=1
            self.screen.blit(font2.render(i, 0, (0, 255, 0)),
                             (self.screen.get_width()/2-font1.size(t)[0]/2-150, 150+30*counter))



