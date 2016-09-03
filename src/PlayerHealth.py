"""
Draws the player's health.

@author: RichardFlanagan - A00193644
@version: 19 April 2014
"""

import pygame



class PlayerHealth(pygame.sprite.Sprite):

    def __init__(self, screenParam, playerParam):
        """
        Initialize variables.

        @param screenParam: The surface to draw the resources onto.
        @param playerParam: The player's object.
        """
        pygame.sprite.Sprite.__init__(self)
        self.screen = screenParam
        self.player = playerParam
        self.font = pygame.font.SysFont("None", 16)




    def update(self):
        """
        Updates information.
        Invoked each tick.
        """
        self.drawHealth()




    def drawHealth(self):
        """
        Draws the player's health under the player sprite.
        """
        text = "%d" % (self.player.health)
        (x, y) = self.font.size(text)
        self.image = self.font.render(text, 1, (0, 255, 255))
        self.rect = pygame.Rect(self.player.trueX-x/2, self.player.trueY+y/2, x, y)



