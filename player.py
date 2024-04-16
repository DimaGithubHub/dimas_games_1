import pygame
class Player:
    def __init__(self):
        pygame.init()
        self.player_pos = (600, 500)
    
    def draw_player(self, screen, color, r):
        pygame.draw.circle(screen, color, self.player_pos, r)
