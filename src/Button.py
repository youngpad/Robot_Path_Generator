import pygame

# Generic button class
class Button:

    def __init__(self, text, text_size, text_pos, button_size, button_pos, button_color, screen):
        self.text = text # text on button
        self.text_size = text_size # text size
        self.text_pos = text_pos # text position with respect to button
        self.button_size = button_size  # button size
        self.button_pos = button_pos  # button position
        self.button_color = button_color # button color
        self.button_original_color = button_color
        self.screen = screen # screen to draw button onto

    def draw(self):
        # draw button
        pygame.draw.rect(self.screen, self.button_color, pygame.Rect(*self.button_pos, *self.button_size))

        # draw text
        text = pygame.font.SysFont('Corbel', self.text_size).render(self.text, True, (255,255,255))
        self.screen.blit(text, (self.button_pos[0]+self.text_pos[0], self.button_pos[1]+self.text_pos[1]))

    # method that checks if mouse is clicked on button 
    def check_if_on(self, mouse_pos):
        if ( (mouse_pos[0] >= self.button_pos[0] and mouse_pos[0] <= self.button_pos[0]+self.button_size[0]) and (mouse_pos[1] >= self.button_pos[1] and mouse_pos[1] <= self.button_pos[1]+self.button_size[1]) ):
            return True
        else:
            return False
    
    def hover(self, is_mouse_on):
        if (is_mouse_on):
            self.button_color = (50,50,50)
        else:
            self.button_color = self.button_original_color