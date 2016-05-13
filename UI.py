import tkinter as tk
from tkinter import *
import random
import tkinter.messagebox as mBox


from NewGame import *

class DisplayFunds():
    def __init__(self, fund , root):
        menubar.entryconfig("Game", state = "disabled")
        self.frm = Frame(root)
        self.frm.pack()
        self.frm.lblFunds = tk.Label (self.frm,text = "Funds: " + str(fund[0]), width  =25, height = 5)
        self.frm.lblFunds.grid(row=0, column = 0)
        self.frm.btnReturn = tk.Button (self.frm, text = "Ok", width =15, command = self.close)
        self.frm.btnReturn.grid(row=1, column = 0)

    def close(self):
        menubar.entryconfig("Game", state = "normal")
        self.frm.destroy()


def ResetFunds(fund):
    menubar.entryconfig("Game", state = "disabled")
    isSure = mBox.askyesno("Reset Winning", "Are you sure?")
    if (isSure == True):
        fund[0] = 0
    menubar.entryconfig("Game", state = "normal")

def exitGame():
    isSure = mBox.askyesno("Reset Winning", "Are you sure?")
    if (isSure == True):
        root.destroy()

'''Main Window'''
def combine_funcs(*funcs):
    def combined_func(*args, **kwargs):
        for f in funcs:
            f(*args, **kwargs)
    return combined_func

def lockMenu():
    menubar.entryconfig("Game", state = "disabled")

fund= []
fund.append(0)
root = Tk()
root.title('Black Jack by Hanfei')
root.geometry('450x150')
root.resizable(width=FALSE, height=FALSE)

'''Menu '''
menubar = Menu(root)
mainmenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Game", menu=mainmenu)
mainmenu.add_command(label="Play the Game", command= combine_funcs(lockMenu, lambda: NewGame(fund, root, menubar, mainmenu)))
mainmenu.add_command(label="Display Available Funds", command=lambda : DisplayFunds(fund, root))
mainmenu.add_command(label="Reset Winning to Zero", command=lambda: ResetFunds(fund))
mainmenu.add_command(label="Quit", command=exitGame)
root.config(menu=menubar)


root.mainloop()





