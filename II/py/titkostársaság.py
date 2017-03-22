class Fa:
    def __init__(self, gyoker):
        self.gyoker = gyoker
        self.bal = None
        self.jobb = None
   
    def BalGyerek(self):
        return self.bal
    def JobbGyerek(self):
        return self.jobb
    def GyokerModosit(self,value):
        self.gyoker = value
    def GyokerElem(self):
        return self.gyoker
    def JobbraIlleszt(self,jobb):
        self.jobb=jobb
        return self
    def BalraIlleszt(self,bal):
        self.bal=bal
        return self
    def BKJ(self):       
        if self.bal!=None:
            Fa.BKJ(Fa.BalGyerek(self))
        print(self.gyoker)
        if self.jobb!=None:
             Fa.BKJ(Fa.JobbGyerek(self))
class KFa(Fa):
    def Keres(self,mit):
       
        if self!=None:
            
            if Fa.GyokerElem(self)==mit:              
                return self
            else:          
                valasz=KFa.Keres(Fa.BalGyerek(self),mit)
                if valasz==None:
                    return KFa.Keres(Fa.JobbGyerek(self),mit)
                else:
                    return valasz   
        else:
            return None

    def Level(self):
        return self.bal==None and self.jobb==None
    

def beolvas():
    N=int(input())
    adatok= []
    for i in range (N-1):
        sor=input().split()
        adatok.append((sor[0], sor[1]))
    return adatok
def felepit(adatok):
    fa=KFa("1")
    for i in range (len(adatok)):
        hova=KFa.Keres(fa,adatok[i][0])
        if adatok[i][1] == "A":
              KFa.BalraIlleszt(hova,KFa(str(i+2)))
        else:
               KFa.JobbraIlleszt(hova,KFa(str(i+2)))
    return fa

def közvetlen(fa):
    s = 0
    if fa.bal == None:
        s += 1
    if fa.jobb == None:
        s += 1
    return s #lehetőségek száma

def beosztott(fa):
    if fa==None:
        return 1
    else:
        return beosztott(fa.bal)+beosztott(fa.jobb)


adatok=beolvas()
fa=felepit(adatok)
print (közvetlen(fa))
if fa.bal == None:
    print (0)
else:
    print (beosztott(fa.bal))
if fa.jobb == None:
    print (0)
else:
    print (beosztott(fa.jobb))
#KFa.BKJ(fa)

#print (adatok)