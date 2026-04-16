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

            self.piecesOnBoard[6][i] = Pawn(Vector2(i,6), "White")

        self.piecesOnBoard[0][0] = Rook(Vector2(0,0), "Black")
        self.piecesOnBoard[0][1] = Knight(Vector2(1,0), "Black")
        self.piecesOnBoard[0][2] = Bishop(Vector2(2,0), "Black") 
        self.piecesOnBoard[0][3] = Queen(Vector2(3,0), "Black")
        self.piecesOnBoard[0][4] = King(Vector2(4,0), "Black")
        self.piecesOnBoard[0][5] = Bishop(Vector2(5,0), "Black")
        self.piecesOnBoard[0][6] = Knight(Vector2(6,0), "Black")
        self.piecesOnBoard[0][7] = Rook(Vector2(7,0), "Black")

        self.piecesOnBoard[7][0] = Rook(Vector2(0,7), "White")
        self.piecesOnBoard[7][1] = Knight(Vector2(1,7), "White")
        self.piecesOnBoard[7][2] = Bishop(Vector2(2,7), "White")
        self.piecesOnBoard[7][3] = King(Vector2(3,7), "White")
        self.piecesOnBoard[7][4] = Queen(Vector2(4,7),"White") 
        self.piecesOnBoard[7][5] = Bishop(Vector2(5,7), "White")
        self.piecesOnBoard[7][6] = Knight(Vector2(6,7), "White")
        self.piecesOnBoard[7][7] = Rook(Vector2(7,7),"White")


        #Currently active pieces (Not taken)
        self.activeBlackPieces = []
        self.activeWhitePieces = []

        
        for j in range(8):
            #Get pawns first
            self.activeBlackPieces.append(self.piecesOnBoard[1][j])
            self.activeBlackPieces.append(self.piecesOnBoard[0][j])

            self.activeWhitePieces.append(self.piecesOnBoard[6][j])
            self.activeWhitePieces.append(self.piecesOnBoard[7][j])

    def remove_active_piece(self, piece):
        if piece == 0:
            return

        if piece.color == "Black":
            if piece in self.activeBlackPieces:
                self.activeBlackPieces.remove(piece)
        elif piece.color == "White":
            if piece in self.activeWhitePieces:
                self.activeWhitePieces.remove(piece)


    def in_bounds(self, pos):
        return 0 <= int(pos.x) < 8 and 0 <= int(pos.y) < 8


    #Updates pieces on the board that were moved
    def update(self, piece, newPos):
        self.piece  = piece
        self.newPos = Vector2(int(newPos[0]), int(newPos[1]))

        oldPos = Vector2(int(self.piece.currPos.x), int(self.piece.currPos.y))
        oldRow = int(oldPos.y)
        oldCol = int(oldPos.x)
        newRow = int(self.newPos.y)
        newCol = int(self.newPos.x)

        if not self.in_bounds(self.newPos):
            return False

        if oldRow == newRow and oldCol == newCol:
            return False

        targetPiece = self.piecesOnBoard[newRow][newCol]
        if targetPiece != 0 and targetPiece.color == self.piece.color:
            return False

        if targetPiece != 0:
            self.remove_active_piece(targetPiece)

        self.piecesOnBoard[oldRow][oldCol] = 0
        self.piecesOnBoard[newRow][newCol] = self.piece
        self.piece.currPos = self.newPos

        return True

        


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
                self.mousePos  = pygame.mouse.get_pos()
                self.mousePos  = Vector2(self.mousePos[0], self.mousePos[1])
                self.mousePos = self.mousePos.elementwise()//64 #Caculates which square is selected
                    
                if self.isHoldingPiece and self.piece != 0:
                    moved = self.gamestate.update(self.piece, self.mousePos)
                    if moved:
                        self.piece = 0 
                        self.isHoldingPiece = False
                else:
                    if self.gamestate.piecesOnBoard[int(self.mousePos.y)][int(self.mousePos.x)] != 0: #Checks if selected square is occupied
                        self.isHoldingPiece = True
                        self.piece = self.gamestate.piecesOnBoard[int(self.mousePos.y)][int(self.mousePos.x)]
                
                self.mousePos = 0


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

class ChessEnv():

    def __init__(self, maxMoves = 300):
        self.maxMoves = maxMoves
        self.reset()

    def reset(self):
        self.gamestate = GameState()
        self.currentPlayer = "White"
        self.moveCount = 0
        self.done = False
        return self.observe()

    def step(self, action):
        if self.done:
            #Returns observatio, reward, done, and info
            return self.observe(), 0.0, True, {"reason" : "epidsode done"}
        
        legal = self.legal_actions()
        #Punish for bad behavior
        if action not in legal:
            self.done = True
            return self.observe(), -1.0, True, {"reason" : "Illegal move"}

        (from_x, from_y), (to_x, to_y) = action
        piece  = self.gamestate.piecesOnBoard[from_y][from_x]
        target = self.gamestate.piecesOnBoard[to_y][to_x]

        moved = self.gamestate.update(piece, target)
        self.moveCount += 1
    
    def legal_actions(self):
        actions = []
        for y in range(8):
            for x in range(8):
                piece = self.gamestate.piecesOnBoard[y][x]
                if piece == 0 or piece.color != self.currentPlayer:
                    continue
                for to_x, to_y in self.legal_targets(piece, x ,y):
                    actions.append(((x,y),(to_x,to_y)))
        return actions


    def observe(self):
        pass

