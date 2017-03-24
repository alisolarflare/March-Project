import pygame
import time

class Metrics():
    draw = 0;
    rect = 0;

    def print():
        print(str(Metrics.draw) +"|\n"+ str(Metrics.rect))
    
class Tile():
    def __init__ (self, x, y, length, piece=None, background=None):
        self.x = x
        self.y = y
        self.length = length
        self.piece = piece;

        if (background != None):
            self.background = background;
        else:
            if (x + y) % 2 == 0:
                self.background = Color.light;
            else:
                self.background = Color.dark;
        
    def rect(self, displayx, displayy):
        Metrics.rect += 1
        return pygame.Rect(displayx + self.x * self.length,
                           displayy + self.y * self.length,
                           self.length,
                           self.length)
        

    
class World():
    def __init__(self, width=8, height=8):
        self.width = width;
        self.height = height;
        self.data = [["" for y in range(width)] for x in range(height)]
        self.font = pygame.font.SysFont("comicsansms", 30)
        
    
    def draw(self, screen, xMargin, yMargin, squareSize):
        for y in range(0,self.height):
            for x in range(0,self.width):
                self.drawTile(screen, xMargin, yMargin, squareSize, x, y)
                Metrics.draw += 1;
                
    def drawTile(self, screen, xMargin, yMargin, squareSize, x, y):
        self.drawSquare(screen, xMargin, yMargin, squareSize, x, y)
        self.drawPiece( screen, xMargin, yMargin, squareSize, x, y)
        
    def drawPiece(self, screen, xMargin, yMargin, squareSize, x, y):
        red   = x * 30
        green = y * 30 
        blue  = x * 10
        color = (red, green, blue)
        text = self.font.render(self.data[x][y], False, color)

        displayx = xMargin + x * squareSize
        displayy = yMargin + y * squareSize
        
        screen.blit(text,(displayx, displayy))

    def drawSquare(self, screen, xMargin, yMargin, squareSize, x, y):
            if (x + y) % 2 == 0:
                color = Color.light;
            else:
                color = Color.dark;

            displayx = xMargin + x * squareSize
            displayy = yMargin + y * squareSize
            rect = pygame.Rect(
                displayx,
                displayy,
                squareSize,
                squareSize);
            
            pygame.draw.rect(screen, color, rect)
            Metrics.draw += 1;

                                    
            
class ChessBoard(World):
    def __init__(self):
        super().__init__(8,8) #m8
        majorpieces = [
            ("WR", "a1"),
            ("WN", "b1"),
            ("WB", "c1"),
            ("WQ", "d1"),
            ("WK", "e1"),
            ("WB", "f1"),
            ("WN", "g1"),
            ("WR", "h1"),
            ("BR", "a8"),
            ("BN", "b8"),
            ("BB", "c8"),
            ("BQ", "d8"),
            ("BK", "e8"),
            ("BB", "f8"),
            ("BN", "g8"),
            ("BR", "h8"),
        ]
        for piece in majorpieces:
            name, loc = piece
            self.insert(name,loc)
            
        for i in range (0, 8):
            loc = chr(ord('a') + i) + "2"
            self.insert("WP",  loc);
        
        for i in range (0, 8):
            loc = chr(ord('a') + i) + "7"
            self.insert("BP",  loc);
            
    def labelSquares(self):
        for y in range(0, self.height):
            for x in range(0 , self.width):
                row = str(chr(x + ord('a')))
                col = str(self.height-y)
                
                text = row + col
                self.insert(text, text);
                
    def insert(self,string, pos):
        x = ord(pos[0]) - ord('a');
        y = self.height - int(pos[1]);
        self.data[x][y] = str(string);
        
        
class Color():
    light = (255, 206, 158)
    dark = (209, 139, 71)
