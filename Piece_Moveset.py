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
    def getSprite(self, img):
        self.rect = (0,0,64,64)
        self.sprite = img
        return self.rect, self.sprite
  

class Pawn(Piece):
    def __init__(self, currPos, color = "b"):
        super().__init__(currPos = currPos, color=color)
        self.value = 1
        if self.color == "w":
            pass #Use the white sprite if not use the black one
    def moveSet(self, newpos):
        self.currPos = newpos
        self.currPos[1] += 1 #move up the column
    def setPos(self, newPos):
        self.currPos = newPos
    def getPos(self):
        return self.currPos
        
class Rook(Piece):
    def __init__(self, currPos, color = "b"):
        super().__init__(currPos = currPos, color=color)
        self.value = 5
        if self.color == "w":
            pass #Use the white sprite if not use the black one
    def moveSet(self, currPos):
        pass
        
class Bishop(Piece):
    def __init__(self, currPos, color = "b"):
        super().__init__(currPos = currPos, color=color)
        self.value = 3
        if self.color == "w":
            pass #Use the white sprite if not use the black one
    def move(pos):
        pos

class Knight(Piece):
    def __init__(self, currPos, color = "b"):
        super().__init__(currPos = currPos, color=color)
        self.value = 3
        if self.color == "w":
            pass #Use the white sprite if not use the black one
    def move(pos):
        pos



class Queen(Piece):
    def __init__(self, currPos, color = "b"):
        super().__init__(currPos = currPos, color=color)
        self.value = 9
        if self.color == "w":
            pass #Use the white sprite if not use the black one
    def move(pos):
        pos


class King(Piece):
    def __init__(self, currPos, color = "b"):
        super().__init__(currPos = currPos, color=color)
        self.value = 0
        if self.color == "w":
            pass #Use the white sprite if not use the black one
    def move(pos):
        pos