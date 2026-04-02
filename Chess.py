import pygame
from pygame.math import Vector2
from Piece_Moveset import *

#Pieces png is 1984x1984 

#black_square = (width/64, height/64)
#white_square = (width/64, height/64)

class GameState():
    def __init__(self):
        self.boardSize = 0
        self.board = []
        self.activeBlackPieces = []
        self.activeWhitePieces = []

    def update(self, piece, newPos):
        self.piece = piece
        self.newPos = newPos


class Chess():
    def __init__(self):
        pygame.init()

        self.gamestate = GameState()

        #Board
        cellSize = Vector2(64,64)

        #Pieces textures
        self.p = Pawn(10)

        self.width = 720
        self.height = 720
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.clock = pygame.time.Clock()
        self.running = True

    def processInput(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    self.running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                print("click")

    def update(self):
        self.gamestate.update(self.p, (0,0))

    def render(self):
        self.screen.fill((0,0,0))
    
        #Gets black pawn sprite

        self.rect, self.sprite = self.p.getSprite()
        self.s = pygame.image.load(self.sprite)
        self.s= pygame.transform.scale(self.s,(64,64))


        self.screen.blit(self.s, (0,0), self.rect)

        pygame.display.flip()
        pygame.display.update()
            

    def run(self):
        while self.running:
            self.processInput()
            self.update()
            self.render()
            self.clock.tick(60) #Limit to 60 fps



def Layer():
    def __init__(self, imageFile):
        self.imageFile = imageFile
    



#Take pos(x,y), x*width of the square, and y*height of square to get position of a piece






if __name__ == "__main__":
    game = Chess()
    game.run()
    pygame.quit()