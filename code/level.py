import pygame 
from settings import *
from player import Player
from overlay import Overlay
from sprites import General

class Level:
    def __init__(self):
        self.display_surface = pygame.display.get_surface()
        self.all_sprites = CameraGroup()
        self.player = None
        self.setup()
        self.overlay = Overlay(self.player)

    def setup(self):
        General(pos = (0,0), surf = pygame.image.load('graphics/world/ground.png'). convert_alpha(), groups = self.all_sprites)
        self.player = Player((640, 360), self.all_sprites)

    def run(self,dt):
        self.display_surface.fill('black')
        self.all_sprites.custom_draw()
        self.all_sprites.update(dt)
        self.overlay.display()

class CameraGroup(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.display_surface = pygame.display.get_surface()

    def custom_draw(self):
        for sprite in self.sprites():
            self.display_surface.blit(sprite.image, sprite.rect)