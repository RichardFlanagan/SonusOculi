"""
Handles the operation of the options menu.

@author: RichardFlanagan - A00193644
@version: 16 April 2014
"""

import pygame
import sys



class OptionsMenu():

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

        # Load button images.
        if self.music.playMusic:
            musicButton = pygame.image.load("../res/images/b_musicOn.png")
        else:
            musicButton = pygame.image.load("../res/images/b_musicOff.png")

        if self.sfx.playSFX:
            sfxButton = pygame.image.load("../res/images/b_soundOn.png")
        else:
            sfxButton = pygame.image.load("../res/images/b_soundOff.png")

        if self.DEBUG:
            debugButton = pygame.image.load("../res/images/b_debugOn.png")
        else:
            debugButton = pygame.image.load("../res/images/b_debugOff.png")

        backButton = pygame.image.load("../res/images/b_back.png")

        while True:
            self.clock.tick(self.FPS)

            for event in pygame.event.get():
                # Close the window.
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit(0)

                # Click on screen.
                if event.type == pygame.MOUSEBUTTONDOWN:

                    # Music Play-back.
                    if (self.testMouse(self.screen.get_width()/2-100, 200, 200, 50)):
                        if self.music.playMusic == True:
                            musicButton = pygame.image.load("../res/images/b_musicOff.png")
                            self.music.toggleMusic()
                        elif self.music.playMusic == False:
                            musicButton = pygame.image.load("../res/images/b_musicOn.png")
                            self.music.toggleMusic()
                        self.sfx.play(self.sfx.button)

                    # Sound Effect Play-back.
                    if (self.testMouse(self.screen.get_width()/2-100, 300, 200, 50)):
                        if self.sfx.playSFX == True:
                            sfxButton = pygame.image.load("../res/images/b_soundOff.png")
                            self.sfx.toggleSFX()
                        elif self.sfx.playSFX == False:
                            sfxButton = pygame.image.load("../res/images/b_soundOn.png")
                            self.sfx.toggleSFX()
                        self.sfx.play(self.sfx.button)

                    # Debug mode.
                    if (self.testMouse(self.screen.get_width()/2-100, 400, 200, 50)):
                        if self.DEBUG == True:
                            debugButton = pygame.image.load("../res/images/b_debugOff.png")
                            self.DEBUG = False
                        elif self.DEBUG == False:
                            debugButton = pygame.image.load("../res/images/b_debugOn.png")
                            self.DEBUG = True
                        self.sfx.play(self.sfx.button)

                    # Back to menu.
                    elif (self.testMouse(self.screen.get_width()-250, 650, 200, 50)):
                        self.sfx.play(self.sfx.button)
                        return (0, self.DEBUG)

                # Keyboard input.
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit(0)

            self.printText()

            self.screen.blit(musicButton, (self.screen.get_width()/2-100,200))
            self.screen.blit(sfxButton, (self.screen.get_width()/2-100,300))
            self.screen.blit(debugButton, (self.screen.get_width()/2-100,400))
            self.screen.blit(backButton, (self.screen.get_width()-250, 650))
            pygame.display.flip()

        return (0, self.DEBUG)




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
        t = ("Options")
        self.screen.blit(font1.render(t, 0, (0, 255, 0)), (self.screen.get_width()/2-font1.size(t)[0]/2, 50))



