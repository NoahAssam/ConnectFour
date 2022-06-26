"""
Exact same as main besides whos_turn function
"""

import tkinter
from tkinter import *
from random import seed
from random import randint
def single():
    seed(1)
    import random
    root = tkinter.Tk()
    count = 0
    # 0== no piece, 1== 🔴player1/ 2== 🔵player2/bot
    list = [[0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0]]
    row = 6
    col = 7

    def board(display, turn, n):
        #build sboard
        for r in range(row):
            for c in range(col):
                tkinter.Label(root, text='⬛', font=("Bold", 40),
                              borderwidth=.1).grid(row=r, column=c)
        # places games pieces
        for r in range(row):
            for c in range(col):
                if display[r][c] == 1:
                    tkinter.Label(root, text='🔴', font=("Bold", 30),
                                  borderwidth=.1).grid(row=r, column=c)
                if display[r][c] == 2:
                    tkinter.Label(root, text='🔵', font=("Bold", 30),
                                  borderwidth=.1).grid(row=r, column=c)
        # buttons to place pieces
        for i in range(7):
            coll = tkinter.Button(root, text="DROP COL" + str(i + 1), height=2, width=8,
                                  command=lambda x=i: check_below(x, display, turn, n))
            coll.grid(row=7, column=i)

    def if_winner(layout, turn, n):
        # Check vertical spaces
        for c in range(row):
            for r in range(3):
                if layout[r][c] == turn and layout[r + 1][c] == turn and \
                        layout[r + 2][c] == turn and layout[r + 3][c] == turn:
                    exit_button = Button(root, text="Player " + str(turn) + " won. click to exit", height=1, width=20,
                                         command=root.destroy)
                    exit_button.grid(row=10, column=1)

        # Check horizontal spaces
        for r in range(row):
            for c in range(col - 3):
                if layout[r][c] == turn and layout[r][c + 1] == turn and \
                        layout[r][c + 2] == turn and layout[r][c + 3] == turn:
                    exit_button = Button(root, text="Player " + str(turn) + " won. click to exit", height=1, width=20,
                                         command=root.destroy)
                    exit_button.grid(row=10, column=1)
        # Check diagonal spaces
        for r in range(row - 3):
            for c in range(3, col):
                if layout[r][c] == turn and layout[r + 1][c - 1] == turn and\
                        layout[r + 2][c - 2] == turn and layout[r + 3][c - 3] == turn:
                    exit_button = Button(root, text="Player " + str(turn) + " won. click to exit", height=1, width=20,
                                         command=root.destroy)
                    exit_button.grid(row=10, column=1)
        # Check diagonal spaces
        for r in range(row - 3):
            for c in range(col - 3):
                if layout[r][c] == turn and layout[r + 1][c + 1] == turn and \
                        layout[r + 2][c + 2] == turn and layout[r + 3][c + 3] == turn:
                    exit_button = Button(root, text="Player " + str(turn) + " won. click to exit", height=1, width=20,
                                         command=root.destroy)
                    exit_button.grid(row=10, column=1)
        whos_turn(layout,n)

    def check_below(rows, display, turn, n):
        if display[5][rows] != 1 and display[5][rows] != 2:
            display[5][rows] = turn
            if_winner(display, turn, n)
        elif display[4][rows] != 1 and display[4][rows] != 2:
            display[4][rows] = turn
            if_winner(display, turn, n)
        elif display[3][rows] != 1 and display[3][rows] != 2:
            display[3][rows] = turn
            if_winner(display, turn, n)
        elif display[2][rows] != 1 and display[2][rows] != 2:
            display[2][rows] = turn
            if_winner(display, turn, n)
        elif display[1][rows] != 1 and display[1][rows] != 2:
            display[1][rows] = turn
            if_winner(display, turn, n)
        elif display[0][rows] != 1 and display[0][rows] != 2:
            display[0][rows] = turn
            if_winner(display, turn, n)
        else:
            print("cant place here, try again")
            board(display, turn, n)

    """
    if its the obts turn, it sends a random space to 
    check_below function
    """
    def whos_turn(layout, n):
        if n % 2 == 0:
            x = 0
        else:
            n = n + 1
            index = randint(-1, 7)
            check_below(index, layout, 2, n)
        n = n + 1
        board(layout, 1, n)

    whos_turn(list, count)
    root.mainloop()