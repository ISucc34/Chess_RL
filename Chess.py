import pygame
import math
from pygame.math import Vector2
from Piece_Moveset import *

#Pieces png is 1984x1984 

#black_square = (width/64, height/64)
#white_square = (width/64, height/64)


#Gamestate controls what state the game is in for ex: where every piece is
class GameState():
    def __init__(self):
        #Sets up the board
        self.boardSize = Vector2(8, 8)
        self.board = [
        [0,1,0,1,0,1,0,1],
        [1,0,1,0,1,0,1,0],
        [0,1,0,1,0,1,0,1],
        [1,0,1,0,1,0,1,0],
        [0,1,0,1,0,1,0,1],
        [1,0,1,0,1,0,1,0],
        [0,1,0,1,0,1,0,1],
        [1,0,1,0,1,0,1,0],
        ]

        self.piecesOnBoard = [
        [Rook(Vector2(0,0)),Knight(Vector2(1,0)),Bishop(Vector2(2,0)), Queen(Vector2(3,0)), King(Vector2(4,0)), Bishop(Vector2(5,0)),Knight(Vector2(6,0)),Rook(Vector2(7,0))],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [Rook(Vector2(7,7)),Knight(Vector2(1,7)),Bishop(Vector2(2,7)), King(Vector2(3,7)), Queen(Vector2(4,7)), Bishop(Vector2(5,7)),Knight(Vector2(6,7)),Rook(Vector2(7,7))]
        ]

        self.activeBlackPieces = []
        self.activeWhitePieces = []

    def update(self, piece, newPos):
        self.piece  = piece
        self.newPos = newPos

#Actual game logic
class Chess():
    def __init__(self):
        pygame.init()

        self.gamestate = GameState()

        #Board
        self.cellSize = Vector2(64,64)


        self.WhiteRect = (0,0, self.cellSize.x, self.cellSize.y)

        #Pieces textures
        self.p = Pawn(Vector2(0,0))

        self.windowSize = self.gamestate.boardSize.elementwise()*self.cellSize
        self.screen     = pygame.display.set_mode((int(self.windowSize.x), int(self.windowSize.y)))
        self.clock      = pygame.time.Clock()
        self.running    = True

    #TODO: Process mouse input and click
    def processInput(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    self.running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self.mousePos  = pygame.mouse.get_pos()
                self.mousePos  = Vector2(self.mousePos[0], self.mousePos[1])
                
                self.mousePos = self.mousePos.elementwise()//64

                if self.gamestate.piecesOnBoard[int(self.mousePos.y)][int(self.mousePos.x)] != 0:
                    print("Occupied")

                print(self.mousePos)

    def update(self):
        self.gamestate.update(self.p, (0,0))

    def render(self):
        self.screen.fill((0,0,0))

        #renders the white squares
        for i in range(8):
            for j in range(8):
                self.scalar = self.gamestate.board[i][j]
                self.screen.fill((self.scalar*255, self.scalar*255, self.scalar*255), (i*self.cellSize.x, j*self.cellSize.y, self.cellSize.x, self.cellSize.y))
            
        #Shows black pawn sprite
        self.rect, self.sprite = self.p.getSprite("t.png")

        self.s = pygame.image.load(self.sprite)
        self.s = pygame.transform.scale(self.s,(64,64))

        for i in range(0,8):
            self.piece = self.gamestate.piecesOnBoard[0][i]

            self.rect, self.sprite = self.piece.getSprite("t.png")
            self.s = pygame.image.load(self.sprite)
            self.s = pygame.transform.scale(self.s,(64,64))

            self.screen.blit(self.s, self.piece.currPos.elementwise()*self.cellSize, self.rect)
        for i in range(8):
            self.piece = self.gamestate.piecesOnBoard[7][i]

            self.rect, self.sprite = self.piece.getSprite("t.png")
            self.s = pygame.image.load(self.sprite)
            self.s = pygame.transform.scale(self.s,(64,64))

            self.screen.blit(self.s, self.piece.currPos.elementwise()*self.cellSize, self.rect)


        pygame.display.flip()
        pygame.display.update()
            
    #Game loop
    def run(self):
        while self.running:
            self.processInput()
            self.update()
            self.render()
            self.clock.tick(60) #Limit to 60 fps


#TODO: Implement layers 1st layer is the board, second layer are the piece sprites
class Layer():
    def __init__(self, ui, imageFile):
        self.ui = ui
        self.texture = pygame.image.load(imageFile)
    def renderTile(self, window, pos, tile):
        spritePos = pos.elementwise()*self.ui.cellSize
        
        
        texturePos  = tile.elementwise()*self.ui.cellsize
        textureRect = pygame.Rect(int(texturePos.x), int(texturePos.y), self.ui.cellWidth, self.ui.cellHeight)



#Take pos(x,y), x*width of the square, and y*height of square to get position of a piece





#Good naming convention on triple T sahur
if __name__ == "__main__":
    game = Chess()
    game.run()
    pygame.quit()