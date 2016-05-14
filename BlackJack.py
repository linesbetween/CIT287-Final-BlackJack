import tkinter as tk
from tkinter import *
import random
import tkinter.messagebox as mBox


from NewGame import *
from DisplayFunds import *


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

def clearDisplay():
    panel1.pack_forget()

fund= []
fund.append(0)
root = Tk()
root.title('Black Jack by Hanfei')
root.geometry('450x150')
root.resizable(width=FALSE, height=FALSE)

'''Welcome pic'''
image1 = tk.PhotoImage(file="cardpic.gif")
#image1.resize (450, 150)
panel1 = tk.Label(root, image=image1)
panel1.pack(side='top', fill='both', expand='yes')
lblWelcome = tk.Label(panel1, text = "Welcome!",width = 5, padx = 75, font = "Helvetica 16 bold italic" )
lblWelcome.pack(side='right')

'''Menu '''
menubar = Menu(root)
mainmenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Game", menu=mainmenu)
mainmenu.add_command(label="Play the Game", command= combine_funcs(lockMenu, clearDisplay, lambda: NewGame(fund, root, menubar, mainmenu)))
mainmenu.add_command(label="Display Available Funds", command= combine_funcs ( clearDisplay, lambda : DisplayFunds(fund, root, menubar)))
mainmenu.add_command(label="Reset Winning to Zero", command= combine_funcs (clearDisplay, lambda: ResetFunds(fund)))
mainmenu.add_command(label="Quit", command=exitGame)
root.config(menu=menubar)


root.mainloop()





