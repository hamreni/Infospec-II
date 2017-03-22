class Fa:
    def __init__(self, gyoker):
        self.gyoker = gyoker
        self.bal = None
        self.jobb = None

    def UresE(self):
        ures = self == None
        return ures
    
    def Beszur(self, elem):
        if elem.gyoker < self.gyoker :
            if self.bal == None:
                self.bal = elem
            else:
                Fa.Beszur(Fa.BalGyerek(self), elem)
        else:
            if self.jobb == None:
                self.jobb = elem
            else:
                Fa.Beszur(Fa.JobbGyerek(self), elem)

    def BalGyerek(self):
        return self.bal
   
    def BalraIlleszt(self,bal):
        self.bal=bal
        return self
    def JobbGyerek(self):
        return self.jobb
    def JobbraIlleszt(self,jobb):
        self.jobb=jobb
        return self
    def GyokerElem(self, gyoker):
        self.gyoker=gyoker
        return gyoker
    

    def BKJ(self):
       if not Fa.UresE(self):
            Fa.BKJ(self.bal)
            print (self.gyoker)
            Fa.BKJ(self.jobb)

           
adatok=[1,2,5,3,9,4,15]

bf=Fa(adatok[0])
for i in range (1,len(adatok)):
    Fa.Beszur(bf, Fa(adatok[i]))

#bf=Fa.BalraIlleszt(bf,Fa(2))
Fa.BKJ(bf)
#print(ki)