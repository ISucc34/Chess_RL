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

        #Chess board, no pieces
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

        #Initialize pieces

        #Location of the chess pieces
        self.piecesOnBoard = [
        [Rook(Vector2(0,0)),Knight(Vector2(1,0)),Bishop(Vector2(2,0)), Queen(Vector2(3,0)), King(Vector2(4,0)), Bishop(Vector2(5,0)),Knight(Vector2(6,0)),Rook(Vector2(7,0))],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [Rook(Vector2(7,7), "w"),Knight(Vector2(1,7), "w"),Bishop(Vector2(2,7), "w"), King(Vector2(3,7), "w"), Queen(Vector2(4,7), "w"), Bishop(Vector2(5,7), "w"),Knight(Vector2(6,7), "w"),Rook(Vector2(7,7), "w")]
        ]

        for i in range(8):
            self.piecesOnBoard[1][i] = Pawn(Vector2(1,i))
            self.piecesOnBoard[6][i] = Pawn(Vector2(6,i), "w")


        #Currently active pieces (Not taken)
        self.activeBlackPieces = []
        self.activeWhitePieces = []

        
        for j in range(8):
            #Get pawns first
            self.activeBlackPieces.append(self.piecesOnBoard[1][j])
            self.activeBlackPieces.append(self.piecesOnBoard[0][j])

            self.activeWhitePieces.append(self.piecesOnBoard[6][j])
            self.activeWhitePieces.append(self.piecesOnBoard[7][j])




    def update(self, piece, newPos):
        self.piece  = piece
        self.newPos = newPos
        self.piecesOnBoard[int(self.piece.currPos.x)][int(self.piece.currPos.y)] = 0

        self.piece.currPos = Vector2(newPos[0], newPos[1])

        self.piecesOnBoard[int(self.piece.currPos.x)][int(self.piece.currPos.y)] = self.piece

#Actual game logic
class Chess():
    def __init__(self):
        pygame.init()

        self.gamestate = GameState()

        #Size of a square
        self.cellSize = Vector2(64,64)

        #window and time initialization
        self.windowSize = self.gamestate.boardSize.elementwise()*self.cellSize
        self.screen     = pygame.display.set_mode((int(self.windowSize.x), int(self.windowSize.y)))
        self.clock      = pygame.time.Clock()
        self.running    = True

    #TODO: Process mouse input and click
    def processInput(self):
        #Quit input handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    self.running = False
            
            #Mouse input handling
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self.mousePos  = pygame.mouse.get_pos()
                self.mousePos  = Vector2(self.mousePos[0], self.mousePos[1])
                self.mousePos = self.mousePos.elementwise()//64
                if self.gamestate.piecesOnBoard[int(self.mousePos.y)][int(self.mousePos.x)] != 0:
                    #self.isHolding = True
                    self.piece = self.gamestate.piecesOnBoard[int(self.mousePos.y)][int(self.mousePos.x)]
            elif event.type == pygame.MOUSEBUTTONUP:
                self.mousePos  = pygame.mouse.get_pos()
                self.mousePos  = Vector2(self.mousePos[0], self.mousePos[1])
                self.mousePos = self.mousePos.elementwise()//64
                
                self.gamestate.update(self.piece, self.mousePos)
  


                print(self.mousePos)

    def update(self):
        pass

    def render(self):
        self.screen.fill((0,0,0))

        #renders the white squares
        for i in range(8):
            for j in range(8):
                self.scalar = self.gamestate.board[i][j]
                self.screen.fill((self.scalar*255, self.scalar*255, self.scalar*255), (i*self.cellSize.x, j*self.cellSize.y, self.cellSize.x, self.cellSize.y))
            
        
        #Renders pieces in first row
        for i in self.gamestate.activeBlackPieces:
            
            self.renderPiece = i

            
            #When a piece is moved, it is no longer in the first row, and since the loop only has the first row it cant render 0
            #Use the active pieces array to solve this issue
            self.rect, self.sprite = self.renderPiece.getSprite("t.png")
            self.s = pygame.image.load(self.sprite)
            self.s = pygame.transform.scale(self.s,(64,64))

            self.screen.blit(self.s, self.renderPiece.currPos.elementwise()*self.cellSize, self.rect)

        #Renders pieces in last row
        for i in self.gamestate.activeWhitePieces:
            
            self.renderPiece = i

            
            #When a piece is moved, it is no longer in the first row, and since the loop only has the first row it cant render 0
            #Use the active pieces array to solve this issue
            self.rect, self.sprite = self.renderPiece.getSprite("t.png")
            self.s = pygame.image.load(self.sprite)
            self.s = pygame.transform.scale(self.s,(64,64))

            self.screen.blit(self.s, self.renderPiece.currPos.elementwise()*self.cellSize, self.rect)


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
#Probably useless because only two layers: board and pieces
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