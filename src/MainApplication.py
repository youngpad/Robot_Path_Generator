# --- libraries ---
import pygame
import csv

# --- classes ---
from DrawingScreen import DrawingScreen
from Button import Button

class MainApplication:

    def __init__(self):

        # --- init pygame ---
        pygame.init()
        pygame.font.init()

        # --- create main screen ---
        self.main_screen = pygame.display.set_mode((600,400))
        self.main_screen.fill((255,255,255))
        pygame.display.set_caption("Robot path generator")

        # --- create drawing screen ---
        self.drawing_screen = DrawingScreen(self.main_screen)

        # --- create buttons ---
        self.clear_button = Button("Clear", text_size=25, button_pos=(60, 325), button_size=(150, 50), button_color=(100, 100, 100), screen=self.main_screen)
        self.save_button = Button("Save path", text_size=25, button_pos=(400, 325), button_size=(150, 50), button_color=(100, 100, 100), screen=self.main_screen)

    def run(self):

        # --- variables ---
        isPressed = False   

        # --- mainloop ---
        while (True): 

            mouse_pos = pygame.mouse.get_pos()

            # --- check button hovers ---
            if (self.clear_button.is_clicked(mouse_pos)):
                self.clear_button.hover(True)
            else:
                self.clear_button.hover(False)

            if (self.save_button.is_clicked(mouse_pos)):
                self.save_button.hover(True)
            else:
                self.save_button.hover(False)

            # --- events ---
            for event in pygame.event.get():

                # --- global events ---
                if (event.type == pygame.QUIT):
                    pygame.quit()

                elif (event.type == pygame.MOUSEBUTTONDOWN):
                    isPressed = True

                elif (event.type == pygame.MOUSEBUTTONUP):
                    isPressed = False

                # --- object events ---
                if ( (event.type == pygame.MOUSEMOTION) and (isPressed == True) ):
                    self.drawing_screen.when_drawn_on()
                
                if( (self.clear_button.is_clicked(mouse_pos)) and (event.type == pygame.MOUSEBUTTONDOWN) ):
                        self.drawing_screen.clear()

                if( (self.save_button.is_clicked(mouse_pos)) and (event.type == pygame.MOUSEBUTTONDOWN) ):
                        self.save_path(self.drawing_screen.get_path_coordinates())

            # --- draw ---
            self.drawing_screen.draw()
            self.clear_button.draw()
            self.save_button.draw()

            # --- update display ---
            pygame.display.update()
    
    def save_path(self, path_coordinates):

        # --- write file ---
        with open("./tmp/path.txt", "w+") as path_file:
            
            # --- create writer ---
            path_writer = csv.writer(path_file)

            # --- write x and y coordinates ---
            path_writer.writerow(path_coordinates[0])
            path_writer.writerow(path_coordinates[1])

        print("Path file saved")