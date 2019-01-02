m,n=input().split()
m=int(m)
n=int(n)
A=input().split()
A=[int(i) for i in A]
B=[]
B=[B.append(0) for i in range(0,m+1)]
for i in range(m+1):
	B[i]=0
for i in A:
	B[i]=B[i]+1
wygrany=1
for i in range(1,m+1):
	print(i,B[i],sep=": ")
	if B[wygrany]<B[i]:
		wygrany=i
print(wygrany)