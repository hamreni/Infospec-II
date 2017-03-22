def binom (n,k):
    if k>n :
        raise Exception()
    if k==0 or k==n:
        return 1

    else:
       return binom(n-1, k) + binom(n-1, k-1)

n=int(input())
k=int(input())

try:
    print (str(n)+"/"+str(k)+"="+str (binom(n,k)))
except:
    print ("k-nak kisebbnek vagy egyenlőnek kell lennie az n-nel")
    # jobb ha nem a fv visszatérését módosítgatjuk

#for i in range (n+1):
 #   s=""
  #  for j in range (i+1):
    #    s+= str(binom(i,j))+" "
      #  print (s)

