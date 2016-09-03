"""
Handles the heads up display.

@author: RichardFlanagan - A00193644
@version: 19 April 2014
"""

import pygame



class HUD(pygame.sprite.Sprite):

    def __init__(self, screenParam, playerParam, clockParam, gunParam):
        """
        Initialize variables.

        @param screenParam: The surface to draw the resources onto.
        @param playerParam: The player's object.
        """
        pygame.sprite.Sprite.__init__(self)
        self.screen = screenParam
        self.player = playerParam
        self.font = pygame.font.SysFont("COURIER", 24)
        self.clock = clockParam
        self.gun = gunParam



    def update(self):
        """
        Updates information.
        Invoked each tick.
        """
        pygame.draw.rect(self.screen, (50,50,50), pygame.Rect(0,0, self.screen.get_width(), 50))
        pygame.draw.line(self.screen, (0,255,0), (0, 50), (self.screen.get_width(), 50))
        self.draw()
        self.clock.tick()



    def draw(self):
        """
        Draws the player's health under the player sprite.
        """
        text = "Health: %d    Score: %d    Weapon: %s    FPS: %d" % (self.player.health, self.player.score, self.gun.gunString, int(self.clock.get_fps()))
        self.image = self.font.render(text, 1, (0, 255, 0))
        self.rect = pygame.Rect(20, 20, 600, 100)



