import pygame
import numpy
import random


WIDTH, HEIGHT = 709,709
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
BLACK = (0,0,0)
WHITE=(255, 255, 255)
BLUE = (0,14,71)

pygame.display.set_caption("Tic Tac Toe")

 
grid = {}           #0 for cross, 1 for nut, 2 for empty
playing = True

for i in range(3):
    grid[i] = []
    for j in range(3):
        grid[i].append(2)

imgs = []
imgs.append(pygame.image.load("Animated_Projects/Tic_Tac_Toe_AI/Graphics/CROSS.png"))
imgs.append(pygame.image.load("Animated_projects/Tic_Tac_Toe_AI/Graphics/CIRCLE.png"))

for i in range(2):
    imgs[i] = pygame.transform.scale(imgs[i], (235,235))


def convert(num):
    if(num==0):return 1
    return -1


def value(board):
    for i in range(3):
        if(board[i][0]==board[i][1] and board[i][0]==board[i][2] and board[i][0]!=2):return convert(board[i][1])
        
        if(board[0][i]==board[1][i] and board[0][i]==board[2][i] and board[0][i]!=2):return convert(board[1][i])

    if(board[0][0]==board[1][1] and board[0][0]==board[2][2] and board[0][0]!=2):return convert(board[0][0])

    if(board[0][2]==board[1][1] and board[0][2]==board[2][0] and board[0][2]!=2):return convert(board[2][0])

    return 0



def minimax(board, depth):

    if(check(board)):
        return value(board)
    
    if depth%2:
        best = 2
        #for each move: best = min(best, value(board, depth+1))
        for i in range(3):
            for j in range(3):
                if(board[i][j]==2):
                    newBoard = board
                    newBoard[i][j]=1
                    best = min(best, minimax(newBoard, depth+1))
                    newBoard[i][j]=2
        
        #return best
        return best

   # do the opposite for depth even 
    best = -2
    for i in range(3):
        for j in range(3):
            if(board[i][j]==2):
                newBoard = board
                newBoard[i][j]=0
                best = max(best, minimax(newBoard, depth+1))
                newBoard[i][j]=2

    
    return best

 



def bestMove(board):
    bestval = 2
    ret = (-1,-1)

    for i in range(3):
        for j in range(3):

            if(board[i][j]==2):
                newBoard = board
                newBoard[i][j] = 1
                k = minimax(newBoard,0)
                if(k<bestval):
                    ret = (i,j)
                    bestval = k
                newBoard[i][j]=2

    
    return ret




def check(board):

    Full = True
    for i in range(3):
        for j in range(3):
            if(board[i][j]==2): Full = False
    
    if(Full): return True

    for i in range(3):
        if(board[i][0]==board[i][1] and board[i][0]==board[i][2] and board[i][0]!=2):return True
        
        if(board[0][i]==board[1][i] and board[0][i]==board[2][i] and board[0][i]!=2):return True

    if(board[0][0]==board[1][1] and board[0][0]==board[2][2] and board[0][0]!=2):return True

    if(board[0][2]==board[1][1] and board[0][2]==board[2][0] and board[0][2]!=2):return True

    return False


def clicked(x, y, turn):

    global grid, playing



    board = grid
    if(turn%2==1):
        x,y = bestMove(board)
        #print((x,y))

    if(grid[x][y]<2):
        return -1
    

    grid[x][y]=turn

    if(check(grid)):playing = False
    return 0



def get_coordinates(pos):
    x,y = pos
    return (int(x/235), int(y/235))



def draw():
    for i in range(3):
        for j in range(3):
            if(grid[i][j]==2):
                pygame.draw.rect(WIN, WHITE, (1+236*i,1+236*j, 235, 235))
            
            else: WIN.blit(imgs[grid[i][j]], (1+236*i,1+236*j))

            


    


run = True
T = 1
while run:

    execute = False
    #time delay
    pygame.time.delay(10)


    for event in pygame.event.get():
        if (event.type==pygame.QUIT): run = False
        if event.type==pygame.MOUSEBUTTONDOWN and playing ==True:
            print(grid)
            T+=1
            x,y = get_coordinates(pygame.mouse.get_pos())
            T+=clicked(x,y,T%2)
    
            


    WIN.fill(BLACK)
    draw()
    pygame.display.update()

    





pygame.quit()

