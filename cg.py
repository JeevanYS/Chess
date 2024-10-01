default_board = [["R","H","B","K","Q","B","H","R"],
                 ["P","P","P","P","P","P","P","P"],
                 [" "," "," "," "," "," "," "," "],
                 [" "," "," "," "," "," "," "," "],
                 [" "," "," "," "," "," "," "," "],
                 [" "," "," "," "," "," "," "," "],
                 ["P","P","P","P","P","P","P","P"],
                 ["R","H","B","K","Q","B","H","R"]]
board = [["R","H","B","K","Q","B","H","R"],
         ["P","P","P","P","P","P","P","P"],
         [" "," "," "," "," "," "," "," "],
         [" "," "," "," "," "," "," "," "],
         [" "," "," "," "," "," "," "," "],
         [" "," "," "," "," "," "," "," "],
         ["P","P","P","P","P","P","P","P"],
         ["R","H","B","K","Q","B","H","R"]]
def move(x1,y1,x2,y2,piece):
    f=0
    if(y1=='A'):
        b = 1
    elif(y1=='B'):
        b = 2
    elif(y1=='C'):
        b = 3
    elif(y1=='D'):
        b = 4
    elif(y1=='E'):
        b = 5
    elif(y1=='F'):
        b = 6
    elif(y1=='G'):
        b = 7
    elif(y1=='H'):
        b = 8
    if(y2=='A'):
        c = 1
    elif(y2=='B'):
        c = 2
    elif(y2=='C'):
        c = 3
    elif(y2=='D'):
        c = 4
    elif(y2=='E'):
        c = 5
    elif(y2=='F'):
        c = 6
    elif(y2=='G'):
        c = 7
    elif(y2=='H'):
        c = 8
    if(piece == "R" and (x1==x2 or b==c)):
        if(x1==x2):
            if():
                if(board[c-1][x1-1].color!=1):
                    for i in range (b,c-1):
                        if(board[i][i]!=" "):
                            f=1
                            break
                        else:
                            f=0
                    if(f==1):
                        print("Illegal Move")
                    else:
                        board[c-1][x2-1]=board[b-1][x1-1]
                        board[b-1][x1-1]= Piece(default_board[5][5],2)
                else:
                    print("Illegal Move")
        else:
            for i in range (x1,x2-1):
                if(board[i][i]!=" "):
                    f=1
                    break
                else:
                    f=0
            if(f==1):
                print("Illegal Move")
            else:
                board[c-1][x2-1]=board[b-1][x1-1]
                board[b-1][x1-1]= Piece(default_board[5][5],2)
    elif(piece == "B" and ((x1-x2==b-c)or(x1-x2==-(b-c)))):
        board[c-1][x2-1]=board[b-1][x1-1]
        board[b-1][x1-1]= Piece(default_board[5][5],2)
    elif(piece == "H" and (((x1+2==x2 or x1-2==x2)and(b+1==c or b-1 == c))or((x1+1==x2 or x1-1==x2)and(b+2==c or b-2==c)))):
        board[c-1][x2-1]=board[b-1][x1-1]
        board[b-1][x1-1]=Piece(default_board[5][5],2)
    elif(piece == "Q" and ((x1==x2 or y1==y2)or((x1-x2==b-c)or(x1-x2==-(b-c))))):
        board[c-1][x2-1]=board[b-1][x1-1]
        board[b-1][x1-1]=Piece(default_board[5][5],2)
    elif(piece=="P"and (b+2==c or b-2==c or (board[c-1][x2-1]!=" "))):
        board[c-1][x2-1]=board[b-1][x1-1]
        board[b-1][x1-1]=Piece(default_board[5][5],2)
    elif(piece=="K"and ((b+1==c) or (b-1==c) or (x1+1==x2) or (x1-1==x2) or (x1+1==x2 and b+1==c) or (x1-1==x2 and b+1==c) or (x1+1==x2 and b-1==c) or (x1-1==x2 and b-1==c))):
        board[c-1][x2-1]=board[b-1][x1-1]
        board[b-1][x1-1]=Piece(default_board[5][5],2)
    else :
        print("Illegal Move")
class Piece:
    def __init__(self, name, team):
        self.name = name
        self.color = team
    def display(self):
        return f" {self.name}"
for i in range (0,8):
    for j in range(0,8):
        if(i<=1):
            e = 1
        elif(i>=6):
            e=0
        else:
            e=2
        board[i][j] = Piece(board[i][j],e)
def print_board():
    z=0
    print("     WHITE")
    print(" 1 2 3 4 5 6 7 8")
    print('---'*11)
    for row in board:
        row_display = []
        for piece in row:
            row_display.append(piece.display())
        print('|'+' |'.join(row_display)+" | ",end = " "+chr(65+z)+"\n")
        print('---'*11)
        z+=1
    print("    BLACK")
print_board()

while True:
    exec(input())