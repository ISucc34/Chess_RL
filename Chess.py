import pygame
from Piece_Moveset import *

def main():
    # pygame setup
    pygame.init()

    width = 720
    height = 720

    screen = pygame.display.set_mode((width, height))
    clock = pygame.time.Clock()
    running = True

    black_square = (width/8, width/8)

    pieces = {"Pawn": 1,
              "Rook": 2 }
    

    board = [[],
             [],
             [],
             [],
             [],
             [],
             [],
             []]

    while running:
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    running = False
        
        
            

        screen.fill("white")




        # flip() the display to put your work on screen
        pygame.display.flip()

        clock.tick(60)  # limits FPS to 60

    pygame.quit()

if __name__ == "__main__":
    main()