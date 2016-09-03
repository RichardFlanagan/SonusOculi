"""
Handles the operation of the high score menu.

@author: RichardFlanagan - A00193644
@version: 16 April 2014
"""

import pygame
import sys



class HighScores():

    def __init__(self, params, debugParam):
        """
        Initialize variables.

        @param params: The list of parameter objects.
        """
        (self.screen, self.FPS, self.clock, self.music, self.sfx) = params
        self.DEBUG = debugParam




    def run(self):
        """
        Runs the options menu screen.

        @return: Exit status. Signals what screen comes next.
        """
        pygame.mouse.set_visible(True)

        background = pygame.Surface(self.screen.get_size())
        background.fill((0, 0, 0))
        self.screen.blit(background, (0, 0))

        backButton = pygame.image.load("../res/images/b_back.png")

        self.generateScores()

        while True:
            self.clock.tick(self.FPS)

            for event in pygame.event.get():

                # Close the window.
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit(0)

                # Click on screen.
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if (self.testMouse(self.screen.get_width()-250, 650, 200, 50)):
                        self.sfx.play(self.sfx.button)
                        return 0

                # Keyboard input.
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit(0)

            self.screen.blit(backButton, (self.screen.get_width()-250, 650))

            self.printText()
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
        Print text and high score table to the screen.
        """
        font1 = pygame.font.SysFont("COURIER", 32)
        t = ("High Scores")
        self.screen.blit(font1.render(t, 0, (0, 255, 0)), (self.screen.get_width()/2-font1.size(t)[0]/2, 50))


        lineCounter = 1
        font2 = pygame.font.SysFont("COURIER", 16)
        f = open("../res/highscores.txt", "r")
        for line in f:
            line = "{0:6}.    {1}".format(lineCounter, line.rstrip())
            self.screen.blit(font2.render(line, 0, (0, 255, 0)),
                             (self.screen.get_width()/2-font1.size(t)[0]/2, 100+50*lineCounter))
            lineCounter+=1
        f.close()




    def generateScores(self):
        """
        Create the high score list from the scores file,
        clear the file,
        then write back to the score file.
        """
        # Read from file.
        f = open("../res/highscores.txt", "r")
        lines = []
        for line in f:
            line = int("{0}".format(line.rstrip()))
            lines.append(line)
        lines.sort(reverse=True)
        lines = lines[0:10]
        f.close()

        # Clear file.
        open("../res/highscores.txt","w").close()

        # Write to file.
        f = open("../res/highscores.txt", "w")
        for i in lines:
            f.write("{0}\n".format(i))

        f.close()





