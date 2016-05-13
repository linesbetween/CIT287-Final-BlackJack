class Card():
    def __init__(self, suit, num):

        self.suit = suit
        self.num = num
        if (num.isnumeric()):
            self.value = int(num) 
        else:
            self.value = 10

    def getNum(self):
        return self.num

    def setValue(self,value):
        self.value = value

    def toStr(self):
        return "%s of %s " % ( self.num, self.suit)

    def __str__( self ):
        return "%s of %s value %d" % ( self.num, self.suit, self.value )
