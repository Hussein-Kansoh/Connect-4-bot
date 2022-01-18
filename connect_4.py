import math
import sys

import numpy as np
import pygame

numRows = 6
numColumns = 7
active = True
turn = 0
White = (255,255,255)
Blue = (0,0,255)
Black = (0,0,0)
Red = (255,0,0)
Yellow = (255,255,0)
flag = True

def init(board):
    for i in range(numRows):
        for j in range(numColumns):
            board[i][j]=0

def createBoard():
    board = np.zeros((numRows, numColumns));
    return board

def isValid(board, col):
    if col<0 or col>6:
        return False
    if board[5][col]==1:
        return False
    return True

def rowOfColumn(board, col):
    for row in range(numRows):
        if board[row][col] == 0:
            return row


def winningHorizontal(board, row, col, piece):
    if col + 3 < 7:
        if board[row][col] == piece and board[row][col + 1] == piece and board[row][col + 2] == piece and board[row][col + 3] == piece:
            return True
    if col - 3 > -1:
        if board[row][col] == piece and board[row][col - 1] == piece and board[row][col - 2] == piece and board[row][col - 3] == piece:
            return True
    if col + 1 < 7 and col - 2 > -1:
        if board[row][col] == piece and board[row][col + 1] == piece and board[row][col - 1] == piece and board[row][col - 2] == piece:
            return True
    if col + 2 < 7 and col - 1 > -1:
        if board[row][col] == piece and board[row][col + 1] == piece and board[row][col + 2] == piece and board[row][col - 1] == piece:
            return True
    return False

def winningVertical(board, row, col, piece):
    if row-3>-1:
        if board[row][col] == piece and board[row-1][col] == piece and board[row-2][col] == piece and board[row-3][col] == piece:
            return True
    return False

def winningSlashDiagonal(board, row, col, piece):
    if row-3>-1 and col-3>-1:
        if board[row][col] == piece and board[row-1][col-1] == piece and board[row-2][col-2] == piece and board[row-3][col-3] == piece:
            return True
    if row+3<8 and col+3<7:
        if board[row][col] == piece and board[row + 1][col + 1] == piece and board[row + 2][col + 2] == piece and board[row + 3][col + 3] == piece:
            return True
    if row+2<8 and col+2<7 and row-1>-1 and col-1>-1:
        if board[row][col] == piece and board[row + 1][col + 1] == piece and board[row + 2][col + 2] == piece and board[row - 1][col - 1] == piece:
            return True
    if row+1<8 and col+1<7 and row-2>-1 and col-2>-1:
        if board[row][col] == piece and board[row + 1][col + 1] == piece and board[row - 1][col - 1] == piece and board[row - 2][col - 2] == piece:
            return True

def winningBackSlashDiagonal(board, row, col, piece):
    if row - 3 > -1 and col + 3 < 7:
        if board[row][col] == piece and board[row - 1][col + 1] == piece and board[row - 2][col + 2] == piece and board[row - 3][col + 3] == piece:
            return True
    if col - 3 > -1 and row + 3 < 8:
        if board[row][col] == piece and board[row + 1][col - 1] == piece and board[row + 2][col - 2] == piece and board[row + 3][col - 3] == piece:
            return True
    if row+2<8 and col+1<7 and row-1>-1 and col-2>-1:
        if board[row][col] == piece and board[row + 1][col - 1] == piece and board[row + 2][col - 2] == piece and board[row - 1][col + 1] == piece:
            return True
    if col+2<8 and row+1<7 and col-1>-1 and row-2>-1:
        if board[row][col] == piece and board[row + 1][col - 1] == piece and board[row - 1][col + 1] == piece and board[row - 2][col + 2] == piece:
            return True

def winningMove(board, row, col, piece):
    if winningHorizontal(board, row, col, piece) or winningVertical(board, row, col, piece) or winningSlashDiagonal(board, row, col, piece) or winningBackSlashDiagonal(board, row, col, piece):
        return True
    else:
        return False

def drawBoard(board):
    for c in range(numColumns):
        for r in range(numRows):
            pygame.draw.rect(screen, Blue, (c*EntrySize, r*EntrySize+EntrySize+5, EntrySize, EntrySize))
            pygame.draw.circle(screen, Black, (int (c*EntrySize+EntrySize/2), int (r*EntrySize+EntrySize+EntrySize/2)), 40)

    for c in range(numColumns):
        for r in range(numRows):
            if board[r][c]==1:
                pygame.draw.circle(screen, Red, (int (c*EntrySize+EntrySize/2), height - int (r*EntrySize+EntrySize/2)), 40)
            elif board[r][c]==2:
                pygame.draw.circle(screen, Yellow, (int (c*EntrySize+EntrySize/2), height - int (r*EntrySize+EntrySize/2)), 40)

    pygame.display.update()



board = createBoard()
pygame.init()
EntrySize = 100
width = numColumns*EntrySize
height = (numRows+1)*EntrySize
size = (width, height)
screen = pygame.display.set_mode(size)
drawBoard(board)
pygame.display.update()

while active:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                active = False;
            if event.key == pygame.K_RETURN:
                init(board)
                turn = 0
                flag = True
                screen.fill(Black)
                drawBoard(board)
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEMOTION and flag:
            pygame.draw.rect(screen, Black, (0, 0, width, 100))
            xPosition = event.pos[0]
            if turn == 0:
                pygame.draw.circle(screen, Red, (xPosition, 50), 40)
            else:
                pygame.draw.circle(screen, Yellow, (xPosition, 50), 40)
        pygame.display.update()
        if event.type == pygame.MOUSEBUTTONDOWN:
             #player1 turn
            if turn == 0:
                xPosition = event.pos[0]
                move = math.floor (xPosition/EntrySize)
                if isValid(board, move):
                    row = rowOfColumn(board, move)
                    board[row][move] = 1
                drawBoard(board)
                if winningMove(board, row, move, 1):
                    flag = False
                    myfont = pygame.font.SysFont('Comic Sans MS', 60)
                    winner = myfont.render('player 1  wins!', 1, White)
                    playAgain = myfont.render('Click Enter to Play Again', 1, White)
                    Quit = myfont.render('Click Backspace to quit', 1, White)
                    screen.fill(Black)
                    screen.blit(winner, (150,100))
                    screen.blit(playAgain, (7, 250))
                    screen.blit(Quit, (20, 400))
                    pygame.display.update()
                turn = 1

             #player2 turn
            elif turn == 1:
                xPosition = event.pos[0]
                move = math.floor (xPosition/100)
                if isValid(board, move):
                    row = rowOfColumn(board, move)
                    board[row][move] = 2
                drawBoard(board)
                if winningMove(board, row, move, 2):
                    flag = False
                    myfont = pygame.font.SysFont('Comic Sans MS', 60)
                    winner = myfont.render('player 2  wins!', 1, White)
                    splayAgain = myfont.render('Click Enter to Play Again', 1, White)
                    Quit = myfont.render('Click Backspace to quit', 1, White)
                    screen.fill(Black)
                    screen.blit(winner, (150,100))
                    screen.blit(playAgain, (7, 250))
                    screen.blit(Quit, (20, 400))
                    pygame.display.update()
                turn = 0

