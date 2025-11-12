from settings import *
import pygame

class Overlay:
    def __init__(self, player):
        self.display_surface = pygame.display.get_surface()
        self.player = player

        #imports
        overlay_path = 'graphics/overlay/'
        self.tools_surface = {tool:pygame.image.load(f'{overlay_path}{tool}.png').convert_alpha() for tool in player.tools}
        self.seeds_surface = {seed:pygame.image.load(f'{overlay_path}{seed}.png').convert_alpha() for seed in player.seeds}

    def display(self):
        tool_surface = self.tools_surface[self.player.selected_tool]
        self.display_surface.blit(tool_surface,(0,0))