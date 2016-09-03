"""
Handles the sonar operation.

@author: RichardFlanagan - A00193644
@version: 16 April 2014
"""

import pygame



class Sonar(pygame.sprite.Sprite):

    def __init__(self, screenParam, playerParam, sfx):
        """
        Initialize variables.

        @param screenParam: The surface to draw the resources onto.
        @param playerParam: The player's object.
        @param sfx: The sound effect handler.
        """
        pygame.sprite.Sprite.__init__(self)
        self.screen = screenParam
        self.player = playerParam
        self.radius = 60

        sfx.play(sfx.ping)




    def update(self):
        """
        Update radius and draw.
        Invoked each tick.
        """
        self.radius += 20
        self.draw()




    def draw(self):
        """
        Draw the circle to the screen.
        """
        pygame.draw.circle(self.screen, (0, 255, 0),
                           (self.player.rect.centerx, self.player.rect.centery),
                           self.radius, 1)




    def inCircle(self, x, y):
        """
        Test to see if the supplied point is inside/on the sonar's radius.
        Formula: (cx-px)^2 + (cy-py)^2 <= r^2     # c:center, p:point, r:radius

        @param x: The x-position of the point to test.
        @param y: The y-position of the point to test.
        @return: The Boolean True if within/on the circle, False if outside.
        """
        if ((self.player.rect.centerx - x)**2 + (self.player.rect.centery - y)**2) <= self.radius**2:
            return True
        else:
            return False



