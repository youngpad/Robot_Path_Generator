import pygame

class DrawingScreen:

    def __init__(self, main_screen):

        self.main_screen = main_screen
        
        self.path_coordinates = [[],[]]

        # --- create screen ---
        self.x = 600
        self.y = 300
        self.screen = pygame.Surface((self.x, self.y))
        self.screen.fill((255,255,255))
        
    # draw screen on given screen
    def draw(self):
        
        pygame.Surface.blit(self.main_screen, self.screen, (0, 0))

    def when_drawn_on(self):
        
        point_width = 5
        scale = 300

        # --- draw circle at mouse pos ---
        (x,y) = pygame.mouse.get_pos()
        pygame.draw.circle(self.screen, (0,0,0), (x,y), point_width)
        
        # --- append coordinates to array ---
        self.path_coordinates[0].append(x/scale + 0.4)
        self.path_coordinates[1].append(self.y/scale - y/scale + 1)

    def clear(self):
        self.screen.fill((255,255,255))
        self.path_coordinates = [[], []]

    def get_path_coordinates(self):
        return self.path_coordinates
