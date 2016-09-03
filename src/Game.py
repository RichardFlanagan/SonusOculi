"""
Handles the operation of the game.

@author: RichardFlanagan - A00193644
@version: 15 April 2014
"""

import pygame
import sys
from Player import Player
from Chaser import Chaser
from Reticule import Reticule
from GunHandler import GunHandler
from Sonar import Sonar
from PlayerSonar import PlayerSonar
from Interceptor import Interceptor
from HUD import HUD
from PlayerHealth import PlayerHealth
from Blood import Blood
from Wanderer import Wanderer




class Game():

    def __init__(self, params, debugParam):
        """
        Initialize variables.

        @param params: The list of parameter objects.
        """
        (self.screen, self.FPS, self.clock, self.music, self.sfx) = params
        self.DEBUG = debugParam

        self.playerList = pygame.sprite.OrderedUpdates()
        self.hudList = pygame.sprite.OrderedUpdates()
        self.bulletList = pygame.sprite.OrderedUpdates()
        self.enemyList = pygame.sprite.OrderedUpdates()
        self.sonarList = pygame.sprite.OrderedUpdates()
        self.bloodList = pygame.sprite.OrderedUpdates()

        self.sonarTimer = int(pygame.time.get_ticks())
        self.sonarTimerDelay = 1000
        self.sonarRadius = 250
        self.maxEnemies = 32
        self.wanderSpawnTimer = int(pygame.time.get_ticks())
        self.wanderSpawnDelay = 30000
        self.i = 0



    def run(self):
        """
        Runs the game.

        @return: Exit status. Signals what screen comes next.
        """
        self.music.fadeout(1000)
        self.music.load(self.music.game)
        self.music.play(-1)

        pygame.mouse.set_visible(False)
        self.background = pygame.Surface(self.screen.get_size())
        self.background.fill((0, 0, 0))
        self.screen.blit(self.background, (0, 0))

        # Game objects.
        cursor = Reticule(self.screen)
        player = Player(self.screen, self.DEBUG)
        playerSonar = PlayerSonar(self.screen, player)
        self.sonarList.add(playerSonar)
        gun = GunHandler(self.screen, player, self.sfx, self.DEBUG)
        hud = HUD(self.screen, player, self.clock, gun)
        playerHealth = PlayerHealth(self.screen, player)

        # Sprite Lists.
        self.playerList.add(player)
        self.hudList.add(playerHealth)
        self.hudList.add(cursor)
        self.hudList.add(hud)


        # Main game loop.
        while (player.health > 0):
            self.clock.tick(self.FPS)
            self.addEnemies(player)

            pygame.time.wait(5)

            for event in pygame.event.get():

                # Close the window.
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit(0)

                # Keyboard input.
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit(0)
                    elif event.key == pygame.K_1:
                        gun.setGun(gun.k_pistol)
                    elif event.key == pygame.K_2:
                        gun.setGun(gun.k_shotgun)
                    elif event.key == pygame.K_3:
                        gun.setGun(gun.k_smg)
                pygame.event.clear()

            # Mouse Button Press.
            self.handleMouse(player, gun)

            # Update Sprite Lists.
            self.handleCollisions(player)
            self.handleSonar(player)
            self.updateScreen()

        if not self.DEBUG:
            self.addScore(player.score)

        return 2




    def addScore(self, score):
        """
        Add the player's score to the high score file.
        """
        f = open("../res/highscores.txt", "a")
        f.write("{0}\n".format(score))
        f.close()




    def addEnemies(self, player):
        """
        Add enemies to the game.

        @param player: The player's object.
        """
        if len(self.enemyList) < self.maxEnemies:
            spawn = [0, 0]
            for i in xrange(2, 6):
                self.enemyList.add(Chaser(self.screen, player))
                spawn[0] += 1
            for j in xrange(0, 3):
                self.enemyList.add(Interceptor(self.screen, player))
                spawn[1] += 1

            if self.DEBUG:
                print "Spawned {0} Chasers, {1} Interceptors.".format(spawn[0], spawn[1])

        if int(pygame.time.get_ticks()) >= self.wanderSpawnTimer+self.wanderSpawnDelay:
            self.enemyList.add(Wanderer(self.screen, player))
            self.wanderSpawnTimer = int(pygame.time.get_ticks())
            if self.DEBUG:
                print "Spawned 1 Wanderer"




    def handleMouse(self, player, gun):
        """
        Test for a mouse press, and handle a press exists.

        @param player: The player's object.
        @param gun: The gun handler.
        """
        (b1, b2, b3) = pygame.mouse.get_pressed()
        if b1 and gun.canShoot(gun.currentState):
            self.bulletList.add(gun.shoot())
        elif b2:
            print "stub"
        elif b3:
            if int(pygame.time.get_ticks()) >= self.sonarTimer+self.sonarTimerDelay:
                self.sonarList.add(Sonar(self.screen, player, self.sfx))
                self.sonarTimer = int(pygame.time.get_ticks())




    def handleCollisions(self, player):
        """
        Handle collisions and out-of-bounds checks.

        @param player: The player's object.
        """
        for i in self.enemyList:

            # Enemy collides with Bullet.
            if pygame.sprite.spritecollide(i, self.bulletList, True):
                if i.type == "chaser":
                    player.score += 10
                elif i.type == "intercept":
                    player.score += 25
                elif i.type == "wander":
                    player.score += 100
                self.bloodList.add(Blood(self.screen, i.rect.centerx, i.rect.centery))
                self.enemyList.remove(i)

            # Collide with player.
            if pygame.sprite.spritecollide(i, self.playerList, False):
                if i.type == "wander":
                    player.health += 20
                    self.sfx.play(self.sfx.health)
                elif not self.DEBUG:
                    player.health -= 10
                    self.sfx.play(self.sfx.hurt)
                self.enemyList.remove(i)


        for i in self.bulletList:
            # Bullet out-of-bounds.
            if i.checkBounds():
                self.bulletList.remove(i)


        # Blood animation time-out.
        for i in self.bloodList:
            if i.delete == True:
                self.bloodList.remove(i)




    def handleSonar(self, player):
        """
        Handles the Sonar and enemy reveal.

        @param player: The player's object.
        """
        for i in self.sonarList:
            # Enemy within radius.
            for j in self.enemyList:
                if i.inCircle(j.rect.centerx, j.rect.centery):
                    j.setState(1)

            # Reach max radius.
            if i.radius > self.sonarRadius:
                self.sonarList.remove(i)




    def updateScreen(self):
        """
        Updates and draws the resources to the screen.
        """
        allSpritesList = pygame.sprite.OrderedUpdates()

        self.sonarList.update()

        allSpritesList.add(self.bloodList)
        allSpritesList.add(self.bulletList)
        allSpritesList.add(self.enemyList)
        allSpritesList.add(self.playerList)
        allSpritesList.add(self.hudList)

        allSpritesList.clear(self.screen, self.background)
        allSpritesList.update()
        allSpritesList.draw(self.screen)

        pygame.display.flip()

        self.screen.blit(self.background, (0, 0))



