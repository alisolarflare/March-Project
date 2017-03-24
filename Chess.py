import sys, pygame
from Display import *
from EEngine import *

    
pygame.init();

display = Display(800,600);
screen = display.screen();
board = ChessBoard();
clock = pygame.time.Clock();

tileHeight = display.height / board.height;
tileWidth = display.width / board.width;

leftMargin = 0;
topMargin = 0;
if (tileWidth < tileHeight):
    squareSize = tileWidth;
    topMargin = (display.height - squareSize * board.hheight)/2
elif(tileHeight < tileWidth):
    squareSize = tileHeight;
    leftMargin = (display.width  - squareSize *  board.width)/2
else:
    squareSize = tileWidth;

running = True;
board.draw(screen, leftMargin, topMargin, squareSize)
counter = 0;
while (running):
    clock.tick(40)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False;
        elif event.type == pygame.MOUSEBUTTONDOWN:
            (posX, posY) = pygame.mouse.get_pos()
            rect = pygame.Rect(posX - 5, posY - 5, 10, 10)
            pygame.draw.rect(screen, (255,0,0), rect)
            



        counter += 1
        if (counter > 20):
            Metrics.print()
            counter = 0
        
    
    

    pygame.display.flip()            
            

pygame.quit();
sys.exit();

