'''
Vált = eredmény : lista
függvény Kódol(Kép, kód )
    ha hossz(Kép)==1 akkor
        eredmény.hozzáfűz(Kód+"0"+Kép[0])

    ha azonos(Kép) akkor
        eredmény.hozzáfűz(Kód+"0"+Kép[0][0])
    különben
        Részek = Darabolás(Kép)
        Kódol(Részek[0], kód+"1")    -> ez a bal felső sarka a kis négyesnek
        Kódol(Részek[1]), kód+"2")
        Kódol(Részek[2], kód+"3")
        Kódol(Részek[3], kód+"4")

függvény Darabolás(Kép)
    Részek=[]*4
    N2 = Hossz(Kép)/2      -> ez a fele , a példában ez 2 lesz (két sor)
    N = Hossz(Kép)         -> példában ez 4 lesz
    Ciklus i = 1 ... N-ig
        ha i<=N2
            Részek[0].hozzáfűz(Kép[i][0:N2])     -> a példában először [[a,b]] majd [[a,b],[b,b]]
            Részek[1].hozzáfűz(Kép[i][N2:])      -> [[b,b],[b,b]]
        különben
            Részek[2].hozzáfűz(Kép[i][0:N2])
            Részek[3].hozzáfűz(Kép[i][N2:])
    return Részek

függvény Azonos(Kép) : logikai     -> az első sor ugyanolyan és a többi sor ugyanolyan mint az első
        segéd = Igaz
        Ha Hossz(Kép)==1 akkor return segéd
        i=0
        ciklus amíg i<Hossz(Kép[0]) és Kép[0][0]==Kép[0][i]
            i +=1
        Ha i<Hossz(Kép[0])
            segéd = False
            return segéd
        különben    -> egy sor ugyanaz
            i=1
            ciklus amíg i<Hossz(Kép) és Kép[0] == Kép[i]
                i+=1
            Ha i <Hossz(Kép)
                segéd = False
                return segéd
            különben
                return segéd
'''
def beolvasas() :
    N=int(input())
    Kep=[]
    for i  in range (N):
        Kep.append(input())
    return Kep

def felbontas(Kep) :
    n=len(Kep)
    n2 = n//2
    Részek= [[],[],[],[]]
    for i in range (n):
        if i<n2:
            Részek[0].append(Kep[i][0:n2])
            Részek[1].append(Kep[i][n2:])
        else:
            Részek[2].append(Kep[i][0:n2])
            Részek[3].append(Kep[i][n2:])

    return Részek

def azonos(Kep):
    if len(Kep) == 1:
        return True
    else:
        i = 1
        while i < len(Kep) and Kep[0][0] == Kep[0][i]:
            i+=1
        azon=i>=len(Kep)
        if azon :
            i = 0
            while i<len(Kep) and Kep[0]==Kep[i]:
                i+=1
                azon=i>=len(Kep)
        return azon

def kodol(Kep, kod):    
    if len(Kep) == 1:
        Eredmeny.append(kod+"0"+Kep[0])
    else:
        if azonos(Kep):
            Eredmeny.append(kod+"0"+Kep[0][0])
        else:
            Részek=felbontas(Kep)
            for i in range (4):
                kodol(Részek[i], kod+str(i+1))
   
Kep=beolvasas()
Eredmeny=[]
kodol(Kep, "")
print (str(len(Kep))+" "+str((len(Eredmeny))))
for elem in Eredmeny:
    print (elem)
#print (Eredmeny)
#Részek=felbontas(Kep)
#if azonos (Kep):
#    print ("azonos")
#else:
   # print ("nem azonos")
#print(Részek[0])

