"""
A simple enemy object. Wanders around the screen.

@author: RichardFlanagan - A00193644
@version: 24 April 2014
"""

import pygame
import random



class CData:
    """
    Control Data.
    """
    def __init__(self, x, y):
        self.move = (x, y)



class Wanderer(pygame.sprite.Sprite):

    def __init__(self, screenParam, playerParam):
        """
        Initialize variables.

        @param screenParam: The surface to draw the resources onto.
        @param playerParam: The player's object.
        """
        pygame.sprite.Sprite.__init__(self)
        self.screen = screenParam
        self.player = playerParam
        self.type = "wander"
        self.debug = self.player.debug

        # Image Variables.
        self.image = pygame.image.load("../res/images/Wanderer_invis.png").convert()
        self.tranColor = self.image.get_at((19,19))
        self.image.set_colorkey(self.tranColor)
        self.rect = self.image.get_rect()

        # Position Variables.
        self.spawn()
        self.trueX = float(self.rect.centerx)
        self.trueY = float(self.rect.centery)
        self.speed = 4.0

        # State Variables.
        self.k_invisible = 0
        self.k_pinged = 1
        self.currentState = 0
        self.pingTimer = int(pygame.time.get_ticks())
        self.pingTimerDelay = 1000




    def update(self):
        """
        Update movement, direction etc.
        Invoked each tick.
        """
        self.updatePosition()
        self.checkState()

        self.rect.centerx = (int) (self.trueX)
        self.rect.centery = (int) (self.trueY)




    def spawn(self):
        """
        Set the spawn position of the enemy.
        """
        u = CData( 0, -1)       # up
        l = CData(-1,  0)       # left
        r = CData( 1,  0)       # right

        self.patternIndex = 0
        self.pattern = [u, u, u, u, u, u, u, u, u, u, u, u, u, u, u, u, u, u, u, u,
                        r, r, r, r, r, r, r, r, r, r, r, r, r, r, r, r, r, r, r, r,
                        u, u, u, u, u, u, u, u, u, u, u, u, u, u, u, u, u, u, u, u,
                        l, l, l, l, l, l, l, l, l, l, l, l, l, l, l, l, l, l, l, l]

        #self.rect.centerx = random.randrange(-30, 0)
        #self.rect.centery = random.randrange(100, self.screen.get_height()-100)

        self.rect.centerx = random.randrange(100, self.screen.get_width()-100)
        self.rect.centery = random.randrange(self.screen.get_height()+30, self.screen.get_height()+50)




    def updatePosition(self):
        """
        Calculate the object's new position.
        """
        self.trueX += self.pattern[self.patternIndex].move[0] * self.speed
        self.trueY += self.pattern[self.patternIndex].move[1] * self.speed

        self.patternIndex += 1
        if self.patternIndex >= len(self.pattern):
            self.patternIndex = 0

        if self.trueY < 70:
            self.trueX = random.randrange(100, self.screen.get_width()-100)
            self.trueY = random.randrange(self.screen.get_height()+30, self.screen.get_height()+50)




    def setState(self, state):
        """
        Set the object to the specified state.

        @param state: The new state to change to.
        """
        self.currentState = state
        if state == self.k_invisible:
            self.image = pygame.image.load("../res/images/Wanderer_invis.png").convert()
        elif state == self.k_pinged:
            self.image = pygame.image.load("../res/images/Wanderer_ping.png").convert()
            self.pingTimer = int(pygame.time.get_ticks())




    def checkState(self):
        """
        Handles state specific updates.
        """
        if self.currentState == self.k_pinged:
            if int(pygame.time.get_ticks()) >= self.pingTimer+self.pingTimerDelay:
                self.setState(self.k_invisible)



