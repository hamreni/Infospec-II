A=[]
def beolv():
    n=int(input())
    for i in range (n):
        A.append(int(input()))

def quick(E,V):
    K=Szetvalogat(E,V)
    if K-E>1:
        quick(E,K-1)
    if V-K>1:
        quick(K+1,V)

def Szetvalogat(E,V):
    segéd=A[E]# egy elem kiemelése
    while E<V:#amíg az eleje és a vége összeér
        while E<V and A[V]>segéd:
            V=V-1
        if E<V: #talált, mert megállt a ciklus
            A[E] = A[V]
            E=E+1
            while E<V and A[E]<segéd:
                E=E+1
            if E<V:
                A[V] = A[E]
                V=V-1
    A[E] = segéd
    return E 

beolv()
quick(0,len(A)-1)
print(A)