import tkinter as tk
from tkinter import *
import random
import tkinter.messagebox as mBox

from Card import *

class NewGame(Frame):
    
    '''Draw game board'''
    def __init__(self, fund, root, menubar, mainmenu):
        self.fund = fund
        self.root = root
        self.menubar = menubar        
        self.mainmenu = mainmenu
        self.frm = Frame(root)
        self.frm.pack()
        self.frm.point = 0
        self.frm.isSoft = True
        self.frm.hasAce = False
        '''Create card deck'''
        self.frm.deck = []
        self.frm.size = 52
        self.frm.suits = ["Spade", "Heart", "Diamond", "Club"]
        self.frm.nums = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        self.frm.cardStrList = []
        self.frm.cardLblList = []
        self.frm.numOfDraw = 0
        '''Create card deck'''
        for j in range (0, 4):
            for i in range (0, 13):
                newCard = Card(self.frm.suits[j], self.frm.nums[i])
                self.frm.deck.append(newCard)

        '''Display card history'''
        for i in range (0, 16):
            cardString = StringVar()
            cardString.set("Card holder")
            self.frm.cardStrList.append(cardString)
            cardLabel = tk.Label(self.frm,textvariable = self.frm.cardStrList[i], width =20 )
            self.frm.cardLblList.append (cardLabel)
        
        for i in range (0, 8):
            self.frm.cardLblList[i].grid(row = i, column = 0, sticky = W+E)
        
        for i in range (8, 16):
            self.frm.cardLblList[i].grid(row = (i-8), column = 2, sticky = W+E)

        '''Interactive area'''
        
        self.frm.pointStr = StringVar() 
        self.frm.pointStr.set( "Current Point: " + str(self.frm.point) )
        lblPoint = tk.Label (self.frm,textvariable = self.frm.pointStr, width = 20)
        lblPoint.grid(row = 0, column = 1, rowspan = 2, sticky = W+E+N+S)
       
        self.frm.cardStr = StringVar() 
        self.frm.cardStr.set( "Card1: "  )
        lblCard = tk.Label( self.frm,textvariable = self.frm.cardStr, width = 20)
        lblCard.grid(row = 2, column = 1, rowspan = 2, sticky = W+E+N+S)

        self.frm.card2Str = StringVar() 
        self.frm.card2Str.set( "Card2: ")
        lblCard2 = tk.Label( self.frm,textvariable = self.frm.card2Str , width = 20)
        lblCard2.grid(row = 4, column = 1, rowspan = 1, sticky = W+E+N+S)
            
        btnPlay = tk.Button(self.frm, text = "Draw cards", width = 15, command = self.play )
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
        self.frm.size = self.frm.size - 1
        self.frm.numOfDraw = self.frm.numOfDraw + 1
        return card
    '''returns a list of 2 cards'''

    def calcSum(self, oldSum, card):
        if (card.getNum() == "A" ):
            if (self.frm.hasAce == False):
                if (oldSum <10):
                    card.setValue(1)
                    self.frm.isSoft = True                    
                elif(oldSum == 10):
                    card.setValue(11)
                    self.frm.isSoft = False
                else:
                    card.setValue(1)
                    self.frm.isSoft = False
                self.frm.hasAce = True
            elif(self.frm.isSoft == True):
                if (oldSum < 10):
                    card.setValue(1)
                elif (oldSum == 10):
                    card.setValue(11)
                    self.frm.isSoft = False
                else:
                    card.setValue(1)
                    self.frm.isSoft = False
            else:
                card.setValue(1)
        else:
            if (self.frm.hasAce == False):
                pass
            elif (self.frm.isSoft == True):
                if ((oldSum + card.value)<11):
                    pass
                elif ((oldSum + card.value) == 11):
                    self.frm.point += 10
                    self.frm.isSoft == False
                else:
                    self.frm.isSoft == False
            else:
                pass
            
        self.frm.point += card.value

    '''handles all the steps of game'''
    def play(self):
           
        if (self.frm.size < 1 or self.frm.numOfDraw > 15): 
            pass #TODO popup message 
        elif (self.frm.numOfDraw == 0): #first draw by user, draw 2 times
            card1=self.drawCards(self.frm.deck,self.frm.size)
            self.calcSum(self.frm.point, card1)
            self.frm.cardStr.set("Card: " + card1.toStr())
            self.frm.cardStrList[self.frm.numOfDraw - 1].set("Card: " + card1.toStr())
            
            card2=self.drawCards(self.frm.deck,self.frm.size)
            self.calcSum(self.frm.point, card2)
            self.frm.card2Str.set("Card2: " + card2.toStr())
            self.frm.cardStrList[self.frm.numOfDraw - 1].set("Card: " + card2.toStr())

            self.frm.pointStr.set("Current Point: " + str(self.frm.point))       
        else: # after 1st draw, draw 1 card each time
            '''Draw cards'''
            card = self.drawCards(self.frm.deck, self.frm.size)
            self.calcSum(self.frm.point, card)
            '''Redraw play board'''
            self.frm.card2Str.set("")
            self.frm.cardStr.set("Card: " + card.toStr())
            self.frm.cardStrList[self.frm.numOfDraw - 1].set("Card: " + card.toStr())
            self.frm.pointStr.set("Current Point: " + str(self.frm.point))

            
        '''Update status'''
        if (self.frm.point<21) :
            isContinue = mBox.askyesno("Continue?", "Not reached 21, Continue?")
            if (isContinue == False):
                self.resetGame()
        elif (self.frm.point == 21):
            self.fund[0] += 100
            print("fund: " + str(self.fund[0]))
            isNewRound = mBox.askyesno("Win", "You Win ! Start anthoer round?")
            if (isNewRound == False):
                self.resumeMenu()
                self.endGame(self.frm)
            else:
                self.resetGame()            
        else:
            self.fund[0] -=50
            print("fund: " + str(self.fund[0]))

            if (self.fund[0]<= -1000):
                mBox.showinfo("Out of funds", "You run out of funds! Please exit")
                self.endGame(self.frm)
                self.resumeMenuWithExit()
            else:
                isNewRound = mBox.askyesno("Lose", "You Lose ! Start anthoer round?")
                if (isNewRound == False):
                    self.resumeMenu()
                    self.endGame(self.frm)
                else:
                    self.resetGame()
                
           

    def resetGame(self):
        for j in range (0, 4):
            for i in range (0, 13):
                newCard = Card(self.frm.suits[j], self.frm.nums[i])
                self.frm.deck.append(newCard)

        self.frm.size = 52
        self.frm.numOfDraw = 0
        
        self.frm.point = 0
        self.frm.pointStr.set( "Current Point: " + str(self.frm.point) )
        self.frm.cardStr.set( "Card1: "  )
        self.frm.card2Str.set("Card2: " )
        for i in range (0, 16):
            self.frm.cardStrList[i].set("Card: ")
        
    def endGame(self, frame):
        frame.destroy()

    
    def resumeMenu(self):
        self.menubar.entryconfig("Game", state = "normal")

    def resumeMenuWithExit(self):
        self.menubar.entryconfig("Game", state = "normal")
        self.mainmenu.entryconfig(0, state = "disabled")
        self.mainmenu.entryconfig(1, state = "disabled")
        self.mainmenu.entryconfig(2, state = "disabled")
