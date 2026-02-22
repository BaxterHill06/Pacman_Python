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
                lblField[i][j].config(bg="black")
            lblField[i][j].grid(row=i, column=j)
            print(f'{field[i][j]:4}' , end=", ")
        print()

    frmGame.pack()


def GenerateField(height, width):
    field = [[0 for _ in range(height)] for _ in range(width)]
    # outlide walls need to be set
    # custom maps
    # seed random to generate
    # wall = -1
    # gate = -2

    # place outside walls
    for i in range(width):
        field[0][i] = -1
        field[i][0] = -1
        field[height - 1][i] = -1
        field[i][height - 1] = -1

    # open teleport
    middleHeight = height // 2 + 1
    field[middleHeight][0] = 0
    field[middleHeight][width-1] = 0

    # middle box
    middleWidth = width // 2 + 1
    field[middleWidth][0] = 0
    field[middleWidth][height-1] = 0

    for i in range(3):
        field[middleHeight - 1][middleWidth - i] = -1
        field[middleHeight - 1][middleWidth + i] = -1
        field[middleHeight + 1][middleWidth - i] = -1
        field[middleHeight + 1][middleWidth + i] = -1

    field[middleHeight][middleWidth + 2] = -1
    field[middleHeight][middleWidth - 2] = -1

        # box gate
    field[middleHeight - 1][middleWidth] = -2

    return field