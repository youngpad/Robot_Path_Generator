import pygame

# init screen
screen = pygame.display.set_mode( (500, 500) )

isPressed = False
running = True
while (running):

    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            isPressed = True

        elif event.type == pygame.MOUSEBUTTONUP:
            isPressed = False
        
        elif event.type == pygame.MOUSEMOTION and isPressed == True:
            (x,y) = pygame.mouse.get_pos()
            pygame.draw.line(screen, (255,255,255), (x,y), (x,y))

    pygame.display.flip()