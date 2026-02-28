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
            match field[i][j][0]:
                case 1:
                    lblField[i][j].config(bg="white", text=f"({i},{j})")
                case 0:
                    lblField[i][j].config(bg="black", text=f"({i},{j})")
                case -1:
                    lblField[i][j].config(bg="blue", text=f"({i},{j})")
                case -4:
                    lblField[i][j].config(bg="red", text=f"({i},{j})")
                case -5:
                    lblField[i][j].config(bg="orange", text=f"({i},{j})")

            lblField[i][j].grid(row=i, column=j)
            print(f'{field[i][j][0]:4}' , end=", ")
        print()

    frmGame.pack()


def GenerateField(height, width, seed):
    # nil = not in list for revealed
    field = [[[-1,"nil"] for _ in range(height)] for _ in range(width)]
    # outlide walls need to be set
    # custom maps
    # seed random to generate
    # tictac = 1
    # wall = -1
    # gate = -2

    # open teleport
    middleHeight = height // 2
    field[middleHeight][0][0] = 0
    field[middleHeight][width-1][0] = 0

    # middle box
    middleWidth = width // 2
    print(middleWidth)
    field[middleHeight][middleWidth][0] = 0
    field[middleHeight][middleWidth - 1][0] = 0
    field[middleHeight][middleWidth + 1][0] = 0

    branchPossible = []

    # clear around box
    for i in range(-3,4): # not inclusive for 4
        field[middleHeight - 2][middleWidth + i][0] = 0
        # add block above to list for branch
        branchPossible.append([middleHeight - 3, middleWidth + i, "up"])
        field[middleHeight + 2][middleWidth + i][0] = 0
        # add block below to list for branch
        branchPossible.append([middleHeight + 3, middleWidth + i, "down"])

    for i in range(-2, 3):  # not inclusive for 2
        pass
        field[middleHeight + i][middleWidth - 3][0] = 0
        # add block to the left to list for branch
        branchPossible.append([middleHeight + i, middleWidth - 4, "left"])
        field[middleHeight + i][middleWidth + 3][0] = 0
        # add block to the right to list for branch
        branchPossible.append([middleHeight + i, middleWidth + 4, "right"])


    """
    # temp for testing set block red if can be branch
    print(branchPossible)
    for branch in branchPossible:
        field[branch[0]][branch[1]][0] = -4
    """

    # box gate
    field[middleHeight - 1][middleWidth][0] = -2

    # seed random
    random.seed(seed)
    numBranches = random.randint(2,14)

    print(f"branches: {numBranches}")


    # loop for each branch
    for i in range(numBranches):
        # cheack if the branch can be placed
        item = random.randint(0, len(branchPossible) - 1)
        attemptBranch = branchPossible[item]

        # remove attemptBranch from list
        branchPossible.pop(item)

        # check if valid
        valid = True
        if field[attemptBranch[0] - 1][attemptBranch[1]][0] == 1 or field[attemptBranch[0] + 1][attemptBranch[1]][0] == 1:
            valid = False
        if field[attemptBranch[0]][attemptBranch[1] - 1][0] == 1 or field[attemptBranch[0]][attemptBranch[1] + 1][0] == 1:
            valid = False

        # if valid place branch
        if valid:
            field[attemptBranch[0]][attemptBranch[1]][0] = 1

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
            attemptBranch[0] += j
            attemptBranch[1] += k
            field[attemptBranch[0]][attemptBranch[1]][0] = 1
            if i == 0:
                llBranchesHead = Branch(attemptBranch)
                llBranchesTail = llBranchesHead
            else:
                llBranchesTemp = Branch(attemptBranch)
                llBranchesTail.next = llBranchesTemp
                llBranchesTail = llBranchesTemp

    # test to be removed
    llBranchesHeadTemp = llBranchesHead
    while llBranchesHeadTemp != None:
        location = llBranchesHeadTemp.data
        print(f"({location[0]},{location[1]})")
        llBranchesHeadTemp = llBranchesHeadTemp.next

    print("endloop")

    # for linked list fill area
    BranchHead(llBranchesHead, llBranchesTail, field, random, height, width)


    return field

def BranchHead(llBranchesHead, llBranchesTail, field, random, height, width):
    # loop till list is empty

    count = 0
    while llBranchesHead != None and count < 700:

        printList(llBranchesHead)

        location = llBranchesHead.data

        # add priority to run forward
        direction = [[-1,0],[1,0],[0,1],[0,-1]]

        # loop for all directions
        maxPaths = random.randint(1, 1)
        numPaths = 0
        loops = 0
        print(f"checking around ({location[0]},{location[1]})")
        while numPaths <= maxPaths and loops <= 3:
            # select a random direction
            print("len ", len(direction), "paths ", numPaths, "maxpaths", maxPaths)
            if len(direction) == 1:
                directionID = 0
            else:
                directionID = random.randint(0, len(direction) - 1)
            print(directionID)
            checkDirection = direction[directionID]

            # save new location to blockCheck
            blockCheck = [location[0] + checkDirection[0], location[1] + checkDirection[1]]

            print("checking ", blockCheck)
            # if a wall
            if field[blockCheck[0]][blockCheck[1]][0] == -1:

                checkAround = [[[0, -1],[-1, -1], [-1, 0]], [[-1, 0], [-1, 1], [0, 1]], [[0,1], [1,1], [1,0]], [[1,0], [1,-1], [0,-1]]]
                for four in checkAround:
                    valid = False
                    for single in four:
                        tempBlockCheck = [blockCheck[0] + single[0], blockCheck[1] + single[1]]
                        #print(tempBlockCheck)
                        if tempBlockCheck[0] > 0 and tempBlockCheck[1] > 0 and tempBlockCheck[0] < height - 1  and tempBlockCheck[1] < width - 1:
                            if field[tempBlockCheck[0]][tempBlockCheck[1]][0] == -1:
                                valid = True
                    if not valid:
                        break

                #print(valid)
                if valid:
                    print("valid place")
                    numPaths += 1
                    field[blockCheck[0]][blockCheck[1]][0] = 1
                    llBranchesTail.next = Branch(blockCheck)
                    llBranchesTail = llBranchesTail.next

            # remove that direction
            direction.pop(directionID)
            loops += 1

        # move to next node
        print(f"({blockCheck[0]},{blockCheck[1]})")
        print(count)
        llBranchesHead = llBranchesHead.next
        #print("loop")
        count += 1


def printList(llBranchesHead):
    # test to be removed
    llBranchesHeadTemp = llBranchesHead
    while llBranchesHeadTemp != None:
        location = llBranchesHeadTemp.data
        print(f"({location[0]},{location[1]})")
        llBranchesHeadTemp = llBranchesHeadTemp.next