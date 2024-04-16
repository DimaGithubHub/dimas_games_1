# 1

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


# 2
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
#         # Центрирование карты по горизонтали и вертикали в окне 800x600
#         self.padding_x = (800 - len(self.st[0]) * self.cell_size) // 2
#         self.padding_y = (600 - len(self.st) * self.cell_size) // 2

#     def draw(self, screen, color):
#         for y, row in enumerate(self.st):
#             for x, cell in enumerate(row):
#                 if cell == "W":
#                     rect = pygame.Rect(x*self.cell_size + self.padding_x, y*self.cell_size+self.padding_y, self.cell_size, self.cell_size)
#                     pygame.draw.rect(screen, color, rect)


# 3

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
#         self.num_cols = len(self.st[0])
#         self.num_rows = len(self.st)
#         self.cell_width = 800 // self.num_cols  # Ширина ячейки
#         self.cell_height = 600 // self.num_rows  # Высота ячейки
#         self.padding_x = 0
#         self.padding_y = 0
#         self.W = self.num_cols * self.cell_width
#         self.H = self.num_rows * self.cell_height

#     def draw(self, screen, color):
#         pygame.init()
#         for y, row in enumerate(self.st):
#             for x, cell in enumerate(row):
#                 if cell == "W":
#                     rect = pygame.Rect(x*self.cell_width + self.padding_x, y*self.cell_height+self.padding_y, self.cell_width, self.cell_height)
#                     pygame.draw.rect(screen, color, rect)
#         pygame.display.flip()



