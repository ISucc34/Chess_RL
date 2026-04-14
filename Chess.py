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
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0]
        ]

        #Set up pawns
        for i in range(8):
            self.piecesOnBoard[1][i] = Pawn(Vector2(i,1), "Black")
            self.piecesOnBoard[0][i] = Rook(Vector2(0,0), "Black")
            self.piecesOnBoard[0][i] = Knight(Vector2(1,0), "Black")
            self.piecesOnBoard[0][i] = Bishop(Vector2(2,0), "Black") 
            self.piecesOnBoard[0][i] = Queen(Vector2(3,0), "Black")
            self.piecesOnBoard[0][i] = King(Vector2(4,0), "Black")
            self.piecesOnBoard[0][i] = Bishop(Vector2(5,0), "Black")
            self.piecesOnBoard[0][i] = Knight(Vector2(6,0), "Black")
            self.piecesOnBoard[0][i] = Rook(Vector2(7,0), "Black")


            self.piecesOnBoard[6][i] = Pawn(Vector2(i,6), "White")
            self.piecesOnBoard[7][i] = Rook(Vector2(i,7), "White")
            self.piecesOnBoard[7][i] = Knight(Vector2(i,7), "White")
            self.piecesOnBoard[7][i] = Bishop(Vector2(i,7), "White")
            self.piecesOnBoard[7][i] = King(Vector2(i,7), "White")
            self.piecesOnBoard[7][i] = Queen(Vector2(i,7),"White") 
            self.piecesOnBoard[7][i] = Bishop(Vector2(i,7), "White")
            self.piecesOnBoard[7][i] = Knight(Vector2(i,7), "White")
            self.piecesOnBoard[7][i] = Rook(Vector2(i,7),"White")


        #Currently active pieces (Not taken)
        self.activeBlackPieces = []
        self.activeWhitePieces = []

        
        for j in range(8):
            #Get pawns first
            self.activeBlackPieces.append(self.piecesOnBoard[1][j])
            self.activeBlackPieces.append(self.piecesOnBoard[0][j])

            self.activeWhitePieces.append(self.piecesOnBoard[6][j])
            self.activeWhitePieces.append(self.piecesOnBoard[7][j])


    #Updates pieces on the board that were moved
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

        self.isHoldingPiece = False #Is a piece selected
        self.piece          = 0 #Current piece the player is holding

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
                if self.isHoldingPiece:
                    if self.piece != 0:
                        self.mousePos  = pygame.mouse.get_pos()
                        self.mousePos  = Vector2(self.mousePos[0], self.mousePos[1])
                        self.mousePos = self.mousePos.elementwise()//64
                        
                        self.gamestate.update(self.piece, self.mousePos)
                        self.piece = 0 
                        self.isHoldingPiece = False
                else:
                    self.mousePos  = pygame.mouse.get_pos()
                    self.mousePos  = Vector2(self.mousePos[0], self.mousePos[1])
                    self.mousePos = self.mousePos.elementwise()//64 #Caculates which square is selected
                    if self.gamestate.piecesOnBoard[int(self.mousePos.y)][int(self.mousePos.x)] != 0: #Checks if selected square is occupied
                        self.isHoldingPiece = True
                        self.piece = self.gamestate.piecesOnBoard[int(self.mousePos.y)][int(self.mousePos.x)]


        
            """if event.type == pygame.MOUSEBUTTONUP and self.isHoldingPiece:
                if self.piece != 0:
                    self.mousePos  = pygame.mouse.get_pos()
                    self.mousePos  = Vector2(self.mousePos[0], self.mousePos[1])
                    self.mousePos = self.mousePos.elementwise()//64
                    
                    self.gamestate.update(self.piece, self.mousePos)
                    self.piece = 0 
                    self.isHoldingPiece = False"""
    

    def update(self):
        pass

    def render(self):
        self.screen.fill((0,0,0))

        #renders the white squares
        for i in range(8):
            for j in range(8):
                self.scalar = self.gamestate.board[i][j]
                self.screen.fill((self.scalar*200, self.scalar*200, self.scalar*200), (i*self.cellSize.x, j*self.cellSize.y, self.cellSize.x, self.cellSize.y))
            
        
        #Renders active black pieces 
        for i in self.gamestate.activeBlackPieces:
            
            self.renderPiece = i

            #When a piece is moved, it is no longer in the first row, and since the loop only has the first row it cant render 0
            #Use the active pieces array to solve this issue
            self.rect, self.sprite = self.renderPiece.getSprite()
            self.s = self.sprite
            self.s = pygame.transform.scale(self.s,(64,64))

            self.screen.blit(self.s, self.renderPiece.currPos.elementwise()*self.cellSize, self.rect)

        #Renders active white pieces
        for i in self.gamestate.activeWhitePieces:
            
            self.renderPiece = i

            self.rect, self.sprite = self.renderPiece.getSprite()
            self.s = self.sprite
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

