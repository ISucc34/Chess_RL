import pygame
import numpy as np


#Maybe use a dictionary, where the key is the position, and value as the piece that lives there?

#Abstract Class template
class Piece():
    def __init__(self, currPos, color):
        self.currPos = currPos #Pos in terms of array index
        self.value = 0
        self.color = color
    def update(self, newPos):
        self.currPos = newPos
    def getSprite(self):
        self.rect = (0,0,64,64)
        self.sprite
        #self.temp = pygame.image.load(self.sprite)
        return self.rect, self.sprite
  

class Pawn(Piece):
    def __init__(self, currPos, color):
        super().__init__(currPos = currPos, color= color)
        self.value = 1
        self.color = color
        self.sprite = pygame.image.load(f"sprites/{color}Pawn.png")
        self.firstMove = True #Implement two space movement later

    def validMoves(self, piecesOnBoard):
        moves = []
        
        if self.color == "White":
            moves.append(pygame.Vector2(self.currPos.x, self.currPos.y-1))
        elif self.color == 'Black':
            moves.append(pygame.Vector2(self.currPos.x, self.currPos.y+1))

        return moves

  
        
class Rook(Piece):
    def __init__(self, currPos, color):
        super().__init__(currPos = currPos, color = color)
        self.value = 5
        self.color = color
        self.sprite = pygame.image.load(f"sprites/{color}Rook.png")
        
    def validMoves(self, piecesOnBoard):
        moves = []

        left  = int(self.currPos.x) +1
        

        right = 8 - int(self.currPos.x)
        print(right)

        above = int(self.currPos.y) + 1

        below = 8 - int(self.currPos.y)

        for i in range(left):
            if piecesOnBoard[int(self.currPos.y)][int(self.currPos.x - i)] == 0:
                moves.append(pygame.Vector2(self.currPos.x - i, self.currPos.y))
            elif piecesOnBoard[int(self.currPos.y)][int(self.currPos.x - i)].color != self.color:
                moves.append(pygame.Vector2(self.currPos.x - i, self.currPos.y))
                break
        
        for i in range(right):
            if piecesOnBoard[int(self.currPos.y)][int(self.currPos.x + i)] == 0:
                moves.append(pygame.Vector2(self.currPos.x + i, self.currPos.y))
            elif piecesOnBoard[int(self.currPos.y)][int(self.currPos.x + i)].color != self.color:
                moves.append(pygame.Vector2(self.currPos.x + i, self.currPos.y))
                break

        for i in range(above):
            if piecesOnBoard[int(self.currPos.y - i)][int(self.currPos.x)] == 0:
                moves.append(pygame.Vector2(self.currPos.x, self.currPos.y - i))
            elif piecesOnBoard[int(self.currPos.y - i)][int(self.currPos.x)].color != self.color:
                print(piecesOnBoard[int(self.currPos.y - i)][int(self.currPos.x)].color)
                moves.append(pygame.Vector2(self.currPos.x, self.currPos.y - i))
                break
        
        

        print(moves)
        
            


        return moves
       


        
class Bishop(Piece):
    def __init__(self, currPos, color):
        super().__init__(currPos = currPos, color= color)
        self.value = 3
        self.color = color
        self.sprite = pygame.image.load(f"sprites/{color}Bishop.png")
    def validateMove(self, newPos):
        pass

class Knight(Piece):
    def __init__(self, currPos, color):
        super().__init__(currPos = currPos, color= color)
        self.value = 3
        self.color = color
        self.sprite = pygame.image.load(f"sprites/{color}Knight.png")
        
    def move(pos):
        pos



class Queen(Piece):
    def __init__(self, currPos, color):
        super().__init__(currPos = currPos, color= color)
        self.value = 9
        self.color = color
        self.sprite = pygame.image.load(f"sprites/{color}Queen.png")
    def move(pos):
        pos


class King(Piece):
    def __init__(self, currPos, color):
        super().__init__(currPos = currPos, color = color)
        self.value = 0
        self.color = color
        self.sprite = pygame.image.load(f"sprites/{color}King.png")

    def validateMove(self, newPos):
        pass
        