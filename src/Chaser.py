"""
The basic enemy object. Chases the player.

@author: RichardFlanagan - A00193644
@version: 15 April 2014
"""

import pygame
import math
import random
from Vector2D import Vector2D



class Chaser(pygame.sprite.Sprite):

    def __init__(self, screenParam, playerParam):
        """
        Initialize variables.

        @param screenParam: The surface to draw the resources onto.
        @param playerParam: The player's object.
        """
        pygame.sprite.Sprite.__init__(self)
        self.screen = screenParam
        self.player = playerParam
        self.type = "chaser"

        # Image Variables.
        self.imageMaster = pygame.image.load("../res/images/Chaser_invis.png").convert()
        self.image = pygame.image.load("../res/images/Chaser_invis.png").convert()
        self.tranColor = self.image.get_at((19,19))
        self.image.set_colorkey(self.tranColor)
        self.rect = self.image.get_rect()

        # Position Variables.
        self.spawn()
        self.trueX = float(self.rect.centerx)
        self.trueY = float(self.rect.centery)
        self.speed = 3

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
        self.updateDirection()
        self.checkState()

        self.rect.centerx = (int) (self.trueX)
        self.rect.centery = (int) (self.trueY)




    def spawn(self):
        """
        Set the spawn position of the enemy.
        """
        w = self.screen.get_width()
        h = self.screen.get_height()

        self.rect.centerx = random.randrange(0, w)
        self.rect.centery = random.randrange(h, h+200)




    def updatePosition(self):
        """
        Calculate the object's new position.
        Move to new position.
        """
        # Find the velocity vector (self to target)
        vec = Vector2D(self.player.rect.centerx - self.trueX,
                          self.player.rect.centery - self.trueY)

        # Multiply the unit vector by the speed and add it to the true positions.
        self.trueX += vec.normalized().getX() * self.speed
        self.trueY += vec.normalized().getY() * self.speed




    def updateDirection(self):
        """
        Updates the direction that the object faces.
        """
        # Find the velocity vector (self to target)
        orig = Vector2D(0,1)    # Must be facing down
        target = Vector2D(self.player.rect.centerx - self.trueX,
                          self.player.rect.centery - self.trueY)

        # Calculate the dot product of the vectors
        dotx = orig.getX() * target.getX()
        doty = orig.getY() * target.getY()

        # Calculate the angle between the spawn vector and the target vector.
        # Formula: cos(@) = (Ax.Bx + Ay.By) / (|Avec| * |Bvec|)
        angle = (dotx + doty) / (orig.magnitude() * target.magnitude())
        angle = math.acos(angle)

        # Rotate and assign the image.
        if (target.getX() > orig.getX()):
            self.image = pygame.transform.rotate(self.imageMaster, math.degrees(angle))
        else:
            self.image = pygame.transform.rotate(self.imageMaster, -math.degrees(angle))
        self.rect = self.image.get_rect()
        self.image.set_colorkey(self.tranColor)




    def setState(self, state):
        """
        Set the object to the specified state.

        @param state: The new state to change to.
        """
        self.currentState = state
        if state == self.k_invisible:
            self.imageMaster = pygame.image.load("../res/images/Chaser_invis.png").convert()
        elif state == self.k_pinged:
            self.imageMaster = pygame.image.load("../res/images/Chaser_ping.png").convert()
            self.pingTimer = int(pygame.time.get_ticks())




    def checkState(self):
        """
        Handles state specific updates.
        """
        if self.currentState == self.k_pinged:
            if int(pygame.time.get_ticks()) >= self.pingTimer+self.pingTimerDelay:
                self.setState(self.k_invisible)



