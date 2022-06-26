#used to import main and bot
from main import *
from bot import *




def display(button):
    """
    sends the use to either 1v1, single player, or exit program
    depings on the button they press
    """
    if button == 2:
        double()
    if button == 3:
        single()
    if button == 4:
        quit()


def options():
    """
    displays the buttons and send information to display
    :return:
    """
    root = tkinter.Tk()
    root.geometry("350x350")
    welcome = tkinter.Button(root, text="THIS IS CONNECT FOUR, SELECT AN OPTION\n"
                                        "PLAYER ONE BLACK, TWO WHITE",
                             height=5, width=50)
    welcome.grid(row=1, column=0)

    two_player=tkinter.Button(root, text="PRESS TO PLAY 1V1",
                              height=5, width=50, command=lambda x=2: display(x))
    two_player.grid(row=2, column=0)

    one_player=tkinter.Button(root, text="PRESS TO PLAY BOT",
                              height=5, width=50,command=lambda x=3: display(x))
    one_player.grid(row=3, column=0)

    exit=tkinter.Button(root, text="PRESS TO EXIT",
                        height=5, width=50, command=lambda x=4: display(x))
    exit.grid(row=4, column=0)

    root.mainloop()

options()