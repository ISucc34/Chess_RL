from Chess import *
import pygame

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
        self.sprite = 0
        self.temp = pygame.image.load(self.sprite)
        return self.rect, self.temp
  

class Pawn(Piece):
    def __init__(self, currPos, color):
        super().__init__(currPos = currPos, color= color)
        self.value = 1
        if self.color == "w":
            self.sprite = "sprites/WhitePawn.png"
        else: 
            self.sprite = "sprites/BlackPawn.png"
    def moveSet(self, newpos):
        self.currPos = newpos
        self.currPos[1] += 1 #move up the column
    def setPos(self, newPos):
        self.currPos = newPos
    def getPos(self):
        return self.currPos
        
class Rook(Piece):
    def __init__(self, currPos, color):
        super().__init__(currPos = currPos, color = color)
        self.value = 5
        if self.color == "w":
            self.sprite = "sprites/WhiteRook.png"
        else: 
            self.sprite = "sprites/BlackRook.png"
    def moveSet(self, currPos):
        pass
        
class Bishop(Piece):
    def __init__(self, currPos, color):
        super().__init__(currPos = currPos, color= color)
        self.value = 3
        if self.color == "w":
            self.sprite = "sprites/WhiteBishop.png"
        else: 
            self.sprite = "sprites/BlackBishop.png"
    def move(pos):
        pos

class Knight(Piece):
    def __init__(self, currPos, color):
        super().__init__(currPos = currPos, color= color)
        self.value = 3
        if self.color == "w":
            self.sprite = "sprites/WhiteKnight.png"
        else: 
            self.sprite = "sprites/BlackKnight.png"
    def move(pos):
        pos



class Queen(Piece):
    def __init__(self, currPos, color):
        super().__init__(currPos = currPos, color= color)
        self.value = 9
        if self.color == "w":
            self.sprite = "sprites/WhiteQueen.png"
        else: 
            self.sprite = "sprites/BlackQueen.png"
    def move(pos):
        pos


class King(Piece):
    def __init__(self, currPos, color):
        super().__init__(currPos = currPos, color = color)
        self.value = 0
        if self.color == "w":
            self.sprite = "sprites/WhiteKing.png"
        else: 
            self.sprite = "sprites/BlackKing.png"
    def move(pos):
        pos