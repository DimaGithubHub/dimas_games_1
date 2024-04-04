import pygame
class Map:
    def __init__(self):
        self.st = ["WWWWWWWWWWWWWWWWWWW",
              "W.................W",
              "W.................W",
              "W.................W",
              "W.................W",
              "W.................W",
              "WWWWWWWWWWWWWWWWWWW"]
        self.W = 600
        self.H = 800
    def draw (self, screen, color, r):
        pygame.init()
        
        for y, row in enumerate(self.st):
            for x, cell in enumerate(row):
                if cell == "W":
                    pygame.draw.circle(screen, color, (x * 20 + 100+180,  y* 20 + 100+180), r)
        pygame.display.flip()



# import pygame

# class Map:
#     def __init__(self):
#         self.st = ["WWWWWWWWWWWWWWWWWWW",
#                    "W.................W",
#                    "W.................W",
#                    "W.................W",
#                    "W.................W",
#                    "W.................W",
#                    "WWWWWWWWWWWWWWWWWWW"]
#         self.cell_size = 20
#         self.padding_x = 100 + 180
#         self.padding_y = 100 + 180
#         self.W = len(self.st[0]) * self.cell_size
#         self.H = len(self.st) * self.cell_size

#     def draw(self, screen, color):
#         pygame.init()

#         for y, row in enumerate(self.st):
#             for x, cell in enumerate(row):
#                 if cell == "W":
#                     rect = pygame.Rect(x * self.cell_size + self.padding_x, y * self.cell_size + self.padding_y, self.cell_size, self.cell_size)
#                     pygame.draw.rect(screen, color, rect)
#         pygame.display.flip()

# # Example usage
# if __name__ == "__main__":
#     pygame.init()
#     screen = pygame.display.set_mode((800, 600))
#     map_instance = Map()
#     map_instance.draw(screen, (255, 255, 255))


