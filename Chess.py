import pygame
from Piece_Moveset import *

class Chess():
    def __init__(self):
        pygame.init()
        
        self.width = 720
        self.height = 720
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.clock = pygame.time.Clock()
        self.running = True

        def processInput(self):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        self.running = False

        def update(self):
            pass

        def render(self):
            self.screen.fill((0,0,0))
            pygame.display.flip()
            

        def run(self):
            while self.running:
                self.processInput()
                self.update()
                self.render()
                self.clock.tick(60) #Limit to 60 fps



def Layer():
    def __init__(self, imageFile):
        self.imageFile = imageFile
    


def main():

    
    # pygame setup



    running = True

    background = pygame.image.load("sprites/chessboard.png").convert()
    background = pygame.transform.scale(background, (width, height))

    #Take pos(x,y), x*width of the square, and y*height of square to get position of a piece

    black_square = (width/64, height/64)
    white_square = (width/64, height/64)

    board = [[Rook((0,0)), 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [Pawn(), 0, 0, 0, 0, 0, 0]]



    pygame.quit()

if __name__ == "__main__":
    main()