"""
Handles the operation of the background music.

@author: RichardFlanagan - A00193644
@version: 16 April 2014
"""

import pygame

pygame.mixer.init()




class MusicPlayer():

    def __init__(self, debugParam):
        """
        Initialize variables.
        """
        self.game = "../res/music/Luftrausers.ogg"
        self.menu = "../res/music/AnEnding.ogg"
        self.menu2 = "../res/music/InTheHouseInAHeartbeat.ogg"
        self.instructions = "../res/music/TheBeginning.ogg"
        self.gameOver = "../res/music/ThenThereWere2.ogg"
        self.load(self.menu)
        self.playMusic = True
        self.DEBUG = debugParam
        self.currentSongName = "NONE"




    def load(self, song):
        """
        Loads the specified song.

        @param song: The string which points to the selected song.
        """
        self.currentSongName = song
        self.currentSong = pygame.mixer.music.load(song)




    def play(self, loop):
        """
        Play the loaded song.

        @param loop: How many times to loop the song. -1 is infinite.
        """
        if self.playMusic:
            pygame.mixer.music.play(loop)




    def fadeout(self, fadeout):
        """
        Reduce the current song's volume to 0 over the specified time in milliseconds.

        @param fadeout: The millisecond time over which the music will fade out.
        """
        pygame.mixer.music.fadeout(fadeout)




    def toggleMusic(self):
        """
        Toggle music player.
        """
        if self.playMusic == True:
            self.playMusic = False
            pygame.mixer.music.stop()
        elif self.playMusic == False:
            self.playMusic = True
            pygame.mixer.music.play(-1)



