"""
Handles the operation of the sound effects.

@author: RichardFlanagan - A00193644
@version: 16 April 2014
"""

import pygame

pygame.mixer.init()


class SFXPlayer():

    def __init__(self):
        """
        Initialize variables.
        """
        self.ping = "../res/sounds/ping.ogg"
        self.hurt = "../res/sounds/hurt.ogg"
        self.pistol = "../res/sounds/pistol.ogg"
        self.shotgun = "../res/sounds/shotgun.ogg"
        self.pistolReload = "../res/sounds/pistolReload.ogg"
        self.shotgunReload = "../res/sounds/shotgunReload.ogg"
        self.smg = "../res/sounds/pistol.ogg"
        self.smgReload = "../res/sounds/smgReload.ogg"
        self.button = "../res/sounds/beep.ogg"
        self.health = "../res/sounds/health.ogg"

        self.playSFX = True




    def play(self, sound):
        """
        Play the specified sound effect.

        @param sound: The sound to play.
        """
        if self.playSFX:
            pygame.mixer.Sound(sound).play()




    def toggleSFX(self):
        """
        Toggle sound effect player.
        """
        self.playSFX = not self.playSFX




