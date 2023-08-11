import pygame

#pygame.init()

FPS = 60
WIDTH, HEIGHT = 720, 620
WHITE = (255,255,255)


SCREEN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Tic Tac Toe")


def draw_window():
    SCREEN.fill(WHITE)
    pygame.display.update()  

def main():
    clock = pygame.time.Clock()
    run = True
    
    while(run):
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                
        draw_window()     
    pygame.quit()
    
if __name__ == "__main__":
    main()