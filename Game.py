from tkinter import *
import random
from LinkedList import *

def StartGame(frmLobby, window, height, width, seed):
    frmLobby.forget()
    frmGame = Frame(window, bg="black")
    #lblTitle = Label(frmGame, text="HELLO", width=20, height=5)
    #lblTitle.grid(row=0, column=0)

    field = GenerateField(height, width, seed)
    lblField = [[Label(frmGame, width=5, height=2) for _ in range(height)] for _ in range(width)]

    for i in range(height):
        for j in range(width):
            match field[i][j]:
                case 1:
                    lblField[i][j].config(bg="white", text=f"({i},{j})")
                case 0:
                    lblField[i][j].config(bg="black", text=f"({i},{j})")
                case -1:
                    lblField[i][j].config(bg="blue", text=f"({i},{j})")
                case -4:
                    lblField[i][j].config(bg="red", text=f"({i},{j})")

            lblField[i][j].grid(row=i, column=j)
            print(f'{field[i][j]:4}' , end=", ")
        print()

    frmGame.pack()


def GenerateField(height, width, seed):
    field = [[-1 for _ in range(height)] for _ in range(width)]
    # outlide walls need to be set
    # custom maps
    # seed random to generate
    # tictac = 1
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

    branchPossible = []

    # clear around box
    for i in range(-3,4): # not inclusive for 4
        field[middleHeight - 2][middleWidth + i] = 0
        # add block above to list for branch
        branchPossible.append([middleHeight - 3, middleWidth + i, "up"])
        field[middleHeight + 2][middleWidth + i] = 0
        # add block below to list for branch
        branchPossible.append([middleHeight + 3, middleWidth + i, "down"])

    for i in range(-2, 3):  # not inclusive for 2
        pass
        field[middleHeight + i][middleWidth - 3] = 0
        # add block to the left to list for branch
        branchPossible.append([middleHeight + i, middleWidth - 4, "left"])
        field[middleHeight + i][middleWidth + 3] = 0
        # add block to the right to list for branch
        branchPossible.append([middleHeight + i, middleWidth + 4, "right"])


    # temp for testing set block red if can be branch
    print(branchPossible)
    for branch in branchPossible:
        field[branch[0]][branch[1]] = -4

    # box gate
    field[middleHeight - 1][middleWidth] = -2

    # seed random
    random.seed(seed)
    numBranches = random.randint(2,14)

    print(f"branches: {numBranches}")

    llBranchesTail = branch

    # loop for each branch
    for i in range(numBranches):
        # cheack if the branch can be placed
        item = random.randint(0, len(branchPossible) - 1)
        attemptBranch = branchPossible[item]

        # remove attemptBranch from list
        branchPossible.pop(item)

        # check if valid
        valid = True
        if field[attemptBranch[0] - 1][attemptBranch[1]] == 1 or field[attemptBranch[0] + 1][attemptBranch[1]] == 1:
            valid = False
        if field[attemptBranch[0]][attemptBranch[1] - 1] == 1 or field[attemptBranch[0]][attemptBranch[1] + 1] == 1:
            valid = False

        # if valid place branch
        if valid:
            field[attemptBranch[0]][attemptBranch[1]] = 1

            # extend branch one block out
            j = 0
            k = 0
            match attemptBranch[2]:
                case "up":
                    j =  -1
                case "down":
                    j = 1
                case "left":
                    k = -1
                case "right":
                    k = 1
            field[attemptBranch[0] + j][attemptBranch[1] + k] = 1
            if i == 0:
                llBranchesHead = branch(attemptBranch)
                llBranchesTail = llBranchesHead
            else:
                llBranchesTemp = branch(attemptBranch)
                llBranchesTail.next(llBranchesTemp)
                llBranchesTail = llBranchesTemp



    # for linked list fill area


    return field