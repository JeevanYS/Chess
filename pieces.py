import pygame
class Pieces:

    #WhitePiece
    B = pygame.image.load("pieces/wB.png")
    H = pygame.image.load("pieces/wH.png")
    K = pygame.image.load("pieces/wK.png")
    P = pygame.image.load("pieces/wP.png")
    Q = pygame.image.load("pieces/wQ.png")
    R = pygame.image.load("pieces/wR.png")

    #BlackPieces
    b = pygame.image.load("pieces/bB.png")
    h = pygame.image.load("pieces/bH.png")
    k = pygame.image.load("pieces/bK.png")
    p = pygame.image.load("pieces/bP.png")
    q = pygame.image.load("pieces/bQ.png")
    r = pygame.image.load("pieces/bR.png")

    def __init__(self, pawn_name: str, team: int = 2):
        self.code = pawn_name
        self.team = team

    def getImage(pawnName):
        d = {"B":Pieces.B,"H":Pieces.H,"K":Pieces.K,"P":Pieces.P,"Q":Pieces.Q,"R":Pieces.R,
             "b":Pieces.b,"h":Pieces.h,"k":Pieces.k,"p":Pieces.p,"q":Pieces.q,"r":Pieces.r}
        return d[pawnName]