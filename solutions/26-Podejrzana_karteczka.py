def litery(l):
	wynik=0
	for i in range(len(l)):
		if (l[i]>='a' and l[i]<='z') or (l[i]>='A' and l[i]<='Z'):
			wynik=wynik+1
	return wynik
def cyfry(l):
	wynik=0
	for i in range(len(l)):
		if l[i]>='0' and l[i]<='9':
			wynik=wynik+1
	return wynik
	
n=int(input())
A=[]
for i in range(n):
	A.append(input())
	print(len(A[i]), litery(A[i]), cyfry(A[i]))