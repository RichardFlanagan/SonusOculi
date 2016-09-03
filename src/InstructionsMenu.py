"""
Displays the instructions.

@author: RichardFlanagan - A00193644
@version: 21 April 2014
"""

import pygame
import sys



class InstructionsMenu():

    def __init__(self, params, debugParam):
        """
        Initialize variables.

        @param params: The list of parameter objects.
        """
        (self.screen, self.FPS, self.clock, self.music, self.sfx) = params
        self.DEBUG = debugParam




    def run(self):
        """
        Runs the instructions screen.

        @return: Exit status. Signals what screen comes next.
        """
        self.music.fadeout(1000)
        self.music.load(self.music.instructions)
        self.music.play(-1)

        pygame.mouse.set_visible(True)

        background = pygame.Surface(self.screen.get_size())
        background.fill((0, 0, 0))
        self.screen.blit(background, (0, 0))

        while True:
            self.clock.tick(self.FPS)

            for event in pygame.event.get():
                # Close the window.
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit(0)

                # Click on screen.
                if event.type == pygame.MOUSEBUTTONDOWN:
                    return 1

                # Keyboard input.
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit(0)

            self.printText()

            pygame.display.flip()

        return 1




    def printText(self):
        """
        Print text to the screen.
        """
        font1 = pygame.font.SysFont("COURIER", 32)
        t = ("Instructions")
        self.screen.blit(font1.render(t, 0, (0, 255, 0)), (self.screen.get_width()/2-font1.size(t)[0]/2, 50))

        font2 = pygame.font.SysFont("COURIER", 16)
        ins = ("-Description-",
               "You are trapped in the hive of lethal insectoids under ",
               "the earth's crust with no hope of escape.",
               "Kill as many of them before they kill you and burrow",
               "to the surface."
               "Use your trusty weapons and advanced sonar tech to",
               "reveal the predators in the darkness.",
               "",
               "-Controls-",
               "<wasd> : Move",
               "<1,2,3> : Weapons",
               "[SHIFT] : Sprint",
               "[LeftClick] : Shoot",
               "[RightClick] : Sonar",
               " ",
               "Click to begin...")

        counter = 0
        for i in ins:
            counter+=1
            self.screen.blit(font2.render(i, 0, (0, 255, 0)),
                             (self.screen.get_width()/2-font1.size(t)[0]/2-150, 150+30*counter))


