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

    background = pygame.image.load("sprites/chessboard.png").convert()
    background = pygame.transform.scale(background, (width, height))

    pieces = {"Pawn": 1,
              "Rook": 2 }
    

    board = [[Rook((0,0)), 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [Pawn(), 0, 0, 0, 0, 0, 0]]

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
        screen.blit(background, (0,0))


        # flip() the display to put your work on screen
        pygame.display.flip()

        clock.tick(60)  # limits FPS to 60

    pygame.quit()

if __name__ == "__main__":
    main()