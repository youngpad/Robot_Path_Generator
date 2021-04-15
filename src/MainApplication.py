import pygame
from DrawingScreen import DrawingScreen
from Button import Button

class MainApplication:

    def __init__(self):
        pygame.init()

        # Create main screen
        self.main_screen = pygame.display.set_mode((600,400))
        pygame.display.set_caption("Robot path generator")

        # Add drawing screen
        self.drawing_screen = DrawingScreen(self.main_screen)

        # Add buttons
        self.clear_button = Button("Clear", text_size=25, text_pos=(50,15), button_pos=(60, 325), button_size=(150, 50), button_color=(100, 100, 100), screen=self.main_screen)

    def main_loop(self):

        # Check actions
        isPressed = False
        while (True): 

            mouse_pos = pygame.mouse.get_pos()
            
            # check if mouse hovers over buttons
            if (self.clear_button.check_if_on(mouse_pos)):
                self.clear_button.hover(True)
            else:
                self.clear_button.hover(False)

            for event in pygame.event.get():

                # if window exit button is pressed, do this
                if event.type == pygame.QUIT:
                    pygame.quit()

                # if mouse button is pressed, do this
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    isPressed = True

                    if(self.clear_button.check_if_on(mouse_pos)):
                        self.drawing_screen.clear()

                # if mouse button is released, do this
                elif event.type == pygame.MOUSEBUTTONUP:
                    isPressed = False

                # if mouse button is pressed and mouse is moving, do this
                elif event.type == pygame.MOUSEMOTION and isPressed == True:
                    self.drawing_screen.when_drawn_on()

            # Draw objects on main screen
            self.drawing_screen.draw()
            self.clear_button.draw()

            # Update display
            pygame.display.update()