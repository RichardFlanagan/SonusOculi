"""
The player object.

@author: RichardFlanagan - A00193644
@version: 15 April 2014
"""

import pygame
import math
from Vector2D import Vector2D
from pygame.locals import K_w, K_a, K_s, K_d, K_LSHIFT



class Player(pygame.sprite.Sprite):

    def __init__(self, screenParam, debugParam):
        """
        Initialize variables.

        @param screenParam: The surface to draw the resources onto.
        @param debug: Toggle debug options.
        """
        pygame.sprite.Sprite.__init__(self)
        self.screen = screenParam
        self.debug = debugParam

        # Image Variables.
        self.imageMaster = pygame.image.load("../res/images/Player.png").convert()
        self.image = pygame.image.load("../res/images/Player.png").convert()
        self.tranColor = self.image.get_at((1,1))
        self.image.set_colorkey(self.tranColor)
        self.rect = self.image.get_rect()

        # Position Variables.
        self.rect.centerx = self.screen.get_width() / 2.0
        self.rect.centery = self.screen.get_height() / 2.0
        self.trueX = float(self.rect.centerx)
        self.trueY = float(self.rect.centery)

        # Player Variables.
        self.health = 100
        self.score = 0
        self.normalSpeed = 3.0
        self.lastMove = Vector2D(0, 0)




    def update(self):
        """
        Update movement, direction etc.
        Invoked each tick.
        """
        self.checkBounds()
        self.updatePosition()
        self.updateDirection()

        self.rect.centerx = (int) (self.trueX)
        self.rect.centery = (int) (self.trueY)




    def updatePosition(self):
        """
        Calculate the object's new position.
        Move to new position.
        """
        # Sprint check.
        speed = self.normalSpeed
        if pygame.key.get_pressed()[K_LSHIFT]:
            speed = self.normalSpeed * 2.0

        # Make vectors.
        vec = Vector2D(0, 0)
        diagMove = math.cos(math.pi/4.0)*speed

        # Direction check.
        if pygame.key.get_pressed()[K_w] and pygame.key.get_pressed()[K_a]:
            vec = Vector2D(-diagMove, -diagMove)
        elif pygame.key.get_pressed()[K_w] and pygame.key.get_pressed()[K_d]:
            vec = Vector2D(diagMove, -diagMove)
        elif pygame.key.get_pressed()[K_s] and pygame.key.get_pressed()[K_a]:
            vec = Vector2D(-diagMove, diagMove)
        elif pygame.key.get_pressed()[K_s] and pygame.key.get_pressed()[K_d]:
            vec = Vector2D(diagMove, diagMove)

        elif pygame.key.get_pressed()[K_w]:
            vec = Vector2D(0, -speed)
        elif pygame.key.get_pressed()[K_s]:
            vec = Vector2D(0, speed)
        elif pygame.key.get_pressed()[K_a]:
            vec = Vector2D(-speed, 0)
        elif pygame.key.get_pressed()[K_d]:
            vec = Vector2D(speed, 0)

        # Assign new position.
        self.trueX += vec.getX()
        self.trueY += vec.getY()
        self.lastMove = vec




    def updateDirection(self):
        """
        Updates the direction that the object faces.
        """
        # Find the velocity vector (self to target)
        orig = Vector2D(0,1)    # Must be facing down
        target = Vector2D(pygame.mouse.get_pos()[0] - self.trueX,
                          pygame.mouse.get_pos()[1] - self.trueY)

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
        """
        if self.trueY > self.screen.get_height()-10:
            self.trueY = self.screen.get_height()-10
        elif self.trueY < 70:
            self.trueY = 70
        elif self.trueX < 10:
            self.trueX = 10
        elif self.trueX > self.screen.get_width()-10:
            self.trueX = self.screen.get_width()-10



