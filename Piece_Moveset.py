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

        Xblocked = False
        Yblocked = False
        
        if self.color == "White":
            for i in range(8):
                #Adds the square onto the list of valid moves
                if Xblocked == False:
                    moves.append([0 + i, self.currPos.x]) 
                if Yblocked == False:
                    moves.append([self.currPos.y, 0+i])
                    # TODO: Add gamestate, if the row is swuare has a piece, this column is blcoked 
        elif self.color == 'Black':
            moves.append([0 + i, self.x]) 
            moves.append([self.y, 0+i])
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
        