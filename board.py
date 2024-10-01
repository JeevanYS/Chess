import pygame
from pieces import *

class Board:
    def __init__(self):
        self.default_board = [['r', 'h', 'b', 'q', 'k', 'b', 'h', 'r'],
                                ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
                                [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                                [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                                [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                                [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                                ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
                                ['R', 'H', 'B', 'Q', 'K', 'B', 'H', 'R']]
        self.board = self.default_board
        for i in range(len(self.default_board)):
            for j in range(len(self.default_board[i])):
                if(i <= 1):
                   team = 0
                elif(i>=6):
                    team = 1
                else:
                    team = 2
                self.default_board[i][j] = Pieces(self.default_board[i][j], team)

    def print_board(self):
        print("                    WHITE")
        print("---"*16)
        for i in range(8):
            for j in range(8):
                print("  "+self.board[i][j].code, end="  |")
            print("\n"+"---"*16,end="\n")
        print("                    BLACK")

    def get(self,x1,y1):
        return self.board[y1-1][x1-1]

    def checkLegal(self, x1, y1, x2, y2, piece):
        if(self.board[y1-1][x1-1].team != self.board[y2-1][x2-1].team):
            if(piece.code.lower() == "h" and ((x2-x1)**2 + (y2-y1)**2) == 5):
                return  True
            if(piece.code.lower() == "b" and (x2-x1)**2 == (y2-y1)**2):
                return True
            if(piece.code.lower() == "r" and (x1==x2 or y1==y2)):
                if(x1 == x2):
                    for i in range(y1-1, y2, 1 if y1<y2 else -1):
                        print(self.get(x1, i).code)
                return True
                        
        return False   


    def edit(self, x1, y1, x2, y2):
        piece = self.board[y1-1][x1-1]
        if(self.checkLegal(x1,y1,x2,y2, piece)):
            self.board[y2-1][x2-1] = Pieces(piece.code, piece.team)
            self.board[y1-1][x1-1] = Pieces(" ", 2)