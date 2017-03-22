
def Hanoi (db, honnan, hova,mivel) 	#mivel a segédút
	if n>1:
		hanoi(n-1,honnan,mivel,hova)
		print (honnan+"->" +hova)
        hanoi(n-1,mivel,hova,honnan)
        
n=int(input())
hanoi (n,"A","B","C")