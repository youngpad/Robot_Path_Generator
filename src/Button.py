import pygame 

class Button:

    def __init__(self, text, text_size, button_size, button_pos, button_color, screen):

        self.text = text # text on button
        self.text_size = text_size # text size

        self.button_size = button_size  # button size
        self.button_pos = button_pos  # button position
        self.button_color = button_color # button color
        self.button_original_color = button_color
        
        self.screen = screen # screen to draw button onto

    def draw(self):
       
        # draw button
        pygame.draw.rect(self.screen, self.button_color, pygame.Rect(*self.button_pos, *self.button_size))

        # draw text 
        text = pygame.font.SysFont('Corbel', self.text_size).render(self.text, True, (255,255,255)) # create text 
        text_width, text_heigth = text.get_width(), text.get_height() # get text width and height to calculate how to center text on button
        self.screen.blit(text, (self.button_pos[0]+((self.button_size[0]-text_width)/2), self.button_pos[1]+((self.button_size[1]-text_heigth)/2))) # blit text to screen

    def is_clicked(self, mouse_pos):
        
        if ( ( (mouse_pos[0] >= self.button_pos[0]) and (mouse_pos[0] <= self.button_pos[0]+self.button_size[0]) ) and ( (mouse_pos[1] >= self.button_pos[1]) and (mouse_pos[1] <= self.button_pos[1]+self.button_size[1]) ) ):
            return True
        else:
            return False
    
    def hover(self, is_mouse_on):
       
        if (is_mouse_on):
            self.button_color = (50,50,50)
        else:
            self.button_color = self.button_original_color