import pygame
from pygame.locals import *
pygame.init()
mainClock = pygame.time.Clock()

pygame.display.set_caption("Prisoner Dilemma")
screen = pygame.display.set_mode((1000, 700))

font = pygame.font.SysFont(None, 20)
font2 = pygame.font.SysFont(None, 50)


def draw_wraped_text(text, font, color, surface, rect, aa=False, bkg=None):
        rect = pygame.Rect(rect)
        x = rect.left
        y = rect.top
        lineSpacing = -2

        fontHeight = font.size("Tg")[1]
        while text:
                i = 1
                if y + fontHeight > rect.bottom:
                        break
                while font.size(text[:i])[0] < rect.width and i < len(text):
                        i += 1

                if i < len(text):
                        i = text.rfind(" ", 0, i) + 1

                if bkg:
                        image = font.render(text[:i], 1, color, bkg)
                        image.set_colorkey(bkg)
                else:
                        image = font.render(text[:i], aa, color)
                surface.blit(image, (x, y))
                y += fontHeight + lineSpacing
                text = text[i:]
        return text

        
def draw_text(text, font, color, surface, x, y):
        textobj = font.render(text, 1, color)
        textrect = textobj.get_rect()
        textrect.topleft = (x, y)
        surface.blit(textobj, textrect)
                

info = "Hello there, You're in jail. We have your partner. This jail makes no sense so instead of years in prison, you gain points. That's right, points. If you two bastards cooperate, you both get 3 points. If you defect and your partner cooperates you get 5 points, and he gets 0, if he defects while you cooperate, you get 0 and he gets 5. If you both defect, you will both get 1 point."


click = False

def main_menu():
        while True:

                screen.fill((0,0,0))
                draw_wraped_text(info, font2, (255, 255, 255), screen, (40, 20, 800, 500))

                mx, my = pygame.mouse.get_pos()
        

                button_0 = pygame.Rect(400, 600, 200, 50)
                if button_0.collidepoint((mx, my)):
                        if click:
                                game()
                pygame.draw.rect(screen, (255, 0, 0), button_0)
                draw_text("Continue",
                          font, (0, 0, 0), screen, 420, 615)
                 
                

                click = False

                for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                                pygame.quit()
                        if event.type == KEYDOWN:
                                if event.key == K_ESCAPE:
                                        pygame.quit()
                        if event.type == MOUSEBUTTONDOWN:
                                if event.button == 1:
                                        click = True
                pygame.display.update()
                mainClock.tick(60)

def game(): 
        running = True
        while running:
                click = False
                screen.fill((0, 0, 0))
                draw_text("NOW CHOOSE ONE OF THE STRATEGIES BELOW.",
                        font, (255, 255, 255), screen, 40, 20)
                draw_text("Player One",
                        font, (255, 255, 255), screen, 40, 100)
                draw_text("Player Two",
                        font, (255, 255, 255), screen, 540, 100)


                
                mx, my = pygame.mouse.get_pos()
        
                button_1 = pygame.Rect(20, 150, 200, 50)
                if button_1.collidepoint((mx, my)):
                        if click:
                                pass
                pygame.draw.rect(screen, (255, 0, 0), button_1)
                button_2 = pygame.Rect(20, 225, 200, 50)
                if button_2.collidepoint((mx, my)):
                        if click:
                                pass
                pygame.draw.rect(screen, (255, 0, 0), button_2)
                button_3 = pygame.Rect(20, 300, 200, 50)
                if button_3.collidepoint((mx, my)):
                        if click:
                                pass
                pygame.draw.rect(screen, (255, 0, 0), button_3)
                button_4 = pygame.Rect(20, 375, 200, 50)
                if button_4.collidepoint((mx, my)):
                        if click:
                                pass
                pygame.draw.rect(screen, (255, 0, 0), button_4)
                button_5 = pygame.Rect(520, 150, 200, 50)
                if button_5.collidepoint((mx, my)):
                        if click:
                                pass
                pygame.draw.rect(screen, (255, 0, 0), button_5)
                button_6 = pygame.Rect(520, 225, 200, 50)
                if button_6.collidepoint((mx, my)):
                        if click:
                                pass
                pygame.draw.rect(screen, (255, 0, 0), button_6)
                button_7 = pygame.Rect(520, 300, 200, 50)
                if button_7.collidepoint((mx, my)):
                        if click:
                                pass
                pygame.draw.rect(screen, (255, 0, 0), button_7)
                button_8 = pygame.Rect(520, 375, 200, 50)
                if button_8.collidepoint((mx, my)):
                        if click:
                                pass
                pygame.draw.rect(screen, (255, 0, 0), button_8)


                draw_text("Always Cooperate",
                          font, (0, 0, 0), screen, 40, 165)
                draw_text("Always Defect",
                          font, (0, 0, 0), screen, 40, 240)
                draw_text("Tit for Tat",
                          font, (0, 0, 0), screen, 40, 315)
                draw_text("Random",
                          font, (0, 0, 0), screen, 40, 390)
                draw_text("Always Cooperate",
                          font, (0, 0, 0), screen, 540, 165)
                draw_text("Always Defect",
                          font, (0, 0, 0), screen, 540, 240)
                draw_text("Tit for Tat",
                          font, (0, 0, 0), screen, 540, 315)
                draw_text("Random",
                          font, (0, 0, 0), screen, 540, 390)


                button_9 = pygame.Rect(400, 600, 200, 50)
                if button_9.collidepoint((mx, my)):
                        if click:
                                pass
                pygame.draw.rect(screen, (255, 0, 0), button_9)
                draw_text("Continue",
                          font, (0, 0, 0), screen, 420, 615)
        

                                 
                
                 
                
                for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                                pygame.quit()
                        if event.type == KEYDOWN:
                                if event.key == K_ESCAPE:
                                        running = False
                                        pygame.quit()
                        if event.type == MOUSEBUTTONDOWN:
                                if event.button == 1:
                                        click = True
                pygame.display.update()
                mainClock.tick(60)

             
main_menu()





















