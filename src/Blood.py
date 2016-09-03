"""
Plays the death animation.

@author: RichardFlanagan - A00193644
@version: 19 April 2014
"""

import pygame



class Blood(pygame.sprite.Sprite):

    def __init__(self, screenParam, x, y):
        """
        Initialize variables.

        @param screenParam: The surface to draw the resources onto.
        """
        pygame.sprite.Sprite.__init__(self)
        self.screen = screenParam
        self.image = pygame.image.load("../res/images/blood/blood06.png")
        self.tranColor = self.image.get_at((1,1))
        self.image.set_colorkey(self.tranColor)
        self.rect = self.image.get_rect()

        self.imagePath = "../res/images/blood/blood0"
        self.imageList = []
        self.frame = 0
        self.delay = 3
        self.pause = self.delay
        self.loadPics()
        self.delete = False

        self.rect.centerx = x
        self.rect.centery = y




    def update(self):
        """
        Update object.
        Invoked each tick.
        """
        self.pause -= 1
        if self.pause <= 0:
            self.pause = self.delay
            self.frame += 1
            if self.frame >= 6:
                self.delete = True
                self.frame = 0
            self.image = self.imageList[self.frame]




    def loadPics(self):
        """
        Load all images to a list.
        """
        for frame in range(1,7):
            imageName = "%s%d.png" %(self.imagePath, frame)
            tempImage = pygame.image.load(imageName).convert_alpha()
            self.imageList.append(tempImage)



