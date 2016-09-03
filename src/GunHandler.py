"""
The handler for the player's gun.

@author: RichardFlanagan - A00193644
@version: 19 April 2014
"""

import pygame
from Bullet import Bullet



class GunHandler(pygame.sprite.Sprite):

    def __init__(self, screenParam, playerParam, sfxParam, debugParam):
        """
        Initialize variables.

        @param screenParam: The surface to draw the resources onto.
        @param playerParam: The player's object.
        @param sfxParam: The sound effect handler.
        """
        pygame.sprite.Sprite.__init__(self)
        self.screen = screenParam
        self.player = playerParam
        self.sfx = sfxParam
        self.DEBUG = debugParam

        # State Variables.
        self.k_pistol = 0
        self.k_shotgun = 1
        self.k_smg = 2
        self.currentState = self.k_pistol
        self.gunString = "Pistol  "

        self.bulletTimer = int(pygame.time.get_ticks())
        self.pistolDelay = 600
        self.shotgunDelay = 1000
        self.smgDelay = 100
        self.smgAmmo = 20

        self.gunChangeTimer = int(pygame.time.get_ticks())
        self.gunChangeDelay = 800




    def shoot(self):
        """
        Shoots the currently selected gun.

        @return: The bullets which have been fired.www
        """
        if self.currentState == self.k_pistol:
            return self.shootPistol()
        elif self.currentState == self.k_shotgun:
            return self.shootShotgun()
        elif self.currentState == self.k_smg:
            return self.shootSMG()




    def setGun(self, gun):
        """
        Set the gun to the specified state.

        @param gun: The gun to be assigned.
        """
        if gun == self.k_pistol:
            self.currentState = self.k_pistol
            self.gunString = "Pistol  "
            if int(pygame.time.get_ticks()) >= self.gunChangeTimer+self.gunChangeDelay:
                self.sfx.play(self.sfx.pistolReload)
                self.gunChangeTimer = int(pygame.time.get_ticks())
        elif gun == self.k_shotgun:
            self.currentState = self.k_shotgun
            self.gunString = "Shotgun "
            if int(pygame.time.get_ticks()) >= self.gunChangeTimer+self.gunChangeDelay:
                self.sfx.play(self.sfx.shotgunReload)
                self.gunChangeTimer = int(pygame.time.get_ticks())
        elif gun == self.k_smg:
            self.currentState = self.k_smg
            self.gunString = "SMG     "
            if int(pygame.time.get_ticks()) >= self.gunChangeTimer+self.gunChangeDelay:
                self.sfx.play(self.sfx.smgReload)
                self.gunChangeTimer = int(pygame.time.get_ticks())




    def canShoot(self, state):
        """
        Check whether the specified gun can shoot.

        @param state: The gun to test for.
        @return: Boolean True for ability to shoot.
        """
        if state == self.k_pistol:
            if int(pygame.time.get_ticks()) >= self.bulletTimer+self.pistolDelay:
                return True
        elif state == self.k_shotgun:
            if int(pygame.time.get_ticks()) >= self.bulletTimer+self.shotgunDelay:
                return True
        elif state == self.k_smg:
            if int(pygame.time.get_ticks()) >= self.bulletTimer+self.smgDelay:
                return True
        return False




    def shootPistol(self):
        """
        Single bullet, medium reload delay.

        @return: The bullet object.
        """
        if int(pygame.time.get_ticks()) >= self.bulletTimer+self.pistolDelay:
            self.sfx.play(self.sfx.pistol)
            self.bulletTimer = int(pygame.time.get_ticks())
            return Bullet(self.screen, self.player, 15)




    def shootSMG(self):
        """
        Single bullet, small reload delay.

        @return: The bullet object.
        """
        if int(pygame.time.get_ticks()) >= self.bulletTimer+self.smgDelay:
            self.sfx.play(self.sfx.smg)
            self.bulletTimer = int(pygame.time.get_ticks())

            if not self.DEBUG:
                self.smgAmmo -= 1
            if self.smgAmmo == 0:
                self.smgAmmo = 20
                self.smgDelay = 3000
                self.sfx.play(self.sfx.smgReload)
            else:
                self.smgDelay = 100
            return Bullet(self.screen, self.player, 25)




    def shootShotgun(self):
        """
        Multiple bullets, spread formation, long reload delay.

        @return: The list of shotgun pellets.
        """
        if int(pygame.time.get_ticks()) >= self.bulletTimer+self.shotgunDelay:
            self.sfx.play(self.sfx.shotgun)
            self.bulletTimer = int(pygame.time.get_ticks())
            bulletList = pygame.sprite.OrderedUpdates()
            for i in range(0, 5):
                bulletList.add(Bullet(self.screen, self.player, 60))
            return bulletList



