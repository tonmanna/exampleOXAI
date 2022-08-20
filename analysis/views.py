from logging import critical
from tkinter import CURRENT
import numpy as np
import random
from django.shortcuts import render
O = []
X = []
win = [[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7]]

def checkWin(p):
    for w in win:
        if all(x-1 in p for x in w):
            return True
    return False

def displayOX():
    OX = np.array([' '] * 9)
    OX[O] = ['O']
    OX[X] = ['X']
    return OX.reshape([3,3])

def calSOX(O,X):
    SO = SX = 0
    criticalmove = []
    for w in  win:
        O = [i-1 in O for i in w]
        X = [i-1 in X for i in w]
        if not any(X):
            nO = O.count(True)
            SO += nO
            if nO == 2:
                print ('critical',w)
                criticalmove = w
            if not any(O):
                SX += X.count(True)
        return SO,SX,criticalmove

def evalOX(O,X):
    SO, SX, criticalmove = calSOX(O,X)
    return 1 + SX- SO, criticalmove

def AI() :
    validmove = list (set (range(9)) - set(O+X))
    V = [-100] * 9
    for m in validmove:
        tempX = X + [m]
        V[m], criticalmove = evalOX(O,tempX)
        if len(criticalmove) > 0:
            move = [i-1 for i in criticalmove if i-1 in validmove]
            return random.choice(move)
    maxV= max(V)
    imaxV = [ i for i,j in enumerate(V) if j == maxV]
    return random.choice(imaxV)


# @csrf_exempt
def main(request):
    DISPLAY = []
    WHOWIN = "PLAING"
    CURRENT_TURN = len(O) + len(X)
    if CURRENT_TURN>= 9 :
        DISPLAY = []
        WHOWIN = "END_GAME"    
    
    movposition = 0;
    # HUMAN TURN 1-9    
    try:
        movposition = int(request.GET["position"])
    except:
        return render(request,'change.html')

    move = movposition - 1
    if move in O+X or move > 8 or move < 0 :
        return render(request, 'index.html',{'TRY_AGAIN':'ALREADY MOVE TO THIS POSITION'})
    O.append(move)
    DISPLAY = displayOX()
    if checkWin(O):
        WHOWIN = "HUMAN"
    if len(O) + len(X) == 9:
        WHOWIN = "DRAW"

    # AI TURN
    X.append(AI())
    DISPLAY = displayOX()
    if checkWin(X):
        WHOWIN = "AI"

    if len(O) + len(X) == 9:
        WHOWIN = "DRAW"
    print(DISPLAY)
    return render(request, 'index.html', {'BOARD': DISPLAY, 'WHOWIN' : WHOWIN, 'MAX_TURN': 9, 'CURRENT_TURN': CURRENT_TURN})
    
def newgame(request):
    O = []
    X = []
    return render(request,'new.html')