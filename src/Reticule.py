"""
The cursor object.

@author: RichardFlanagan - A00193644
@version: 15 April 2014
"""

import pygame



class Reticule(pygame.sprite.Sprite):

    def __init__(self, screenParam):
        """
        Initialize variables.

        @param screenParam: The surface to draw the resources onto.
        """
        pygame.sprite.Sprite.__init__(self)
        self.screen = screenParam

        # Image Variables.
        self.image = pygame.image.load("../res/images/Cursor.png").convert()
        self.tranColor = self.image.get_at((1,1))
        self.image.set_colorkey(self.tranColor)
        self.rect = self.image.get_rect()

        # Position Variables.
        self.rect.centerx = pygame.mouse.get_pos()[0]
        self.rect.centery = pygame.mouse.get_pos()[1]




    def update(self):
        """
        Update information.
        Invoked each tick.
        """
        self.rect.centerx = pygame.mouse.get_pos()[0]
        self.rect.centery = pygame.mouse.get_pos()[1]



