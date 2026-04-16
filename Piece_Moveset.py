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
        self.sprite
        #self.temp = pygame.image.load(self.sprite)
        return self.rect, self.sprite
  

class Pawn(Piece):
    def __init__(self, currPos, color):
        super().__init__(currPos = currPos, color= color)
        self.value = 1
        self.color = color
        self.sprite = pygame.image.load(f"sprites/{color}Pawn.png")

    def validateMove(self, newpos):
        if self.color == "White":
            if int(newpos.y) == int(self.currPos.y - 1):
                self.currPos.y -= 1
                return True
            else:
                return False
        elif self.color == "Black":
            if int(newpos.y) == int(self.currPos.y + 1):
                self.currPos.y += 1
                return True
            else:
                return False
        
class Rook(Piece):
    def __init__(self, currPos, color):
        super().__init__(currPos = currPos, color = color)
        self.value = 5
        self.color = color
        self.sprite = pygame.image.load(f"sprites/{color}Rook.png")
    def moveSet(self, currPos):
        pass
        
class Bishop(Piece):
    def __init__(self, currPos, color):
        super().__init__(currPos = currPos, color= color)
        self.value = 3
        self.color = color
        self.sprite = pygame.image.load(f"sprites/{color}Bishop.png")
    def move(pos):
        pos

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

    def move(pos):
        pos