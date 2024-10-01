import pygame
import time
from board import *

fps = 60
whiteSqColor = (255,249,214)
blackSqColor = (100,100,100)
grid_size = 80
piece_size = 64

board = Board()

pygame.init()
screen = pygame.display.set_mode((grid_size*8, grid_size*8))
pygame.display.set_caption("Chess!!!")

#Loading Chess Piece Images


def draw():
    screen.fill((255,255,255))
    #BOARD
    for i in range(8):
        for j in range(8):
            if(i+j)%2 == 0:
                color = whiteSqColor
            else:
                color = blackSqColor
            pygame.draw.rect(screen, color, pygame.Rect(j*grid_size, i*grid_size, grid_size, grid_size))
            
            #PIECES
            if(board.board[i][j].code != " "):
                offset = (grid_size-piece_size)/2
                screen.blit(Pieces.getImage(board.board[i][j].code),(j*grid_size + offset, i*grid_size + offset), pygame.Rect(0,0,piece_size, piece_size))
    pygame.display.update()

draw()
running = True
x1,y1,x2,y2 = 0,0,0,0
while running:
    for event in pygame.event.get():
        if(event.type == pygame.QUIT):
            running = False
        if(event.type == pygame.MOUSEBUTTONDOWN):
            x1, y1 = pygame.mouse.get_pos()
            x1, y1 = (x1//grid_size) + 1, (y1//grid_size) + 1
            print(x1,y1)
            
        if(event.type == pygame.MOUSEBUTTONUP):
            x2, y2 = pygame.mouse.get_pos()
            x2, y2 = (x2//grid_size) + 1, (y2//grid_size) + 1
            print(x2, y2)
            board.edit(x1,y1,x2,y2)
            draw()

    time.sleep(1/fps)
