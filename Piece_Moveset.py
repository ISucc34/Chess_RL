from Chess import *
import pygame


class Piece():
    def __init__(self):
        pass
    def getSprite(self):
        pass


class Rook():
    def __init__(self, currPos, newPos):
        self.currPos = currPos
        self.newPos = newPos
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

class Pawn():
    def __init__(self, pos):
        self.pos = pos
        self.value = 9
    def getSprite(self):
        self.rect = (0,0,64,64)
        self.sprite = "t.png"
        return self.rect, self.sprite
        
    def spawnSprite(self, window):
        self.window = window
        self.window.blit(self.sprite, (20,20), self.rect)

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