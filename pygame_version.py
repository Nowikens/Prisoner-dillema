import pygame

pygame.init()
pygame.font.init()
window = pygame.display.set_mode((500, 200))


def table(window):
    # color
    window.fill((145, 254, 222))
    # 1.name of font 2.height
    myfont = pygame.font.SysFont('Comic Sans MS', 12)
    # 1.what text 2.? 3.color
    player1_text = myfont.render('Player 1 /n nstrategy', False, (0, 0, 0))
    player2_text = myfont.render('Player 2 /n nstrategy', False, (0, 0, 0))
    
    # horizontal lines 1.where(surface) 2.color 3.start-pos 4.end-pos 5.width
    pygame.draw.line(window, (0,0,0), (50,50), (450, 50), 1)
    pygame.draw.line(window, (0,0,0), (50,100), (450, 100), 1)
    pygame.draw.line(window, (0,0,0), (50,150), (450, 150), 1)
    
    # vertical lines 
    pygame.draw.line(window, (0,0,0), (100,25), (100, 175), 1)
    pygame.draw.line(window, (0,0,0), (200,25), (200, 175), 1)
    pygame.draw.line(window, (0,0,0), (300,25), (300, 175), 1)
    
    # players
    
    
    # blitting surface, 1.what surface 2.new position
    window.blit(player1_text,(50,60))
    window.blit(player2_text,(50,110))
    
while True:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        pygame.quit()
        

        pygame.display.set_caption('Prisoner Dillema')
        table(window)
        pygame.display.flip()
        
        
pygame.quit()

