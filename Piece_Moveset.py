from Chess import *
import pygame

#Abstract Class template
class Piece():
    def __init__(self, currPos):
        self.currPos = currPos
        self.value = 0
    def update(self, newPos):
        self.currPos = newPos
    def getSprite(self, img):
        self.rect = (0,0,64,64)
        self.sprite = img
        return self.rect, self.sprite

class Pawn(Piece):
    def __init__(self, currPos):
        super().__init__(currPos = currPos)
        self.value = 1
        
class Rook(Piece):
    def __init__(self, currPos):
        super().__init__(currPos)
        self.value = 5
    def move(currPos, newPos):
        pass
        
class Bishop(Piece):
    def __init__(self, pos):
        super().__init__(pos)
        self.value = 3
    def move(pos):
        pos

class Knight(Piece):
    def __init__(self, pos):
            super().__init__(pos)
            self.value = 3
    def move(pos):
        pos



class Queen(Piece):
    def __init__(self, pos):
        super().__init__(pos)
        self.value = 9
    def move(pos):
        pos


class King(Piece):
    def __init__(self, pos):
        super().__init__(pos)
        self.value = 0
    def move(pos):
        pos