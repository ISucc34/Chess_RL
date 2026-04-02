import pygame


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
        self.rect = pygame.rect(0,0,64,64)
        self.sprite = "t.png"
        
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