"""
The basic bullet object.

@author: RichardFlanagan - A00193644
@version: 16 April 2014
"""

import pygame
import math
import random
from Vector2D import Vector2D



class Bullet(pygame.sprite.Sprite):

    def __init__(self, screenParam, playerParam, spreadParam):
        """
        Initialize variables.

        @param screenParam: The surface to draw the resources onto.
        @param playerParam: The player's object.
        @param sfx: The sound effect handler.
        """
        pygame.sprite.Sprite.__init__(self)
        self.screen = screenParam
        self.player = playerParam
        self.spread = spreadParam

        # Image Variables.
        self.imageMaster = pygame.image.load("../res/images/Bullet.png").convert()
        self.image = pygame.image.load("../res/images/Bullet.png").convert()
        self.tranColor = self.image.get_at((1,1))
        self.image.set_colorkey(self.tranColor)
        self.rect = self.image.get_rect()

        # Position Variables.
        self.rect.centerx = self.player.rect.centerx
        self.rect.centery = self.player.rect.centery
        self.trueX = float(self.rect.centerx)
        self.trueY = float(self.rect.centery)
        self.speed = 8

        self.accuracy = 100
        self.moveVector = self.getTargetVec()
        self.rotate()





    def update(self):
        """
        Update movement, direction etc.
        Invoked each tick.
        """
        self.checkBounds()

        self.trueX += self.moveVector.getX() * self.speed
        self.trueY += self.moveVector.getY() * self.speed

        self.rect.centerx = (int) (self.trueX)
        self.rect.centery = (int) (self.trueY)




    def getTargetVec(self):
        """
        Calculate the object's movement vector.
        """
        vec = Vector2D(pygame.mouse.get_pos()[0] - self.trueX,
                          pygame.mouse.get_pos()[1] - self.trueY)

        if vec.magnitude() > self.accuracy:
            vec = Vector2D(pygame.mouse.get_pos()[0]+random.randint(-self.spread,self.spread) - self.trueX,
                pygame.mouse.get_pos()[1]+random.randint(-self.spread,self.spread) - self.trueY)

        return vec.normalized()




    def rotate(self):
        """
        Updates the direction that the object faces.
        """
        # Find the velocity vector (self to target)
        orig = Vector2D(0,1)    # Must be facing down
        target = self.moveVector

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




    def checkBounds(self):
        """
        Test the object's position against the edge of the screen.
        Wrap if off-screen.

        @return: Boolean True if off-screen.
        """
        if self.trueY > self.screen.get_height():
            return True
        elif self.trueY < 0:
            return True
        elif self.trueX < 0:
            return True
        elif self.trueX > self.screen.get_width():
            return True
        else:
            return False



