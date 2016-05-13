import tkinter as tk
from tkinter import *


class DisplayFunds():
    def __init__(self, fund , root, menubar):
        self.fund = fund
        self.menubar = menubar
        self.menubar.entryconfig("Game", state = "disabled")
        self.frm = Frame(root)
        self.frm.pack()
        self.frm.lblFunds = tk.Label (self.frm,text = "Funds: " + str(self.fund[0]), width  =25, height = 5)
        self.frm.lblFunds.grid(row=0, column = 0)
        self.frm.btnReturn = tk.Button (self.frm, text = "Ok", width =15, command = self.close)
        self.frm.btnReturn.grid(row=1, column = 0)

    def close(self):
        self.menubar.entryconfig("Game", state = "normal")
        self.frm.destroy()
