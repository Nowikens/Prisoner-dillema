import pygame

pygame.init()
pygame.font.init()
window = pygame.display.set_mode((500, 200))


def table(window):
    window.fill((145, 254, 222))
    myfont = pygame.font.SysFont('Comic Sans MS', 30)
    textsurface = myfont.render('Some Text', False, (0, 0, 0))
    
    # horizontal lines
    pygame.draw.line(window, (0,0,0), (50,50), (450, 50), 1)
    pygame.draw.line(window, (0,0,0), (50,100), (450, 100), 1)
    pygame.draw.line(window, (0,0,0), (50,150), (450, 150), 1)
    
    # vertical lines 
    pygame.draw.line(window, (0,0,0), (100,25), (100, 175), 1)
    pygame.draw.line(window, (0,0,0), (200,25), (200, 175), 1)
    pygame.draw.line(window, (0,0,0), (300,25), (300, 175), 1)
    
    # players
    
    
    # blit
    window.blit(textsurface,(0,0))
    
while True:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        pygame.quit()
        

        pygame.display.set_caption('Prisoner Dillema')
        table(window)
        pygame.display.flip()
        
        
pygame.quit()

