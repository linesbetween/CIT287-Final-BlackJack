import tkinter as tk
from tkinter import *
import random

class Card():
    def __init__(self, suit, num):

        self.suit = suit
        self.num = num
        if (num.isnumeric()):
            self.value = int(num) 
        else:
            self.value = 10

    def toStr(self):
        return "%s of %s " % ( self.num, self.suit)

    def __str__( self ):
        return "%s of %s value %d" % ( self.num, self.suit, self.value )

def donothing():
    filewin = Toplevel(root)
    button = Button(filewin, text="Do nothing button")
    button.pack()

class Game():
    
    initFund = 1000
    point = 0
    '''Create card deck'''
    deck = []
    size = 52
    suits = ["Spade", "Heart", "Diamond", "Club"]
    nums = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    cardStrList = []
    cardLblList = []
    numOfDraw = 0


    '''Draw game board'''
    def __init__(self):

        for j in range (0, 4):
            for i in range (0, 13):
                newCard = Card(self.suits[j], self.nums[i])
                self.deck.append(newCard)

        '''Drawn card display area'''
        for i in range (0, 16):
            cardString = StringVar()
            cardString.set("Card")
            self.cardStrList.append(cardString)
            cardLabel = tk.Label(textvariable = self.cardStrList[i])
            self.cardLblList.append (cardLabel)
        
        for i in range (0, 8):
            self.cardLblList[i].grid(row = i, column = 0, sticky = W+E+N+S)
        
        for i in range (8, 16):
            self.cardLblList[i].grid(row = (i-8), column = 2, sticky = W+E+N+S)

        card1=self.drawCards(self.deck,self.size)
        self.calcSum(self.point, card1)
        card2=self.drawCards(self.deck,self.size)
        self.calcSum(self.point, card2)

        '''Interactive area'''
        
        self.pointStr = StringVar() 
        self.pointStr.set( "Current Point: " + str(self.point) )
        lblPoint = tk.Label (textvariable = self.pointStr, width = 25)
        lblPoint.grid(row = 0, column = 1, rowspan = 2, sticky = W+E+N+S)
       
        self.cardStr = StringVar() 
        self.cardStr.set( "Card1: " + card1.toStr() )
        self.cardStrList[0].set("Card: " + str(card1.toStr()))
        lblCard = tk.Label( textvariable = self.cardStr, width = 25)
        lblCard.grid(row = 2, column = 1, rowspan = 2, sticky = W+E+N+S)

        self.card2Str = StringVar() 
        self.card2Str.set( "Card2: " + card2.toStr())
        self.cardStrList[1].set("Card: " + card2.toStr())
        lblCard2 = tk.Label( textvariable = self.card2Str , width = 25)
        lblCard2.grid(row = 4, column = 1, rowspan = 1, sticky = W+E+N+S)
            
        btnPlay = tk.Button( text = "Draw cards", width = 15, command = self.play )
        btnPlay.grid(row = 5, column = 1, rowspan = 2, sticky = W+E+N+S)

    '''receives the deck and size'''
    def drawCards(self,deck,size):        
        randNum = random.randrange(0,size)
        card = deck[randNum]
        del deck[randNum];
        #rand2 = random.randrange(0,size - 1)
        #card2 = deck [rand2]
        #del deck[rand2];
        #cardPair = [card1, card2]
        self.size = self.size - 1
        self.numOfDraw = self.numOfDraw + 1
        return card
    '''returns a list of 2 cards'''

    def calcSum(self, oldSum, card):
        self.point = oldSum + card.value 

    '''handles all the steps of game'''
    def play(self):
        if (self.numOfDraw == 2): #first draw by user
            self.card2Str.set("")
        if (self.size < 1 or self.numOfDraw > 15
            ): 
            pass #TODO popup message 
        else:
            '''Draw cards'''
            card = self.drawCards(self.deck, self.size)
            '''Calculate points'''
            self.calcSum(self.point, card)
            '''Update status'''
            if (self.point<21) :
                done = False
                is21 = False
            elif (self.point == 21):
                done = True
                is21 = True
            else:
                done = True
                is21 = False
            

            '''Redraw play board'''
            self.cardStr.set("Card: " + card.toStr())
            self.cardStrList[self.numOfDraw - 1].set("Card: " + card.toStr())
            self.pointStr.set("Current Point: " + str(self.point))
            
            
        #return (status[done, is21], point, size) #return value not used
        
    
    def resume():
        menubar.entryconfig("Game", state = "normal")
    
    #to draw cards, display cards, calculate sum, decide winning.


"""
class GameUI():
    def __init__(self):
       
        
        self.lblCard1 = tk.Label( text = "Card1: " , width = 25)
        self.lblCard1.place(x = 80, y = 30)

        self.lblCard2 = tk.Label( text = "Card2: " , width = 25)
        self.lblCard2.place(x = 80, y = 60)
        
        self.btnPlay = tk.Button( text = "Draw cards", width = 15,
                               command = self.shutdown )
        self.btnPlay.place(x = 175 , y = 100)

    def shutdown(self):
        pass
"""
class DisplayFunds(Frame):
    def __init__(self):
        new = tk.Frame.__init__(self)
        new = Toplevel(self)
        new.title("Display Funds")
        new.geometry('300x100')
        new.lblFunds = tk.Label (new,text = "Funds: ", width  =25)
        new.lblFunds.place(x=20, y = 20)
        new.btnReturn = tk.Button (new, text = "Return", width =15, command = self.close)
        new.btnReturn.place(x=100, y = 50)

    def close(self):
        self.destroy()


class ResetFunds(Frame):
    def __init__(self):
       
        new = tk.Frame.__init__(self)
        new = Toplevel(self)
        new.title("Reset Funds")
        new.geometry('300x100')
        new.lblFunds = tk.Label (new,text = "Funds: ", width  =25)
        new.lblFunds.place(x=20, y = 20)
        new.btnReturn = tk.Button (new, text = "Return", width =15, command=self.close)
        new.btnReturn.place(x=100, y = 50)

    def close(self):
        self.destroy()

def combine_funcs(*funcs):
    def combined_func(*args, **kwargs):
        for f in funcs:
            f(*args, **kwargs)
    return combined_func

def lockMenu():
    menubar.entryconfig("Game", state = "disabled")

root = Tk()
root.title('Black Jack by Hanfei')
root.geometry('450x150')

'''Menu part'''
menubar = Menu(root)
mainmenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Game", menu=mainmenu)
mainmenu.add_command(label="Play the Game", command= combine_funcs(lockMenu,Game))
mainmenu.add_command(label="Display Available Funds", command=DisplayFunds)
mainmenu.add_command(label="Reset Funds to Zero", command=ResetFunds)
mainmenu.add_command(label="Quit", command=donothing)




root.config(menu=menubar)
root.mainloop()





