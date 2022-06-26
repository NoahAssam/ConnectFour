
# USed to import tkinter
import tkinter
from tkinter import *


def double():
    """
    double contains the entire code.
    it makes two players playing possible
    """
    root = tkinter.Tk()
    count = 0
    # 0== no piece, 1== 🔴player1/ 2== 🔵player2/bot
    list = [[0, 0, 0, 0, 0, 0, 0], # created gameboard to keep track of data
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0]]
    row = 6
    col = 7

    def board(display, turn, n): # display is the grid, turn is which player, n is to
        # decide who goes next
        """
        Creates the board tiles, places the game
        pieces depending on the placements of two's
        and ones in the two-d array. creates the buttons
        to places the pieces. send data to check_below
        """
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
        """
        checks who won y continuously looking for 4 of the same
        numbers in a row. either vertical, horizontal, diagonal.
        uses two for loops to go through the list of numbers. uses
        diffenent sizes of columns and rows to make sure the loop
        doesnt go out of range. if a row of the same numbers in four did happen.
        a button of who qins pops up and can click it to exit. if not winner
        gots to whos_Turn
        """
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

    def check_below(coll, display, turn, n): # coll is what column it is
        """
        checks if the bottom most available space
        doesnt have a 1 or 2. this has the effect of gravity
        that the actually pieces have irl
        """
        if display[5][coll] == 0:
            display[5][coll] = turn
            if_winner(display, turn, n)
        elif display[4][coll] == 0:
            display[4][coll] = turn
            if_winner(display, turn, n)
        elif display[3][coll] == 0:
            display[3][coll] = turn
            if_winner(display, turn, n)
        elif display[2][coll] == 0:
            display[2][coll] = turn
            if_winner(display, turn, n)
        elif display[1][coll] == 0:
            display[1][coll] = turn
            if_winner(display, turn, n)
        elif display[0][coll] == 0:
            display[0][coll] = turn
            if_winner(display, turn, n)
        else:
            print("cant place here, try again")
            board(display, turn, n)

    def whos_turn(layout, n):
        """
        tells who wins my continuously counting and
        then doing eiher odd or even. sends to the board
        """
        if n % 2 == 0:
            turn = 1
        else:
            turn = 2
        n = n + 1
        board(layout, turn, n)

    whos_turn(list, count)
    root.mainloop()



