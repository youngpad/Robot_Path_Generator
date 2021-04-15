import pygame

class DrawingScreen:

    def __init__(self, main_screen):
        self.main_screen = main_screen

        # create screen
        self.screen = pygame.Surface((600,300))
        self.screen.fill((255,255,255))
        
    # draw screen on given screen
    def draw(self):
        pygame.Surface.blit(self.main_screen, self.screen, (0, 0))

    def when_drawn_on(self):
        point_width = 5
        (x,y) = pygame.mouse.get_pos()
        pygame.draw.circle(self.screen, (0,0,0), (x,y), point_width)

    def clear(self):
        self.screen.fill((255,255,255))