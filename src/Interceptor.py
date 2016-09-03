"""
An advanced enemy object. Attempts to intercept the player. Chases when close enough.

@author: RichardFlanagan - A00193644
@version: 18 April 2014
"""

import pygame
import math
import random
from Vector2D import Vector2D



class Interceptor(pygame.sprite.Sprite):

    def __init__(self, screenParam, playerParam):
        """
        Initialize variables.

        @param screenParam: The surface to draw the resources onto.
        @param playerParam: The player's object.
        """
        pygame.sprite.Sprite.__init__(self)
        self.screen = screenParam
        self.player = playerParam
        self.type = "intercept"
        self.debug = self.player.debug

        # Image Variables.
        self.imageMaster = pygame.image.load("../res/images/Interceptor_invis.png").convert()
        self.image = pygame.image.load("../res/images/Interceptor_invis.png").convert()
        self.tranColor = self.image.get_at((19,19))
        self.image.set_colorkey(self.tranColor)
        self.rect = self.image.get_rect()

        # Position Variables.
        self.spawn()
        self.trueX = float(self.rect.centerx)
        self.trueY = float(self.rect.centery)
        self.lastMove = Vector2D(0, 0)
        self.speed = 4.0
        self.chaseRange = 50.0

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
        vecToPlayer = Vector2D(self.player.trueX - self.trueX, self.player.trueY - self.trueY)
        if vecToPlayer.magnitude() > self.chaseRange:
            self.interceptMove()
        else:
            self.vecToTarget = vecToPlayer
        self.trueX += vecToPlayer.normalized().getX() * self.speed
        self.trueY += vecToPlayer.normalized().getY() * self.speed
        self.lastMove = self.vecToTarget.normalized() * self.speed




    def interceptMove(self):
        """
        Project the player's position and vector and us it as an intercept point to move towards.
        """
        # Variables.
        preyx = self.player.trueX
        preyy = self.player.trueY
        preyVelx = self.player.lastMove.getX()
        preyVely = self.player.lastMove.getY()
        targetOffset = 20.0

        # Relative velocity between this and prey (closing velocity).
        relativeVelVec = Vector2D(preyVelx - self.lastMove.getX(), preyVely - self.lastMove.getY())

        # Calculate targetOffset. (Time = Distance/RelativeVelocity)
        if relativeVelVec.magnitude() == 0.0:
            targetOffset = 0.0
        else:
            targetOffset = 10

        # Calculate the intercept point and vector.
        targetx = (int)(preyx + self.player.lastMove.getX() * targetOffset)
        targety = (int)(preyy + self.player.lastMove.getY() * targetOffset)

        # Limit target point to prevent overflow.
        if targetx < -1000:
            targetx = -1000
        elif targetx > 1000:
            targetx = 1000
        if targety < -1000:
            targety = -1000
        elif targety > 1000:
            targety = 1000

        self.vecToTarget = Vector2D(targetx - self.trueX, targety - self.trueY)

        # (Debug) Draw intercept point and trajectory.
        if (self.debug):
            pygame.draw.circle(self.screen, (255, 0, 0), (targetx, targety), 8, 0)
            pygame.draw.line(self.screen, (255, 0, 0), (self.trueX, self.trueY), (int(targetx), int(targety)), 1)




    def updateDirection(self):
        """
        Updates the direction that the object faces.
        """
        # The spawn vector.
        orig = Vector2D(0,1)    # Must be facing down

        # Calculate the dot product of the vectors
        dotx = orig.getX() * self.vecToTarget.getX()
        doty = orig.getY() * self.vecToTarget.getY()

        # Calculate the angle between the spawn vector and the target vector.
        # Formula: cos(@) = (Ax.Bx + Ay.By) / (|Avec| * |Bvec|)
        angle = (dotx + doty) / (orig.magnitude() * self.vecToTarget.magnitude())
        angle = math.acos(angle)

        # Rotate and assign the image.
        if (self.vecToTarget.getX() > orig.getX()):
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
            self.imageMaster = pygame.image.load("../res/images/Interceptor_invis.png").convert()
        elif state == self.k_pinged:
            self.imageMaster = pygame.image.load("../res/images/Interceptor_ping.png").convert()
            self.pingTimer = int(pygame.time.get_ticks())




    def checkState(self):
        """
        Handles state specific updates.
        """
        if self.currentState == self.k_pinged:
            if int(pygame.time.get_ticks()) >= self.pingTimer+self.pingTimerDelay:
                self.setState(self.k_invisible)



