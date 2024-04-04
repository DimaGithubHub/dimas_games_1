import pygame
import sys
from map import Map
 
class game:
    def __init__(self):
        pygame.init()
        self.W = 600
        self.H = 800


        self.FPS = 60

        self.y = self.W // 2 
        self.x = self.H // 2
        self.radius = 13

        self.line_x = (self.x, self.y)
        self.line_y = (self.H, self.W)
        self.speed = 5
        
    


        self.color = (255, 255, 255)
        self.GREEN = (0, 255, 0)
        
        self.sc = pygame.display.set_mode((self.H, self.W))
        self.cloc = pygame.time.Clock()

        self.draw_menu()
        
    def draw_menu(self):
        font = pygame.font.Font(None, 36)
        menu_items = ["Play", "Quit"]
        selected_item = 0
        while True:
            self.sc.fill(self.color)
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        selected_item = (selected_item - 1) % len(menu_items)
                    elif event.key == pygame.K_DOWN:
                        selected_item = (selected_item + 1) % len(menu_items)
                    elif event.key == pygame.K_RETURN:
                        if selected_item == 0:
                            self.draw_game()
                        elif selected_item == 1:
                            pygame.quit()
                            sys.exit()
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()      
                    



                for i, item in enumerate(menu_items):
                    color = self.GREEN if i == selected_item  else self.color
                    text =  font.render(item, True, color)
                    self.sc.blit(text, (self.H // 2 - text.get_width() // 2, self.W // 2 + i * 50))
                pygame.display.flip()
                self.cloc.tick(self.FPS)



    def draw_game(self):
        si_green = True
        is_vg = False

        while True:
           
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()
            
             
            key = pygame.key.get_pressed()
            if key[pygame.K_LEFT] and self.x - self.radius > 0:
                self.x -= self.speed
            if key[pygame.K_DOWN] and self.y + self.radius < self.W:
                self.y += self.speed
            if key[pygame.K_UP] and self.y - self.radius > 0:
                self.y -= self.speed
            if key[pygame.K_RIGHT] and self.x + self.radius < self.H:
                self.x += self.speed
                

            if key[pygame.K_BACKSPACE]:
                self.x = self.H // 2 
                self.y = self.W // 2

            if key[pygame.K_1]:
                si_green = True

            if key[pygame.K_2]:
                si_green = False
            if key[pygame.K_3]:
                is_vg = True
                si_green = True
            if key[pygame.K_4]:
                is_vg = False
                
                

            if si_green:
                self.sc.fill(self.color)
                self.draw_players()
                
                
            if si_green == False:
                self.draw_p()
                is_vg = False

            elif is_vg:
                self.drow_player()
                
            elif is_vg == True:
                self.draw_players_S()
               
            n = Map()
            n.draw(self.sc, self.GREEN, self.radius) 
            
            

            pygame.display.update()
            self.cloc.tick(self.FPS)


    def drow_player(self):
        self.sc.fill("Black")
        pygame.draw.circle(self.sc, self.GREEN, (self.x, self.y), 13)
    
    def draw_p(self): 

        self.sc.fill(self.GREEN)
        pygame.draw.circle(self.sc, self.color, (self.x, self.y), 13)
        
        
        

    def draw_players(self):
        self.sc.fill(self.color)
        pygame.draw.circle(self.sc, self.GREEN, (self.x, self.y), 13)
        # pygame.display.flip()

    def draw_players_S(self):
        self.sc.fill("Blue")
        pygame.draw.circle(self.sc, self.GREEN, (self.x, self.y), 13)
        # pygame.display.flip()
    
    
    