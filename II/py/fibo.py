def fibo(n):
    if n==0 or n==1:
        return 1
    else:
        return fibo(n-1)+fibo(n-2)

n=int(input())
for i in range (1,n):
    print (str(i)+". fibonacci szam:"+str (fibo(i)))
