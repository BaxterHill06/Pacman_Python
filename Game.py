from tkinter import *

def StartGame(frmLobby, window, height, width):
    frmLobby.forget()
    frmGame = Frame(window, bg="black")
    #lblTitle = Label(frmGame, text="HELLO", width=20, height=5)
    #lblTitle.grid(row=0, column=0)

    field = GenerateField(height, width)
    lblField = [[Label(frmGame, width=5, height=2) for _ in range(height)] for _ in range(width)]

    for i in range(height):
        for j in range(width):
            if field[i][j] == -1:
                lblField[i][j].config(bg="blue", text=f"({i},{j})")
            lblField[i][j].grid(row=i, column=j)
            print(f'{field[i][j]:4}' , end=", ")
        print()

    frmGame.pack()


def GenerateField(height, width):
    field = [[-1 for _ in range(height)] for _ in range(width)]
    # outlide walls need to be set
    # custom maps
    # seed random to generate
    # wall = -1
    # gate = -2

    # open teleport
    middleHeight = height // 2
    field[middleHeight][0] = 0
    field[middleHeight][width-1] = 0

    # middle box
    middleWidth = width // 2
    print(middleWidth)
    field[middleHeight][middleWidth] = 0
    field[middleHeight][middleWidth - 1] = 0
    field[middleHeight][middleWidth + 1] = 0

    # clear around box
    for i in range(-3,4): # not inclusive for 4
        field[middleHeight - 2][middleWidth + i] = 0
        field[middleHeight + 2][middleWidth + i] = 0

    for i in range(-1, 2):  # not inclusive for 2
        pass
        field[middleHeight + i][middleWidth - 3] = 0
        field[middleHeight + i][middleWidth + 3] = 0

    # box gate
    field[middleHeight - 1][middleWidth] = -2

    # seed random

    # select 2-14 branch spots

    return field