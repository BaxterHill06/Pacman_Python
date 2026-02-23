from Game import *


def MakeLobby(window):
    frmLobby = Frame(window, bg="black")
    lblTitle = Label(frmLobby, text="Pacman", font=("Times new roman", 28), fg="white", bg="black")
    btnStart = Button(frmLobby, command= lambda : StartGame(frmLobby, window, 25,25, 3))
    lblTitle.pack()
    btnStart.pack()
    frmLobby.pack()

