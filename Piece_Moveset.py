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
        
class Rook():
    def __init__(self, currPos):
        self.currPos = currPos
        self.value = 9
    def move(currPos, newPos):
        pass
        
class Bishop():
    def __init__(self, pos):
        self.pos = pos
        self.value = 9
    def move(pos):
        pos

class Knight():
    def __init__(self, pos):
        self.pos = pos
        self.value = 9
    def move(pos):
        pos



class Queen():
    def __init__(self, pos):
        self.pos = pos
        self.value = 9
    def move(pos):
        pos


class King():
    def __init__(self, pos):
        self.pos = pos
        self.value = 9
    def move(pos):
        pos